from django.shortcuts import render
from .models import  Equipment, Journal, Comments, User, Messages, SchemaEquipment
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import SearchForm, JournalForm, CommentForm, SendMessage
from django.shortcuts import get_object_or_404


class PostListView(LoginRequiredMixin,ListView):
    queryset = Equipment.objects.all()
    total = queryset.count()
    context_object_name = 'posts'
    paginate_by = 6
    template_name = 'users/index.html'

    extra_context = {
        'total': total
    }



class ProfileListView(LoginRequiredMixin, ListView):
    model = User
    paginate_by = 2
    template_name = 'users/list_profiles.html'
    context_object_name = 'users'
    
    def get_queryset(self):
        return User.objects.all()


@login_required
def profile(request):
    return render(request,
                'users/profile.html',
                {'title': 'Кабинет пользователя'})  


@login_required
def detail_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request,
                'users/profile_detail.html',
                {'user': user})   


@login_required
def profile_messages_input(request, pk):
    messages = Messages.objects.filter(owner=pk)
    return render(request,
                'users/profile_messages_input.html',
                {'messages': messages})   


@login_required
def profile_messages_output(request, pk):
    messages = Messages.objects.filter(sender=pk)
    return render(request,
                'users/profile_messages_output.html',
                {'messages': messages})  


class CategoryListView(LoginRequiredMixin, ListView):
    model = Equipment
    paginate_by = 6
    template_name = 'users/show_categories.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        return Equipment.objects.filter(cat__slug=self.kwargs['cat_slug'])
    

class TagListView(LoginRequiredMixin, ListView):
    model = Equipment
    paginate_by = 6
    template_name = 'users/show_categories.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        return Equipment.objects.filter(tags__slug=self.kwargs['tag_slug'])


class JournalListView(LoginRequiredMixin, ListView):
    model = Journal
    paginate_by = 10 
    template_name = 'users/journal.html'
    context_object_name = 'records'

    def get_queryset(self):
        return Journal.objects.prefetch_related('equipment').all()
    

class SchemaEquipmentListView(LoginRequiredMixin, ListView):
    model = SchemaEquipment 
    paginate_by = 10 
    template_name = 'users/schema_equipment.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return SchemaEquipment.objects.all()    


class CommentListView(LoginRequiredMixin, ListView):
    model = Comments
    paginate_by = 10 
    template_name = 'users/comment.html'
    context_object_name = 'records'

    def get_queryset(self):
        return Comments.objects.prefetch_related('equipment').all()


class ShowDetailEquipment(LoginRequiredMixin, DetailView):
    model = Equipment
    slug_url_kwarg = 'post_slug'
    template_name = 'users/detail.html'
    context_object_name = 'equipment'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['journals'] = Journal.objects.prefetch_related('equipment').filter(equipment__slug=self.kwargs['post_slug'])
        context['comments'] = Comments.objects.prefetch_related('equipment').filter(equipment__slug=self.kwargs['post_slug'])
        return context
    

class JournalRecordsEquipment(LoginRequiredMixin, ListView):
    model = Equipment
    paginate_by = 10
    slug_url_kwarg = 'equipment_slug'
    template_name = 'users/journal_equipment_records.html'
    context_object_name = 'records'
    
    def get_queryset(self):
        records = Journal.objects.prefetch_related('equipment').filter(equipment__slug=self.kwargs['equipment_slug'])
        return records


class CommentRecordsEquipment(LoginRequiredMixin, ListView):
    model = Equipment
    paginate_by = 10
    slug_url_kwarg = 'equipment_slug'
    template_name = 'users/comment_equipment_records.html'
    context_object_name = 'records'
    
    def get_queryset(self):
        records = Comments.objects.prefetch_related('equipment').filter(equipment__slug=self.kwargs['comment_slug'])
        return records


@login_required
def profile_comments(request, pk):
    comments = Comments.objects.filter(user=pk)
    return render(request,
                'users/profile_comments.html',
                {'comments': comments}) 


@login_required
def profile_journals(request, pk):
    journals = Journal.objects.filter(user=pk)
    return render(request,
                'users/profile_journal.html',
                {'journals': journals}) 


@login_required
def journal_record(request):
    if request.method == 'POST':
        form = JournalForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = JournalForm()       
         
    return render(request,
                'users/record_successfully.html',
                {'form': form,
                 'title': 'Запись успешна сохранена в журнале'
                })   


@login_required
def comment_record(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CommentForm()       
         
    return render(request,
                'users/record_successfully.html',
                {'form': form,
                 'title': 'Комментарий успешно сохранен'
                })   


@login_required
def search_equipment(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Equipment.objects.filter(title__icontains=query)
            total = results.count()
    else:
        form = SearchForm()       
         
    return render(request,
                'users/search_result.html',
                {'form': form,
                'posts': results,
                'total': total
                })        


@login_required
def search_journal(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Journal.objects.filter(equipment__title__icontains=query)
            total = results.count()
    else:
        form = SearchForm()       
         
    return render(request,
                'users/journal_search.html',
                {'form': form,
                'posts': results,
                'total': total
                })  


@login_required
def search_comment(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Comments.objects.filter(equipment__title__icontains=query)
            total = results.count()
    else:
        form = SearchForm()       
         
    return render(request,
                'users/comment_search.html',
                {'form': form,
                'posts': results,
                'total': total
                })  


@login_required
def search_profile(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query'].split()
            if len(query) > 1:
                users = User.objects.filter(last_name__icontains=query[0],
                                            first_name__icontains=query[1])
            elif len(query) == 1:
                users = User.objects.filter(last_name__icontains=query[0])
            total = users.count()
    else:
        form = SearchForm()       
         
    return render(request,
                'users/profile_search.html',
                {'form': form,
                'users': users,
                'total': total
                }) 


@login_required
def profile_search_comments(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Comments.objects.filter(equipment__title__icontains=query)
            total = results.count()
    else:
        form = SearchForm()       
         
    return render(request,
                'users/profile_search_comments.html',
                {'form': form,
                'comments': results,
                'total': total
                })   


@login_required
def profile_search_journal(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Journal.objects.filter(equipment__title__icontains=query)
            total = results.count()
    else:
        form = SearchForm()       
         
    return render(request,
                'users/profile_search_journals.html',
                {'form': form,
                'journal': results,
                'total': total
                })  


@login_required
def send_message(request):
    if request.method == 'POST':
        form = SendMessage(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SendMessage()       
    return render(request,
                'users/message_successfully.html',
                {'form': form,
                 'title': 'Сообщение успешно отправлено'
                })   
 

@login_required
def profile_message_output(request):
    user_output_messages = Messages.objects.filter(sender=request.user.pk)
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query'].split()
            if len(query) > 1:
                messages = user_output_messages.filter(owner__last_name__icontains=query[0],
                                            owner__first_name__icontains=query[1])
            elif len(query) == 1:
                messages = user_output_messages.filter(owner__last_name__icontains=query[0])
            total = messages.count()    
    else:
        form = SearchForm()       
         
    return render(request,
                'users/profile_search_output_messages.html',
                {'form': form,
                'messages': messages,
                'total': total,
                }) 


@login_required
def profile_message_input(request):
    user_output_messages = Messages.objects.filter(owner=request.user.pk)
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query'].split()
            if len(query) > 1:
                messages = user_output_messages.filter(sender__last_name__icontains=query[0],
                                            sender__first_name__icontains=query[1])
            elif len(query) == 1:
                messages = user_output_messages.filter(sender__last_name__icontains=query[0])
            total = messages.count()    
    else:
        form = SearchForm()       
         
    return render(request,
                'users/profile_search_input_messages.html',
                {'form': form,
                'messages': messages,
                'total': total,
                }) 

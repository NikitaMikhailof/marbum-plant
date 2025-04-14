from django import forms
from .models import Journal, Comments, Messages


class SearchForm(forms.Form):
    query = forms.CharField()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'id': 'search',
                'name': 'search',
                'type': 'text',
                'placeholder': 'введите запрос'
        })
            

class JournalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'id': f'{field}',
                'name': f'{field}',
        })
            
    class Meta:
        model = Journal
        fields = ['user', 'equipment', 'body']    


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'id': f'{field}',
                'name': f'{field}',
        })
            
    class Meta:
        model = Comments
        fields = ['user', 'equipment', 'body']    


class SendMessage(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'id': f'{field}',
                'name': f'{field}',
        })
            
    class Meta:
        model = Messages
        fields = ['body', 'owner', 'sender']          
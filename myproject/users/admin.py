from django.contrib import admin
from .models import Category, Messages, Equipment, Comments, Journal, SchemaEquipment
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe 


admin.site.site_header = 'Панель администрирования'


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('third_name', 'job', 'department', 'telephone', 'photo')}),
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    fields = ['title', 'slug']
    prepopulated_fields = {"slug": ("title", )}
    search_fields = ['title', 'slug']


class MessagesAdmin(admin.ModelAdmin):
    list_display = ['body', 'owner', 'sender', 'time_create']
    search_fields = ['body']


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'place', 'cat', 'characteristic', 'slug', 'get_html_photo']
    prepopulated_fields = {"slug": ("title", )}
    search_fields = ['title', 'slug']

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")
        else:
            return "Нет фото"
        
    get_html_photo.short_description = "Фото"


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'body', 'equipment', 'time_create']
    search_fields = ['user', 'equipment']


class JournalAdmin(admin.ModelAdmin):
    list_display = ['equipment', 'body', 'user', 'time_create']
    search_fields = ['user', 'equipment']


class SchemaEquipmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'time_create', 'get_html_photo']
    search_fields = ['title']

    def get_html_photo(self, object):
        if object.schema_image:
            return mark_safe(f"<img src='{object.schema_image.url}' width=50>")
        else:
            return "Нет фото"
        
    get_html_photo.short_description = "Фото"



admin.site.register(get_user_model(), MyUserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Messages, MessagesAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Journal, JournalAdmin)
admin.site.register(SchemaEquipment, SchemaEquipmentAdmin)
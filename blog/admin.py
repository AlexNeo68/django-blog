from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['id', 'title', 'slug']

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['id', 'title', 'slug']


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='Содержимое')
    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']
    list_filter = ['category', 'tags']
    
    list_display = ['id', 'title', 'slug', 'category', 'created_at', 'get_photo']

    list_display_links = ['id', 'title']

    fields = ['title', 'content', 'slug', 'photo', 'get_photo','category', 'views', 'created_at', 'tags']
    readonly_fields = ['created_at', 'views', 'get_photo']
    
    save_on_top=True
    save_as=True
    actions_on_top=True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75" />')
        else:
            return 'фото не установлено'
        
    get_photo.short_description = 'Миниатюра'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
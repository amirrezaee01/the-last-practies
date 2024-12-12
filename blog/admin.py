from django.contrib import admin
from blog.models import *


class PostaAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ['title' ,'author','counted_views','login_require','status','published_date','created_date']
    list_filter = ['status','author']
    search_fields = ['title','content']
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ['name' ,'post','approved','created_date']
    list_filter = ['post','approved']
    search_fields = ['title','content']
    
admin.site.register(Post,PostaAdmin)
admin.site.register(Category)
admin.site.register(Comment,CommentAdmin)



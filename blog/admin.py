from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'post', 'created_date', 'approved_comment')
    list_filter = ('approved_comment', 'created_date')
    search_fields = ('author', 'text')
    actions = ['approve_comment']

    def approve_comments(self, request, queryset):
        queryset.update(approved_comment=True)

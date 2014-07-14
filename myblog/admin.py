from django.contrib import admin
from myblog.models import Post
'''
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
'''

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'recently_published')
    list_filter = ['pub_date']
    search_fields = ['title']
  #  inlines = [CommentInline]

admin.site.register(Post, BlogAdmin)
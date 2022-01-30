from django.contrib import admin

from .models import Post, Author

from .forms import *

admin.site.register(Author)

admin.site.site_header = 'Farm Kenya'

class BlogAdmin(admin.ModelAdmin):

    form = PostAdminForm

class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'author', 'publish', 'status')

    list_filter = ('status', 'created', 'publish', 'author')

    prepopulated_fields = { 'slug' : ('title',)}

    raw_id_field = ('author',)

    search_fields = ('title', 'body')

    ordering = ('status', 'publish')

    date_hierarchy = 'publish'

admin.site.register(Post, BlogAdmin)
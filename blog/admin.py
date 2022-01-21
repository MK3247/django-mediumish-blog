from django.contrib import admin

from .models import Post, Author, Categories

admin.site.register(Author)

admin.site.register(Categories)

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'author', 'publish', 'status')

    list_filter = ('status', 'created', 'publish', 'author')

    prepopulated_fields = { 'slug' : ('title',)}

    raw_id_field = ('author',)

    search_fields = ('title', 'body')

    ordering = ('status', 'publish')

    date_hierarchy = 'publish'
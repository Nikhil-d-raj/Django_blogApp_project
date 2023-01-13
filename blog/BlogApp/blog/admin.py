from django.contrib import admin

from .models import Post, Category, Comment, Movie
#this below class is for adding the comments in posts admin dashboard
class CommentItemInline(admin.TabularInline):
    model = Comment
    row_id_fields = ['post']

class  PostAdmin(admin.ModelAdmin):
    search_fields = ['title','intro','body']
    list_display = ['title','slug','category','published_at']
    list_filter = ['category','published_at']
    inlines = [CommentItemInline]
    prepopulated_fields = {'slug':('title',)}
#for searching an item in the admin panel
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug':('title',)}
    

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','post','created_at']
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Movie)
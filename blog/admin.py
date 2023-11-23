from django.contrib import admin
from .models import PostModel
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'summary','context','status','created_at']
    list_filter = ['created_at']
    search_fields = ['title']

admin.site.register(PostModel, PostAdmin)

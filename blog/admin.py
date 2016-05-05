from django.contrib import admin
from .models import Blog, Category

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
	exclude = ['posted']
	pre_populated_fields = {'slug':('title',)}
	
class CategoryAdmin(admin.ModelAdmin):
	pre_populated_fields = {'slug': ('title',)}
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(PostImage)

admin.site.register(Category)

admin.site.register(Tag)

class PostImageInline(admin.StackedInline):
	model = PostImage


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	
	inlines = [PostImageInline]
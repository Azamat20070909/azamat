from django.contrib import admin
from .models import News, Comment, Category
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(News, NewsAdmin)
admin.site.register(Comment)
admin.site.register(Category)
# Register your models here.

from django.urls import path
from .views import create_news, edit, delete, detail

urlpatterns = [

		path('crete/', create_news, name='create'),
		path('edit/<int:id>', edit	, name = 'edit'),
		path('delete/<int:id>', delete, name = 'delete'),
		path('detail/<int:id>', detail, name = 'detail'),



]
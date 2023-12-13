from django import forms
from .models import News, Comment


class NewsForm(forms.ModelForm):
	class Meta:
		model = News
		fields = ['title', 'content', 'author', 'category']


class CommentForm(forms.ModelForm):
	comment = forms.CharField(max_length = 200)
	class Meta:
		model = Comment
		fields = ['comment']
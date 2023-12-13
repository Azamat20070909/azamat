from django.shortcuts import render, redirect
from .forms import NewsForm, CommentForm
from .models import News, Comment
from user.models import User
from django.views import View


def create_news(request):
	form = NewsForm()
	if request.method == 'POST':
		form = NewsForm(data = request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
		return render(request, 'create.html', {'form':form})
	return render(request, 'create.html', {'form':form})


def edit(request, id):
	news = News.objects.get(id=id)
	form = NewsForm(instance = news)
	if request.method == 'POST':
		form = NewsForm(intance=news, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
		return render(request, 'create.html', {'form':form})
	return render(request, 'create.html', {'form':form})


def delete(request, id):
	news = News.objects.get(id=id)
	news.delete()
	return redirect('home')




def detail(request, id):
	news = News.objects.get(id = id)
	form = CommentForm(data = request.POST)
	if request.method == 'POST':
		form = CommentForm(data = request.POST)
		if form.is_valid():
			comment = form.cleaned_data['comment']
			Comment.objects.create(
				comment = comment,
				news = news,
				user = request.user
			)
			return redirect('home')
	return render(request, 'detail.html', {'news':news, 'form':form})



def Create_Comment(request, id):
	if request.method == 'POST':
		form = CommentForm(data = request.POST)
		if form.is_valid():
			form.save()
			return redirect('detail', id)
# Create your views here.
	
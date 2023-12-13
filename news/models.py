from django.db import models
from user.models import User
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class News(models.Model):
	title = models.CharField(max_length=100, verbose_name='Xabar Sarlavhasi')
	content = models.TextField(verbose_name='Xabar matni')
	category = models.ForeignKey(Category, on_delete = models.CASCADE, null=True, blank=True)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)	
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'user_news')
	photo = models.ImageField(upload_to = 'news_images/', null=True, blank=True)
	slug = models.SlugField(blank = True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super().save(*args, **kwargs)

	def __str__(self):
		return f'{self.author},{self.title[:20]}'

	@property
	def sum_of_likes(self):
		return self.likes.user.count()

	@property
	def sum_of_dislikes(self):
		return self.dislikes.user.count()
	

class Comment(models.Model):
	comment = models.TextField(verbose_name = 'Izoh')
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'user_comments')
	news = models.ForeignKey(News, on_delete=models.CASCADE, related_name = 'news_comments')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.comment


class Like(models.Model):
	news = models.OneToOneField(News, on_delete = models.CASCADE, related_name = 'likes')
	user = models.ManyToManyField(User)


class Dislike(models.Model):
	news = models.OneToOneField(News, on_delete = models.CASCADE, related_name = 'dislikes')
	user = models.ManyToManyField(User)
from django.db import models

from ..accounts.models import Account
from ..classrooms.models import Classroom


class Moment(models.Model):
	# Basic
	content = models.CharField(max_length=200)
	images = models.TextField(default='[]')
	flagged = models.IntegerField(default=False)

	creator = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='moments', null=True, blank=True)
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='moments', null=True, blank=True)

	# Timestamp
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	# Relatives
	# 1) comments


class Post(models.Model):
	# Basic
	content = models.TextField()
	# Relations
	creator = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
	# Timestamp
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	# Relatives
	# 1) comments


class Comment(models.Model):
	# Basic
	content = models.CharField(max_length=200)
	image = models.URLField(blank=True, null=True)
	# relations
	creator = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
	moment = models.ForeignKey(Moment, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
	# how related_name work:
	# http://stackoverflow.com/questions/2642613/what-is-related-name-used-for-in-django
	# note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
	# Timestamp
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


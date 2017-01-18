from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from django.template.defaultfilters import slugify


from ..accounts.models import Account
from ..classrooms.models import Classroom


class Room(models.Model):
	name = models.CharField(max_length=20)
	label = models.SlugField(blank=True, null=True)
	# relationship
	accounts = models.ManyToManyField(Account, related_name='rooms')
	creator = models.ForeignKey(Account)
	classroom = models.ForeignKey(Classroom, related_name='class_chatroom')

	class Meta:
		ordering = ("name",)

	def __unicode__(self):
		return self.name

	@models.permalink
	def get_absolute_url(self):
		return ("room", (self.slug,))

	def save(self, *args, **kwargs):
		if not self.label:
			self.label = slugify(self.name)
		super(Room, self).save(*args, **kwargs)


class Message(models.Model):
	room = models.ForeignKey(Room, related_name='messages')
	context = models.CharField(max_length=140, blank=True)
	handle = models.CharField(max_length=140)
	message = models.CharField(max_length=140)
	created = models.DateTimeField(default=timezone.now, db_index=True)

	def __unicode__(self):
		return '[{timestamp}] {handle}: {message}'.format(**self.as_dict())

	@property
	def formatted_timestamp(self):
		return self.created.strftime('%b %-d %-I:%M %p')

	def as_dict(self):
		return {'handle': self.handle, 'message': self.message, 'timestamp': self.formatted_timestamp}

	class Meta:
		get_latest_by = 'timestamp'


class ChatUser(models.Model):
	name = models.ForeignKey(Account, max_length=20, related_name="name")
	session = models.CharField(max_length=20)
	room = models.ForeignKey(Room, related_name="users")

	class Meta:
		ordering = ("name",)

	def __unicode__(self):
		return self.name

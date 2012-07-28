from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.db import models

# Initially modeled after okfn's elastic search implementation 
# github.com/okfn/annotator-store
class Annotation(models.Model):
	# Base fields
	created 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)
	quote		= models.TextField(help_text="The text being annotated (not the comment itself)")
	uri			= models.URLField()
	user		= models.ForeignKey(User,'annotations')
	text		= models.CharField()
	consumer	= models.CharField()
	# Tagging not supported yet
	# tags		= generic.GenericRelation(ct_field='content_type', fk_field='object_pk')
	# Support for threading
	parent		= models.ForeignKey('self',blank=True,related_name='children')
	# Support for app-specific data
	extension	= generic.GenericForeignKey(ct_field='content_type', fk_field='object_pk',blank=True)

class Range(models.Model):
	# Base fields
	annotation	= models.ForeignKey('Annotation',related_name='ranges')
	start		= models.CharField()
	end			= models.CharField()
	startOffset	= models.PositiveIntegerField()
	endOffset	= models.PositiveIntegerField()

class Permission(models.Model):
	# Base fields
	annotation	= models.ForeignKey('Annotation',related_name='permissions')
	read		= models.ManyToManyField('User')
	update		= models.ManyToManyField('User')
	delete		= models.ManyToManyField('User')
	admin		= models.ManyToManyField('User')

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
	user		= models.ForeignKey(User,related_name='annotations')
	text		= models.CharField(max_length=255)
	consumer	= models.CharField(max_length=255)
	# Tagging not supported yet
	# tags		= generic.GenericRelation(ct_field='content_type', fk_field='object_pk')
	# Support for threading
	parent		= models.ForeignKey('self',blank=True,related_name='children')
	# Support for app-specific data
	extension	= generic.GenericForeignKey(ct_field='content_type', fk_field='object_pk')

class Range(models.Model):
	# Base fields
	annotation	= models.ForeignKey('Annotation',related_name='ranges')
	start		= models.CharField(max_length=255)
	end			= models.CharField(max_length=255)
	startOffset	= models.PositiveIntegerField()
	endOffset	= models.PositiveIntegerField()

class Permission(models.Model):
	# Base fields
	annotation	= models.ForeignKey('Annotation',related_name='permissions')
	read		= models.ManyToManyField(User,related_name='annotation_read_permissions')
	update		= models.ManyToManyField(User,related_name='annotation_update_permissions')
	delete		= models.ManyToManyField(User,related_name='annotation_delete_permissions')
	admin		= models.ManyToManyField(User,related_name='annotation_admin_permissions')

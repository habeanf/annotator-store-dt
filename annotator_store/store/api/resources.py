from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization
from store.models import Annotation,Range,Permission

class AnnotationResource(ModelResource):
#	permissions	= fields.ToManyField('store.api.resources.PermissionResource','permissions')
	ranges		= fields.ToManyField('store.api.resources.RangeResource','ranges')
	class Meta:
		queryset	= Annotation.objects.all()
		resource_name	= 'annotation'
		allowed_methods	= ['get', 'post', 'put', 'delete']
		authorization	= Authorization()

	def hydrate_user(self,bundle):
		return null

	def dehydrate_user(self,bundle):
 		return 'habeanf'

	def hydrate(self,bundle):
		return bundle

class RangeResource(ModelResource):
	annotation			= fields.ToOneField(AnnotationResource,'annotation')	
	class Meta:
		queryset		= Range.objects.all()
        resource_name	= 'range'

class PermissionResource(ModelResource):
	annotation			= fields.ToOneField(AnnotationResource,'annotation')	
	class Meta:
		queryset		= Permission.objects.all()
		resource_name	= 'permission'


from tastypie.resources import ModelResource
from store.models import Annotation


class AnnotationResource(ModelResource):
    class Meta:
        queryset 		= Annotation.objects.all()
        resource_name	= 'annotation'
        allowed_methods	= ['get', 'post', 'put', 'delete']
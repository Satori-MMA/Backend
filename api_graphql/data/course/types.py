from graphene_django import DjangoObjectType
from courses.models import Course
from graphene import relay


class CourseNode(DjangoObjectType):
    class Meta:
        model = Course
        fields = '__all__'
        filter_fields = {
            'coTitle': ['exact', 'icontains', 'istartswith'],
            'coPrice': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node,)
from graphene_django import DjangoObjectType
from lessons.models import Lesson
from graphene import relay


class LessonNode(DjangoObjectType):
    class Meta:
        model = Lesson
        fields = '__all__'
        filter_fields = {
            'leName': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node,)
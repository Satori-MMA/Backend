from graphene_django import DjangoObjectType
from lessons.models import lessonUser
from graphene import relay


class LessonUserNode(DjangoObjectType):
    class Meta:
        model = lessonUser
        fields = '__all__'
        filter_fields = {
            'user_id': ['exact'],
            'lesson_id': ['exact']
        }
        interfaces = (relay.Node,)
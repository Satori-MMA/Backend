from graphene_django import DjangoObjectType
from reviews.models import Review
from graphene import relay


class ReviewNode(DjangoObjectType):
    class Meta:
        model = Review
        fields = '__all__'
        filter_fields = {
            'opQualification': ['exact', 'icontains', 'istartswith'],
            'lesson_id': ['exact']
        }
        interfaces = (relay.Node,)
from graphene_django import DjangoObjectType
from categories.models import Category
from graphene import relay


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        fields = '__all__'
        filter_fields = {
            'catName': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node,)
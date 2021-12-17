from graphene_django import DjangoObjectType
from roles.models import Role
from graphene import relay


class RoleNode(DjangoObjectType):
    class Meta:
        model = Role
        fields = '__all__'
        filter_fields = {
            'rol_name': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node,)
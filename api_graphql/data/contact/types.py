from graphene_django import DjangoObjectType
from contacts.models import ContactSatori
from graphene import relay


class ContactNode(DjangoObjectType):
    class Meta:
        model = ContactSatori
        fields = '__all__'
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'email': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node,)
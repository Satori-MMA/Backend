from graphene_django import DjangoObjectType
from courses.models import Payment
from graphene import relay


class PaymentNode(DjangoObjectType):
    class Meta:
        model = Payment
        fields = '__all__'
        filter_fields = {
            'paDate': ['exact', 'icontains', 'istartswith'],
            'user_id': ['exact'],
            'course_id': ['exact']
        }
        interfaces = (relay.Node,)
from graphene_django import DjangoObjectType
from monthly_payments.models import MonthlyPayment
from graphene import relay


class MonthlyPaymentNode(DjangoObjectType):
    class Meta:
        model = MonthlyPayment
        fields = '__all__'
        filter_fields = {
            'moStartDate': ['exact'],
            'moFinishDate': ['exact'],
            'moType': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node,)
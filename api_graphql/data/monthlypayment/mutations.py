from graphene import Field, Mutation
from api_graphql.data.monthlypayment.inputs import CreateMonthlyPaymentInput,UpdateMonthlyPaymentInput

from monthly_payments.models import MonthlyPayment
from .types import MonthlyPaymentNode
from api_graphql.utils import delete_attributes_none
from api_graphql.utils import transform_global_ids

class CreateMonthlyPayment(Mutation):
    monthlyPayment = Field(MonthlyPaymentNode)

    class Arguments:
        input = CreateMonthlyPaymentInput(required=True)
        
    #@login_required
    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        monthlyPayment = MonthlyPayment.objects.create(**input)
        return CreateMonthlyPayment(monthlyPayment=monthlyPayment)

class UpdateMonthlyPayment(Mutation):
    """Clase para actualizar """
    monthlyPayment = Field(MonthlyPaymentNode)

    class Arguments:
        input = UpdateMonthlyPaymentInput(required=True)
        
    #@login_required
    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        MonthlyPayment.objects.filter(pk=input.get("id")).update(**input)
        monthlyPayment = MonthlyPayment.objects.get(pk=input.get('id'))
        # Notice we return an instance of this mutation
        return UpdateMonthlyPayment(monthlyPayment=monthlyPayment)


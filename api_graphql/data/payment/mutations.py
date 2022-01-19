from graphene import Field, Mutation
from api_graphql.data.payment.inputs import CreatePaymentInput,UpdatePaymentInput

from courses.models import Payment
from .types import PaymentNode
from api_graphql.utils import delete_attributes_none
from api_graphql.utils import transform_global_ids

class CreatePayment(Mutation):
    """Clase para Crear """
    payment = Field(PaymentNode)

    class Arguments:
        input = CreatePaymentInput(required=True)
        
    #@login_required
    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        payment = Payment.objects.create(**input)
        return CreatePayment(payment=payment)

class UpdatePayment(Mutation):
    """Clase para actualizar """
    payment = Field(PaymentNode)

    class Arguments:
        input = UpdatePaymentInput(required=True)
        
    #@login_required
    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        Payment.objects.filter(pk=input.get("id")).update(**input)
        payment = Payment.objects.get(pk=input.get('id'))
        # Notice we return an instance of this mutation
        return UpdatePayment(payment=payment)


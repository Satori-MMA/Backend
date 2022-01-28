from graphene import Field, Mutation
from api_graphql.data.contact.inputs import CreateContactInput

from contacts.models import ContactSatori
from .types import ContactNode
from api_graphql.utils import delete_attributes_none
from api_graphql.utils import transform_global_ids
from contacts.views import send_email

class CreateContact(Mutation):
    """Clase para Crear contacto"""
    contact = Field(ContactNode)

    class Arguments:
        input = CreateContactInput(required=True)
        
    #@login_required
    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        contact = ContactSatori.objects.create(**input)
        send_email(contact)
        return CreateContact(contact=contact)


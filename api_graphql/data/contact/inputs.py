from graphene import InputObjectType
from graphene.types.scalars import String
# Create your inputs types here.



class CreateContactInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios para la
    creacion de contacto
    """
    name = String(Required = True)
    phone = String(Required = True)
    email = String(Required = True)
    comment = String(Required = True)

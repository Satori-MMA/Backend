from graphene import InputObjectType
from graphene.types.scalars import ID
from graphene import Date
# Create your inputs types here.

class CreatePaymentInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios para la creacion de un pago de un curso por parte del usuario
    """
    paDate = Date(Required = True)

    #Relaciones
    user_id = ID(Required = True)
    course_id = ID(Required = True)

class UpdatePaymentInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para actualizar un rol
    """
    id = ID(requiered=True)
    paDate = Date()

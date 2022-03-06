from graphene import InputObjectType
from graphene.types.scalars import ID
from graphene import Date
from graphene.types.scalars import String
# Create your inputs types here.


class CreateMonthlyPaymentInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios para la
    creacion de una mensualidad
    """
    moStartDate = Date(Required = True)
    moFinishDate = Date(Required = True)
    moType = String(Required = True)

    #Relaciones
    payment_id = ID(Required = True)

class UpdateMonthlyPaymentInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para actualizar una mensualidad
    """
    id = ID(requiered=True)
    moStartDate = Date()
    moFinishDate = Date()
    moType = String

    #Relaciones
    payment_id = ID(Required = True)
from graphene import InputObjectType
from graphene.types.scalars import ID
from graphene import Date
from graphene.types.scalars import String, Float, Boolean
# Create your inputs types here.


class CreateLessonUserInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios para la
    creacion de una mensualidad
    """
    taCheck = Boolean(Required = True)

    #Relaciones
    user_id = ID(Required = True)
    lesson_id = ID(Required = True)

class UpdateLessonUserInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para actualizar una mensualidad
    """
    id = ID(requiered=True)
    taCheck = Boolean()

    #Relaciones
    user_id = ID()
    lesson_id = ID()
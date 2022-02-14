from decimal import Decimal
from graphene import InputObjectType
from graphene.types.scalars import ID
from graphene import String, Float, Boolean
# Create your inputs types here.

class CreateLessonInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios para la creacion de una lession por parte del usuario
    """
    leName = String(Required = True)
    leDescription =String(Required = True)
    leEvaluation = Float(Required = True)
    leLinkVideo = String(Required = True)

    #Relaciones
    course_id = ID(Required = True)

class UpdateLessonInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para actualizar un rol
    """
    id = ID(requiered=True)
    leName = String()
    leDescription =String()
    leEvaluation = Float()
    leLinkVideo = String()
    is_active = Boolean()

    #Relación
    course_id = ID()

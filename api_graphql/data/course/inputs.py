from graphene import InputObjectType
from graphene.types.scalars import ID
from graphene.types.scalars import String, Float, Boolean
# Create your inputs types here.



class CreateCourseInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios para la
    creacion de un curso
    """
    coTitle = String(Required = True)
    coDescription = String(Required = True)
    coImage = String(Required = True)
    coPrice = Float(Required = True)

    #Relaciones
    category_id = ID(Required = True)

class UpdateCourseInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para actualizar un rol
    """
    id = ID(requiered=True)
    coTitle = String()
    coDescription = String()
    coImage = String()
    coPrice = String()
    is_active = Boolean()

    #Relaciones
    category_id = ID()

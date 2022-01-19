from graphene import InputObjectType
from graphene.types.scalars import ID
from graphene.types.scalars import String, Int
# Create your inputs types here.



class CreateCourseInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios para la
    creacion de un curso
    """
    coTitle = String(Required = True)
    coDescription = String(Required = True)
    coImage = String(Required = True)
    coPrice = Int(Required = True)

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

from graphene import InputObjectType
from graphene.types.scalars import ID
from graphene.types.scalars import String, Int
# Create your inputs types here.


class CreateCategoryInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios para la
    creacion de una categoria
    """
    catName = String(Required = True)

class UpdateCategoryInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para actualizar un rol
    """
    id = ID(requiered=True)
    catName = String()
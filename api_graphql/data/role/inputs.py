from graphene import InputObjectType
from graphene.types.scalars import ID
from graphene.types.scalars import String
# Create your inputs types here.



class CreateRoleInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios para la
    creacion de un rol
    """
    rol_name = String(Required=True)
    #Relaciones
    user_id = ID(Required=True)

class UpdateRoleInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para actualizar un rol
    """
    id = ID(requiered=True)
    rol_name = String()

    #Relacion
    user_id = ID()

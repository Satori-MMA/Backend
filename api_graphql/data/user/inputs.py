from graphene import InputObjectType
from graphene.types.scalars import ID
from graphene.types.scalars import String, Boolean
# Create your inputs types here.


class UpdateUsersInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para actualizar
    """
    id = ID(requiered=True)
    first_name = String(required=True)
    last_name = String(required=True)
    email = String(required=True)
    password = String(required=True)
    is_superuser = Boolean(required=False)
    is_staff = Boolean(required=False)
    is_active = Boolean(required=False)
    
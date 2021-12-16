from graphene import Field, Mutation
from api_graphql.data.role.inputs import UpdateRoleInput

from roles.models import Role
from .types import RoleNode
from api_graphql.utils import delete_attributes_none
from api_graphql.utils import transform_global_ids

class UpdateRole(Mutation):
    """Clase para actualizar """
    role = Field(RoleNode)

    class Arguments:
        input = UpdateRoleInput(required=True)
        
    #@login_required
    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        Role.objects.filter(pk=input.get("id")).update(**input)
        role = Role.objects.get(pk=input.get('id'))
        # Notice we return an instance of this mutation
        return UpdateRole(role=role)

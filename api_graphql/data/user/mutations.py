from graphene import Field, Mutation
from .types import UsersNode
from users.models import ExtendUser
from api_graphql.data.user.inputs import UpdateUsersInput
from api_graphql.utils import delete_attributes_none
from api_graphql.utils import transform_global_ids
from graphql_jwt.decorators import login_required

class UpdateUsers(Mutation):
    """Clase para crear """
    user = Field(UsersNode)

    class Arguments:
        input = UpdateUsersInput(required=True)
        
    @login_required
    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        ExtendUser.objects.filter(pk=input.get("id")).update(**input)
        user = ExtendUser.objects.get(pk=input.get('id'))
        user.set_password(user.password)
        user.save()
        # Notice we return an instance of this mutation
        return UpdateUsers(user=user)

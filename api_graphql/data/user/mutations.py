from graphene import Field, Mutation
from .types import UsersNode
from users.models import UserStori
from api_graphql.data.user.inputs import UpdateUsersInput
from api_graphql.utils import delete_attributes_none
from api_graphql.utils import transform_global_ids
from graphql_jwt.decorators import login_required
from graphql_auth import mutations

class UpdateUsers(Mutation):
    """Clase para crear """
    user = Field(UsersNode)

    class Arguments:
        input = UpdateUsersInput(required=True)
        
    @login_required
    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        UserStori.objects.filter(pk=input.get("id")).update(**input)
        user = UserStori.objects.get(pk=input.get('id'))
        user.set_password(user.password)
        user.save()
        # Notice we return an instance of this mutation
        return UpdateUsers(user=user)
class RegisterCustom(mutations.Register):
    user = Field(UsersNode)

    @classmethod
    def mutate(self, *args, **kwargs):
        try: 
            res = super().mutate(*args, **kwargs)
            email = kwargs.get("email")
            user = UserStori.objects.filter(email=email).first()
            return RegisterCustom(
                success=res.success,
                errors=res.errors,
                user=user,
            )
        except Exception:
            raise Exception(res.errors)
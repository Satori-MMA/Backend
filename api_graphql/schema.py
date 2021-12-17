from graphene.relay.node import Node
from graphql_auth import mutations

from .data.user.types import UsersNode
from graphene import relay, ObjectType, Schema, Field
from graphene_django.filter import DjangoFilterConnectionField
from .data.user.mutations import RegisterCustom, UpdateUsers
import graphql_jwt
from graphql_jwt.decorators import login_required
from users.models import UserStori
from graphql_auth.schema import UserQuery, MeQuery

#Roles
from .data.role.types import RoleNode
from .data.role.mutations import CreateRole, UpdateRole

class Query(UserQuery, MeQuery,ObjectType):
    #Consulas a la app Users
    allUsers = DjangoFilterConnectionField(UsersNode)
    #nodo
    user = relay.Node.Field(UsersNode)
    @login_required
    def resolve_allUsers(self, info, **kwargs):
        return UserStori.objects.all()
        #return Users.objects.filter(kwargs)
    
    #Roles
    role = relay.Node.Field(RoleNode)
    all_Roles = DjangoFilterConnectionField(RoleNode)
class AuthMutation(ObjectType):
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset = mutations.SendPasswordResetEmail.Field()

    verify_token = mutations.VerifyToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    revoke_token = mutations.RevokeToken.Field()

    #Cuando se olvido de la contraseña
    password_reset = mutations.PasswordReset.Field()
    #Cuando sabe la contraseña antigua
    password_change = mutations.PasswordChange.Field()
    archive_account = mutations.ArchiveAccount.Field()
    delete_account = mutations.DeleteAccount.Field()

class Mutation(AuthMutation,ObjectType):
    role_update = UpdateRole.Field()
    role_create = CreateRole.Field()
    user_register = RegisterCustom.Field()
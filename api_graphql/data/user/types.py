from graphene_django import DjangoObjectType
from users.models import UserStori
from graphene import relay


class UsersNode(DjangoObjectType):
    class Meta:
        model = UserStori
        fields = '__all__'
        #filter_fields = ['name','is_active',]
        filter_fields = {
            'email' : ['exact', 'icontains','istartswith']
            #Rangofechas
            #categor__name
            #gt > | gte >= | lt < | lte <=
            #'create_at' : ['gt','gte','lt','lte']
        }
        #Excluir 
        #exclude = ['post_set']
        interfaces = (relay.Node,)
"""
class Query(ObjectType):
    #Consulas a la app Users
    allUsers = DjangoFilterConnectionField(UsersNode)
    #nodo
    user = relay.Node.Field(UsersNode)
"""
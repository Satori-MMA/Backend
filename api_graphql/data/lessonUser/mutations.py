from graphene import Field, Mutation
from api_graphql.data.lessonUser.inputs import CreateLessonUserInput,UpdateLessonUserInput

from lessons.models import lessonUser
from .types import LessonUserNode
from api_graphql.utils import delete_attributes_none
from api_graphql.utils import transform_global_ids

class CreateLessonUser(Mutation):
    lessonsUser = Field(LessonUserNode)

    class Arguments:
        input = CreateLessonUserInput(required=True)
        
    #@login_required
    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        lessonsUser = lessonUser.objects.create(**input)
        return CreateLessonUser(lessonsUser=lessonsUser)

class UpdateLessonUser(Mutation):
    """Clase para actualizar """
    lessonsUser = Field(LessonUserNode)

    class Arguments:
        input = UpdateLessonUserInput(required=True)
        
    #@login_required
    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        lessonUser.objects.filter(pk=input.get("id")).update(**input)
        lessonsUser = lessonUser.objects.get(pk=input.get('id'))
        # Notice we return an instance of this mutation
        return UpdateLessonUser(lessonsUser=lessonsUser)


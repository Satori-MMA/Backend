from graphene import Field, Mutation
from api_graphql.data.lesson.inputs import CreateLessonInput, UpdateLessonInput

from lessons.models import Lesson
from .types import LessonNode
from api_graphql.utils import delete_attributes_none
from api_graphql.utils import transform_global_ids

class CreateLesson(Mutation):
    """Clase para Crear """
    lesson = Field(LessonNode)

    class Arguments:
        input = CreateLessonInput(required=True)
        
    #@login_required
    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        lesson = Lesson.objects.create(**input)
        return CreateLesson(lesson=lesson)

class UpdateLesson(Mutation):
    """Clase para actualizar """
    lesson = Field(LessonNode)

    class Arguments:
        input = UpdateLessonInput(required=True)
        
    #@login_required
    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        Lesson.objects.filter(pk=input.get("id")).update(**input)
        lesson = Lesson.objects.get(pk=input.get('id'))
        # Notice we return an instance of this mutation
        return UpdateLesson(lesson=lesson)

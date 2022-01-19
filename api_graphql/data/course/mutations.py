from graphene import Field, Mutation
from api_graphql.data.course.inputs import CreateCourseInput,UpdateCourseInput

from courses.models import Course
from .types import CourseNode
from api_graphql.utils import delete_attributes_none
from api_graphql.utils import transform_global_ids

class CreateCourse(Mutation):
    """Clase para Crear """
    course = Field(CourseNode)

    class Arguments:
        input = CreateCourseInput(required=True)
        
    #@login_required
    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        course = Course.objects.create(**input)
        return CreateCourse(course=course)

class UpdateCourse(Mutation):
    """Clase para actualizar """
    course = Field(CourseNode)

    class Arguments:
        input = UpdateCourseInput(required=True)
        
    #@login_required
    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        Course.objects.filter(pk=input.get("id")).update(**input)
        course = Course.objects.get(pk=input.get('id'))
        # Notice we return an instance of this mutation
        return UpdateCourse(course=course)


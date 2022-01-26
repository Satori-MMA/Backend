from graphene import Field, Mutation
from api_graphql.data.category.inputs import CreateCategoryInput,UpdateCategoryInput

from categories.models import Category
from .types import CategoryNode
from api_graphql.utils import delete_attributes_none
from api_graphql.utils import transform_global_ids

class CreateCategory(Mutation):
    category = Field(CategoryNode)

    class Arguments:
        input = CreateCategoryInput(required=True)
        
    #@login_required
    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        category = Category.objects.create(**input)
        return CreateCategory(category=category)

class UpdateCategory(Mutation):
    """Clase para actualizar """
    category = Field(CategoryNode)

    class Arguments:
        input = UpdateCategoryInput(required=True)
        
    #@login_required
    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        Category.objects.filter(pk=input.get("id")).update(**input)
        category = Category.objects.get(pk=input.get('id'))
        # Notice we return an instance of this mutation
        return UpdateCategory(category=category)


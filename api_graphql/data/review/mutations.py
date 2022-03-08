from ast import If
from graphene import Field, Mutation
from api_graphql.data.review.inputs import CreateReviewInput,UpdateReviewInput

from reviews.models import Review
from roles.models import Role
from .types import ReviewNode
from api_graphql.utils import delete_attributes_none
from api_graphql.utils import transform_global_ids

class CreateReview(Mutation):
    """Clase para actualizar """
    review = Field(ReviewNode)

    class Arguments:
        input = CreateReviewInput(required=True)
        
    #@login_required
    def mutate(self, info, input):
        try:
            input = delete_attributes_none(**vars(input))
            input = transform_global_ids(**input)
            user = Role.objects.get(user_id=input.get('user_id'))
            if(user.rol_name == 'STUDENT'):
                review = Review.objects.create(**input)
                return CreateReview(review=review)
        except:
            return CreateReview(review=review)

class UpdateReview(Mutation):
    """Clase para actualizar """
    review = Field(ReviewNode)

    class Arguments:
        input = UpdateReviewInput(required=True)
        
    #@login_required
    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        Review.objects.filter(pk=input.get("id")).update(**input)
        review = Review.objects.get(pk=input.get('id'))
        # Notice we return an instance of this mutation
        return UpdateReview(review=review)


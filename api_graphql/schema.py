from graphene.relay.node import Node
from graphql_auth import mutations

from .data.user.types import UsersNode
from graphene import relay, ObjectType, Schema, Field
from graphene_django.filter import DjangoFilterConnectionField
from .data.user.mutations import RegisterCustom, UpdateUsers
import graphql_jwt
from graphql_jwt.decorators import login_required
from users.models import UserStori
from graphql_auth.schema import (
    UserQuery, 
    MeQuery
)
from .data.role.types import RoleNode
from .data.course.types import CourseNode
from .data.payment.types import PaymentNode
from .data.category.types import CategoryNode
from .data.lesson.types import LessonNode
from .data.monthlypayment.types import MonthlyPaymentNode
from .data.review.types import ReviewNode

from .data.role.mutations import (
    CreateRole, 
    UpdateRole
)

from .data.course.mutations import(
    CreateCourse,
    UpdateCourse
)

from .data.payment.mutations  import(
    CreatePayment,
    UpdatePayment
)

from .data.category.mutations import(
    CreateCategory,
    UpdateCategory
)

from .data.contact.mutations import(
    CreateContact
)

from .data.lesson.mutations import(
    CreateLesson,
    UpdateLesson
)

from .data.monthlypayment.mutations import(
    CreateMonthlyPayment,
    UpdateMonthlyPayment
)

from .data.review.mutations import(
    CreateReview,
    UpdateReview
)

from .data.lessonUser.mutations import(
    CreateLessonUser,
    UpdateLessonUser
)

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

    #Course
    course = relay.Node.Field(CourseNode)
    all_Courses = DjangoFilterConnectionField(CourseNode)

    #Payment
    payment = relay.Node.Field(PaymentNode)
    all_Payments = DjangoFilterConnectionField(PaymentNode)

    #Category
    category = relay.Node.Field(CategoryNode)
    all_Categories = DjangoFilterConnectionField(CategoryNode)

    #Lesson
    lesson = relay.Node.Field(LessonNode)
    all_lessons = DjangoFilterConnectionField(LessonNode)

    #MonthlyPayment
    monthlypayment = relay.node.Field(MonthlyPaymentNode)
    all_monthlypayments = DjangoFilterConnectionField(MonthlyPaymentNode)

    #Review
    review = relay.node.Field(ReviewNode)
    all_reviews = DjangoFilterConnectionField(ReviewNode)
class AuthMutation(ObjectType):
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
    #Role
    role_update = UpdateRole.Field()
    role_create = CreateRole.Field()
    user_register = RegisterCustom.Field()

    #Course
    course_register = CreateCourse.Field()
    course_update = UpdateCourse.Field()

    #Payment
    payment_register = CreatePayment.Field();
    payment_update = UpdatePayment.Field();

    #Category
    category_register = CreateCategory.Field();
    category_update = UpdateCategory.Field();

    #Contact
    opinion_register = CreateContact.Field();

    #Lesson
    lesson_register = CreateLesson.Field();
    lesson_update = UpdateLesson.Field();

    #MonthlyPayment
    monthlypayment_register = CreateMonthlyPayment.Field();
    monthlypayment_update = UpdateMonthlyPayment.Field();

    #Review
    review_register = CreateReview.Field();
    review_update = UpdateReview.Field();

    #LessonUser
    lessonUser_register = CreateLessonUser.Field()
    lessonUser_update = UpdateLessonUser.Field()
from graphene import InputObjectType
from graphene.types.scalars import ID
from graphene.types.scalars import String
# Create your inputs types here.



class CreateReviewInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios para la
    creacion de una valoracion de una leccion
    """
    opComment = String(Required = True)
    opQualification = String(Required = True)
    
    #Relaciones
    lesson_id = ID(Required=True)

class UpdateReviewInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para actualizar un rol
    """
    id = ID(requiered=True)
    opComment = String()
    opQualification = String()
    
    #Relación
    lesson_id = ID()

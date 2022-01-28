from django.shortcuts import render

# Create your views here.
from django.core.mail import BadHeaderError, EmailMessage

def send_email(self):
    contact = self
    subject = 'Nueva opinión de usuario'
    message =  'Nombre: ' + contact.name+ '\nCorreo: '+ contact.email + '\nTelefono: '+contact.phone+'\nComentario: ' + contact.comment
    email = EmailMessage(
        subject,
        message,
        'noreply@semycolon.com',
        ['roninsatorimma@gmail.com'],
    )
    
    try:
        email.send()
    except BadHeaderError:
        return 'Error'


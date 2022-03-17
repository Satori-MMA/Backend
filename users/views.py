from django.utils.encoding import force_bytes
from django.shortcuts import redirect

from graphql_auth.models import UserStatus

def activate(request,token):
    try:
        UserStatus.verify(token)  
        return redirect('https://satorimma.herokuapp.com/login')
    except Exception:
        raise Exception()

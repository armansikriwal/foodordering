from django.contrib.auth.models import User
from django.http import response
from django.shortcuts import redirect
def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        user=request.user.id
        returnUrl=request.META["PATH_INFO"]
        if user is None  :
            return redirect(f"login?return_url={returnUrl}")
        response=get_response(request)



        return response

    return middleware
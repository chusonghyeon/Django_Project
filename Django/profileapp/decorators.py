from django.contrib.auth.models import User

from profileapp.models import Profile
from django.http import HttpResponseForbidden


def profile_ownership_required(func):
    def decorated(requset, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs['pk'])
        if not profile.user == requset.user:
            return HttpResponseForbidden()
        return func(requset, *args, **kwargs)    
    return decorated
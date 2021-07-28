from django.http import HttpResponseForbidden


def profile_owership_required(func):
    def decorated(request, *args, **kwargs):
        target_profile = Profile.objects.get(pk=kwargs['pk'])
        if target_profile.user == request.user:
            return func
        else:
            return HttpResponseForbidden()

        return decorated
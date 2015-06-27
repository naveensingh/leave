from profiles.models import PersonalProfile


class PersonalProfileMiddleware(object):
    def process_request(self, request):
        user_profile = None
        if request.user.is_authenticated():
            user_profile, _ = PersonalProfile.objects.get_or_create(
                user=request.user)
        request.user_profile = user_profile

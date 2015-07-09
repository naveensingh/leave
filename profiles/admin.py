from django.contrib import admin
from profiles.models import PersonalProfile


class PersonalProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'can_approve')
    search_fields = ['user__first_name', 'user__last_name']

    fieldsets = (
        ('Personal Details', {
            'fields': ('date_of_birth', 'gender', 'bio',
                       'linkedin_url', 'twitter_url', 'profile_picture', "can_approve")
        }),
    )


admin.site.register(PersonalProfile, PersonalProfileAdmin)
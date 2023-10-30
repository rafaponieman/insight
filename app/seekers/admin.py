from django.contrib import admin

from seekers.models import Seeker, Run, Training


class SeekerAdmin(admin.ModelAdmin):
    pass


class RunAdmin(admin.ModelAdmin):
    pass


class TrainingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Seeker, SeekerAdmin)
admin.site.register(Run, RunAdmin)
admin.site.register(Training, TrainingAdmin)

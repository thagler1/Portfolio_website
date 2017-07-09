from django.contrib import admin
from .models import Profile, Titles, Project, Language, Contact
# Register your models here.


admin.site.register(Profile)
admin.site.register(Titles)
admin.site.register(Project)
admin.site.register(Language)
admin.site.register(Contact)
from django.contrib import admin
from users.models import CustomUser, Word

admin.site.register(CustomUser)
admin.site.register(Word)

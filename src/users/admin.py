from django.contrib import admin
from users.models import CustomUser, Word, Category

admin.site.register(CustomUser)
admin.site.register(Word)
admin.site.register(Category)

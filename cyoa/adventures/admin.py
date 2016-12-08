from django.contrib import admin
from .models import Question, Choice, Adventure

# Register your models here.
# Used django's tutorials heavily

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Adventure)
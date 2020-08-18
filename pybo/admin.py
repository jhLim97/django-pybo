from django.contrib import admin
from .models import Question

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

#장고 화면사이트에 추가
admin.site.register(Question, QuestionAdmin)
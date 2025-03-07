from django.contrib import admin

from apps.models.auth_model import User
from apps.models.inquiry_model import Inquiry
from apps.models.question_model import QuestionCategory, Question, UserAnswer


admin.site.register(User)
admin.site.register(QuestionCategory)
admin.site.register(Question)
admin.site.register(UserAnswer)
admin.site.register(Inquiry)

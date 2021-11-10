from django.contrib import admin
from polls.models import Question, Poll, PollResult, UserAnswer


admin.site.register(Poll)
admin.site.register(Question)
admin.site.register(PollResult)
admin.site.register(UserAnswer)

from django.contrib import admin
from models import Code, Voter, Quiz, Question, Answer, Store

class CodeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Code, CodeAdmin)


class VoterAdmin(admin.ModelAdmin):
    pass
admin.site.register(Voter, VoterAdmin)

class AnswerInline(admin.TabularInline):
    model = Answer
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline
    ]
admin.site.register(Question, QuestionAdmin)


class AnswerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Answer, AnswerAdmin)


class QuestionInline(admin.TabularInline):
    model = Question

class QuizAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline
    ]
admin.site.register(Quiz, QuizAdmin)

class StoreAdmin(admin.ModelAdmin):
    pass
admin.site.register(Store, StoreAdmin)
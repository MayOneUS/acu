from django.db import models

# Create your models here.
class Voter(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __string__(self):
        return self.firstName + " " + self.lastName
    def __unicode__(self):
        return self.firstName + " " + self.lastName


class Quiz(models.Model):
    name = models.CharField(max_length=200)
    video_url = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name

    def validate_answers(self, answers):
        questions = self.question_set.all()
        correct_answers = [(question.id,list(question.answer_set.filter(correct=True)[:1])[0]) for question in questions]

        wrong_answers = [question_id for question_id,answer in correct_answers if answers[str(question_id)] != str(answer.id)]

        print questions, correct_answers
        return wrong_answers


class Store(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name

class Code(models.Model):
    code = models.CharField(max_length=20)
    voter = models.ForeignKey(Voter)
    started_watching = models.DateTimeField(null=True, blank=True)
    finished_watching = models.DateTimeField(null=True, blank=True)
    quiz = models.ForeignKey(Quiz)
    quiz_complete = models.BooleanField(default=False)
    chosen_email = models.EmailField(blank=True, null=True)
    store = models.ForeignKey(Store, blank=True, null=True)

    def __string__(self):
        return self.code

    def __unicode__(self):
        return self.voter.firstName +  ": "  + self.code


class Question(models.Model):
    question = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz)

    def __unicode__(self):
        return self.question

class Answer(models.Model):
    answer = models.CharField(max_length=200)
    question = models.ForeignKey(Question)
    correct = models.BooleanField(default=False)

    def __unicode__(self):
        return self.question.question + ": " + self.answer

class QuizResponse(models.Model):
    code = models.ForeignKey(Code)
    answers = models.ManyToManyField(Answer)
    quiz = models.ForeignKey(Quiz)

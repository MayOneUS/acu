from django.shortcuts import render, render_to_response
from models import Code, Store
from django.views.generic import View
from django.http import HttpResponse
from datetime import datetime
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

import json

def home(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('index.html', c)

def Validate(request):
    if request.method == 'GET':
        print "in validate!"
        token = request.GET.get('token', '')
        if token == '':
            return HttpResponse(status=400)
        try:
            code = Code.objects.get(code=token)
            print "hello!"
            questions = code.quiz.question_set.all()
            QandA = [
                {'question':question.question, 'id':question.id,
                      'answers': [{'text':answer.answer, 'id':answer.id} for answer in question.answer_set.all()]
                }
                for question in questions]
            quiz = {'quiz': {'id': code.quiz_id},
                    'questions': QandA}
            return HttpResponse(json.dumps(quiz), status=200)

        except Code.DoesNotExist:
           return HttpResponse(status=400)


@csrf_exempt
def quizcheck(request):
    print "in quizcheck"
    body = json.loads(request.body)['data']
    try:
        token = body.get('token', '')
        code = Code.objects.get(code=token)
    except Code.DoesNotExist:
        return HttpResponse(status=400)
    print request.body
    answers = body.get('answers', '')
    if answers != '':
        results = code.quiz.validate_answers(answers)
    if len(results) != 0:
        return HttpResponse(json.dumps(results), status=400)

    code.quiz_complete = True;
    code.save();
    return HttpResponse('valid')


class StartedWatching(View):
    def post(self, request):
        token = request.POST.get('token', '')
        try:
            code = Code.objects.get(code=token)
            code.started_watching = datetime.now()
            code.save()
            return HttpResponse(status=200)
        except:
            return HttpResponse(status=400)


class FinishedWatching(View):
    def post(self, request):
        token = request.POST.get('token', '')
        try:
            code = Code.objects.get(code=token)
            code.finished_watching = datetime.now()
            code.save()
            return HttpResponse(status=200)
        except:
            return HttpResponse(status=400)


class ValidateQuiz(View):
    def post(self, request):
        token = request.POST.get('token', '')
        try:
            code = Code.objects.get(code=token)
        except:
            return HttpResponse(status=400)

        # expects json in the form of:
        # { data : { quiz: { id: 1 },
        # questions: [ 1, 2, 3],
        # answers: [ 4, 52, 13]
        # } }

def SelectGift(request):
    return HttpResponse()


def ListStores(request):
    stores = Store.objects.all()
    stores = [{'name':store.name, 'img_url':store.image_url} for store in stores]
    return HttpResponse(json.dumps(stores))

@csrf_exempt

def SaveStoreSelection(request):
    body = json.loads(request.body)
    code = body.get('token', '')
    email = body.get('email', '')
    storeName = body.get('storeSelection', '')
    try:
        code = Code.objects.get(code=code)
        store = Store.objects.get(name=storeName)
        if not code.quiz_complete:
            return HttpResponse(status=400)
    except:
        return HttpResponse(status=400)
    try:
        storeid = code.store.id
        return HttpResponse("already has a store!", status=200)
    except:
        code.store = store
        code.chosen_email = email
        code.save()
        return HttpResponse(status=200)


def PayItForward(request):
    body = json.loads(request.body)
    code = body.get('token', '')
    email = body.get('email', '')
    try:
        code = Code.objects.get(code=code)

    except:
        return HttpResponse(status=400)
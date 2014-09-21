from datetime import datetime

from django import forms
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView

from .models import Token


# def watch_video(request):
#     if not request.user.is_authenticated():
#         return HttpResponseRedirect('home')
#     # TODO: get user's prescribed video, or a default.
#     return render(request, 'learn.html', dictionary={'video': Video.objects.all()[0]})


# TODO: multiple quiz forms, or random subset of questions.
class QuizForm(forms.Form):
    YES, NO, SOME = 'yes', 'no', 'some'
    WATCHED_VIDEO_CHOICES = (
        (NO, 'No'),
        (YES, 'Yes'),
        (SOME, 'Some of it...')
    )
    watched_video = forms.ChoiceField(
        choices=WATCHED_VIDEO_CHOICES,
        label="Did you watch the video? (No lying.)",
        # widget=forms.RadioSelect,
    )

    code = forms.CharField(max_length=5)

    def clean_watched_video(self):
        response = self.cleaned_data['watched_video']
        if response != 'yes':
            raise forms.ValidationError('Wrong answer!')
        return response

    def clean_code(self):
        code = self.cleaned_data['code']
        if Token.objects.filter(code=code).exists():
            token = Token.objects.get(code=code)
            if token.is_valid:
                return code
            else:
                raise forms.ValidationError('This code has already been used.')
        else:
            raise forms.ValidationError('This code is invalid.')


# class CodeRedeemForm(forms.Form):
#     code = forms.CharField(max_length=5)
#
#     def clean_code(self):
#         code = self.cleaned_data['code']
#         if Token.objects.filter(code=code).exists():
#             token = Token.objects.get(code=code)
#             if token.is_valid:
#                 return code
#             else:
#                 raise forms.ValidationError('This code has already been used.')
#         else:
#             raise forms.ValidationError('This code is invalid.')


def learn(request):
    if request.method == 'POST':
        # TODO: throttling
        form = QuizForm(request.POST)
        if form.is_valid():
            token = Token.objects.get(code=form.data['code'])
            token.redeemed = datetime.now()
            token.save()
            return render(request, 'thanks.html')
        else:
            # Incorrect responses; take quiz again.
            return render(request, 'learn.html', dictionary={'form': form})
    else:
        form = QuizForm()
        return render(request, 'learn.html', dictionary={'form': form})
#
#
# def redeem(request):
#     if request.method == 'POST':
#         # TODO: throttling
#         form = CodeRedeemForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('thanks')
#         else:
#             return render(request, 'redeem.html', dictionary={'form': form})
#     else:
#         form = CodeRedeemForm()
#         return render(request, 'redeem.html', dictionary={'form': form})

def thanks(request):
    return render(request, 'thanks.html')
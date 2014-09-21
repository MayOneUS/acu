from collections import namedtuple
from datetime import datetime

from django import forms
from django.shortcuts import render

from .models import Token


Question = namedtuple("Question", ['prompt', 'choices', 'answer'])

quiz = [
    Question(
        "When an individual has incentives that work against their professional responsibilities, this is often called a _______.",
        [
            "Free Market",
            "Fundamental Error",
            "Conflict of Interest     x",
            "System Failure",
        ],
        2
    ),

    Question(
        "True or False: Conflicts of interest can be found frequently in society",
        [
            "True          x",
            "False",
        ],
        0
    ),

    Question(
        "When a doctor is seeking the right treatment for a patient, which of these factors would most likely become a conflict of interest?",
        [
            "Patient's medical history",
            "A medicine company sending a doctor on a nice business trip          x",
            "Doctor's salary increasing with years in the business",
            "Patient grew up in the same state as the doctor",
        ],
        1
    ),

    Question(
        "Which of these is a clear conflict of interest when someone is buying a home?",
        [
            "The real estate agent represents both the buyer and the seller            x",
            "The buyers know the person selling the house personally",
            "Two different real estate agents represent the buyer and the seller",
            "The real estate agent for the buyer is also on the local school committee",
        ],
        0
    ),

    Question(
        "Which professor is likely to design the least challenging class? A professor promoted on..",
        [
            "the content of the syllabus",
            "the opinions of the faculty",
            "the knowledge of their field",
            "the opinions of the students     x",
        ],
        3
    ),

    Question(
        "Which of these helps to reduce conflicts of interest?",
        [
            "Codes of Conduct",
            "Respect customers or clients perspective",
            "Consulting more-experienced or trustworthy people",
            "All of the Above      x",
        ],
        3
    ),
]


# TODO: multiple quiz forms, or random subset of questions.
class QuizForm(forms.Form):
    # YES, NO, SOME = 'yes', 'no', 'some'
    # WATCHED_VIDEO_CHOICES = (
    #     (NO, 'No'),
    #     (YES, 'Yes'),
    #     (SOME, 'Some of it...')
    # )
    # watched_video = forms.ChoiceField(
    #     choices=WATCHED_VIDEO_CHOICES,
    #     label="Did you watch the video? (No lying.)",
    #     widget=forms.RadioSelect,
    # )

    # Unsure how dynamically monkey-patching these fields on would work with
    # the Form class' declarative syntax, so explicitly declaring all questions for now.
    q0 = forms.ChoiceField(
        widget=forms.RadioSelect,
        label=quiz[0].prompt,
        choices=list(enumerate(quiz[0].choices))
    )

    q1 = forms.ChoiceField(
        widget=forms.RadioSelect,
        label=quiz[1].prompt,
        choices=list(enumerate(quiz[1].choices))
    )

    q2 = forms.ChoiceField(
        widget=forms.RadioSelect,
        label=quiz[2].prompt,
        choices=list(enumerate(quiz[2].choices))
    )

    q3 = forms.ChoiceField(
        widget=forms.RadioSelect,
        label=quiz[3].prompt,
        choices=list(enumerate(quiz[3].choices))
    )

    q4 = forms.ChoiceField(
        widget=forms.RadioSelect,
        label=quiz[4].prompt,
        choices=list(enumerate(quiz[4].choices))
    )

    q5 = forms.ChoiceField(
        widget=forms.RadioSelect,
        label=quiz[5].prompt,
        choices=list(enumerate(quiz[5].choices))
    )

    redemption_code = forms.CharField(
        max_length=5,
        label='Enter your redemption code',
    )

    def clean_watched_video(self):
        response = self.cleaned_data['watched_video']
        if response != 'yes':
            raise forms.ValidationError('Wrong answer!')
        return response


    def clean_code(self):
        code = self.cleaned_data['redemption_code']
        if Token.objects.filter(code=code).exists():
            token = Token.objects.get(code=code)
            if token.is_valid:
                return code
            else:
                raise forms.ValidationError('This code has already been used.')
        else:
            raise forms.ValidationError('This code is invalid.')


    def clean(self):
        for i, question in enumerate(quiz):
            field_name = 'q{}'.format(i)  # gross hax
            if field_name in self.cleaned_data and self.cleaned_data[field_name] != str(question.answer):
                raise forms.ValidationError('Sorry, at least one quiz answer is incorrect.'.format(field_name, self.cleaned_data[field_name], question.answer))
        return self.cleaned_data


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


def home(request):
    if request.method == 'POST':
        # TODO: throttling
        form = QuizForm(request.POST)
        if form.is_valid():
            token = Token.objects.get(code=form.data['redemption_code'])
            token.redeemed = datetime.now()
            token.save()
            return render(request, 'thanks.html')
        else:
            # Incorrect responses; take quiz again.
            return render(request, 'home.html', dictionary={'form': form})
    else:
        form = QuizForm()
        return render(request, 'home.html', dictionary={'form': form})

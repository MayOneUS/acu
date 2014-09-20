from django.http import HttpResponseRedirect
from django.shortcuts import render
from learn.models import Video


def watch_video(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('home')
    # TODO: get user's prescribed video, or a default.
    return render(request, 'videos/watch.html', dictionary={'video': Video.objects.all()[0]})

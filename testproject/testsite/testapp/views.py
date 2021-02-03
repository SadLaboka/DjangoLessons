from django.shortcuts import render
from .models import Rubric


def test(request):
    return render(request, 'testapp/test.html', context={'rubrics': Rubric.objects.all()})


def get_rubric(request):
    pass
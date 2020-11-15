from django.shortcuts import render

from .models import Surveys, Result, Questions

# Create your views here.
def main(request):
    title = 'Главная'

    text = Surveys.objects.all()
    content = {"title": title, "text": text}

    return render(request, 'mainapp/index.html', content)

def survey(request, pk=None):
    print(type(pk))
    return render(request, "mainapp/survey.html")
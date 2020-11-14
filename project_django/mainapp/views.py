from django.shortcuts import render

# Create your views here.
def main(request):
    title = 'Главная'
    text = {'name': 'Тутачки текс вставляется на главную)))'}

    content = {"title": title, "text": text}

    return render(request, 'mainapp/index.html', content)

def survey(request):
    return render(request, "mainapp/survey.html")

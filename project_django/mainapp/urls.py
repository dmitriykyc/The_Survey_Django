from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.Surveys, name='index'),
    path('<int:pk>/', mainapp.Surveys, name='survey'),

]

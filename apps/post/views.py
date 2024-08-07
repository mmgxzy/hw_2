from django.shortcuts import render
from django.utils import timezone

# Create your views here.

def index(request):
    context = {
        'title': "Главная",
        'description': "Описание главной страницы",
    }
    return render(request, 'index.html', context)

def news(request):
    context = {
        'title': 'новости',
        'description': 'ничего'
    }
    return render(request, 'news.html', context)



def contact(request):
    context = {
        'title': 'контакты',
        'description': 'ничего'
    }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        'title': "О нас",
        'description': "Мы группа 18-1B ",
        'students': ['Митаева Кызжибек', 'Нурпаяз кызы Арууке', 'Анвардинов Билолдин', 'Анапияев Залкар']
    }
    return render(request, 'about.html', context)

def time(request):
    current_time = timezone.now()
    context = {
        'title': "время",
        'date': current_time.strftime('%Y-%m-%d'),
        'time': current_time.strftime('%H:%M:%S'), 
    }
    return render(request, 'time.html', context)



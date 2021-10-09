from django.shortcuts import render


def index(request):
    name = 'первое изменение'
    return render(request, 'index.html', locals())

def index2(request):
    name = 'второе изменение'
    return render(request, 'index2.html', locals())

def index3(request):
    name = 'Rosa Rusvelt'
    return render(request, 'index3.html', locals())

def index4(request):
    name = 'Sape Svano'
    return render(request, 'index4.html', locals())

def index5(request):
    name = 'Andro Dodo'
    return render(request, 'index5.html', locals())
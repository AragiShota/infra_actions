from django.http import HttpResponse


def index(request):
    return HttpResponse('Почему мы всё ещё здесь?')


def second_page(request):
    return HttpResponse('А это вторая страница!')

from django.http import HttpResponse


def index(request):
    return HttpResponse("Семён, пошли бухать!!!")



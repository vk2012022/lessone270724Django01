from django.http import HttpResponse

def data_view(request):
    return HttpResponse("Это страница с данными.")

def test_view(request):
    return HttpResponse("Это страница с тестом.")



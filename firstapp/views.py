from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, "index.html")


def my_folio_view(request):
    return render(request, "my_folio.html")


def lorem_view(request):
    return render(request, "lorem.html")
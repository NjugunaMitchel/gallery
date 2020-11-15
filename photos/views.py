from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def photos(request):
    return render(request, 'photos.html')

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Pictures.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'photos.html',{"message":message,"photos": searched_category})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photos.html',{"message":message})

from django.shortcuts import render
from django.http import HttpResponse
from .models import Pictures,Editor, category


def index(request):
    return render(request, 'index.html')

def photos(request):
   photos= Pictures.objects.all()
   context = {'photos':photos}
   return render(request,'photos.html',context)

   
def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Pictures.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"photos": searched_category})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})




def photo(request,photo_id):
    try:
        photo = Pictures.objects.get(id = photo_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"photo.html", {"photo":photo})



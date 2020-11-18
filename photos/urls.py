from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import  views

urlpatterns=[
    path('',views.index,name='landing'),
    path(r'photos/',views.photos,name='gallery'),
    path(r'photo/<int:photo_id>/',views.photo,name='details'),
    path(r'search/', views.search_results, name='search_results')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
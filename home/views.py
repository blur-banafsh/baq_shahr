from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.


def home_menu(request):
    if request.method == 'GET':
        cate = Category.objects.all()
        cat_all_gallery = CategoryForGallery.objects.all()
        return render(request, 'index.html', context={'cat': cate,
                                                      'all': cat_all_gallery})


def gallery_menu(request, pk):
    if request.method == "GET":
        cat_all_gallery = CategoryForGallery.objects.filter(id=pk)
        cate = Category.objects.all()
        return render(request, 'allgallery.html', context={'all': cat_all_gallery,
                                                           'cat': cate})



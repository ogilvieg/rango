from django.shortcuts import render
from django.http import HttpResponse

from models import Category, Page

# Create your views here.
def index(request):
    """
    Query all categories from database and retrieve top 5
    """
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list }

    return render(request, 'rango/index.html', context_dict)

def about(request):

	return render(request, 'rango/about.html', {})

def category(request, category_name_slug):

    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category

    except Category.DoesNotExist:
        pass


    return render(request, 'rango/category.html', context_dict)

from django.shortcuts import render
from django.http import HttpResponse

from models import Category, Page
from forms import CategoryForm

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


def add_category(request):

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            # Save the new category to the database
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return  index(request)
        else:
            # The supplied form contained errors - just print them to the terminal
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()

    return render(request, 'rango/add_category.html', {'form': form})
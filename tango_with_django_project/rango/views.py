from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

	page = """Hello world! <br/> <a href='/rango/about'>About</a>"""
	return HttpResponse(page)

def about(request):

	page = """Rango says here is the about page. <br><a href='/rango/'>Index</a>"""
	return HttpResponse(page)
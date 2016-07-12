from django.shortcuts import render
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, HttpResponse
from django.http import HttpResponse
from rango.models import Category

def home(request):
	content = {}
	return render_to_response('home.html', content, context_instance=RequestContext(request))

def about(request):
	return HttpResponse('Rango says here is the about page')

def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    # Render the response and send it back!
    return render(request, 'rango/index.html', context_dict)
# Create your views here.

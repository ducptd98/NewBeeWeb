from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	response = HttpResponse()
	response.writelines("<h1>Hello, Do you see me?</h1>")
	response.write("This is home app")
	return response

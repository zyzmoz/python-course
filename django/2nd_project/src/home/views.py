from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request, *args, **kwargs):
  my_context = {"text":"Hello guys!"}
  print(type(my_context))
  return render(request, "home.html",my_context)
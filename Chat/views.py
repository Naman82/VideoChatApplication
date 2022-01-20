from django.shortcuts import render
from django.template import context

# Create your views here.
def index(request):
    # context={}
    return render(request,'Chat/index.html')
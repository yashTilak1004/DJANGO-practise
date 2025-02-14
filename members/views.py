from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import members

#def home(request):
#    obj = loader.get_template('f.html')
#    return HttpResponse(obj.render())

def home (request):
    mymembers = members.objects.all().values()
    temp = loader.get_template('all_members.html')
    context = {
        'mymembers' : mymembers
    }
    return HttpResponse(temp.render(context,request))

def details(request,id):
    mymember = members.objects.get(id=id)
    print(mymember)
    temp = loader.get_template('details.html')
    context = {
        'mymembers':mymember
    }
    return HttpResponse(temp.render(context,request))

def main(request):
    temp = loader.get_template('main.html')
    return HttpResponse(temp.render())
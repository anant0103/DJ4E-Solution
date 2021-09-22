from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def myview(request):
    n=request.session.get('n',0)+1
    request.session['n']=n
    if n>4:
        del(request.session['n'])
    resp=HttpResponse('view count='+str(n))
    resp.set_cookie('dj4e_cookie', 'ed9c7f78', max_age=1000)
    return resp
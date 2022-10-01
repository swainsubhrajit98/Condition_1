from django.shortcuts import render

# Create your views here.
def Cond(request):
    d={'a':5,'b':10,'c':6}
    return render(request,'cond.html',context=d)
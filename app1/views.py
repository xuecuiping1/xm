from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')


def zwn(request):
    return render(request,'zwn.html')

def lyj(request):
    return render(request,'lyj.html')

def xcp(request):
    return render(request,'xcp.html')


def zyl(request):
    return render(request,"zyl.html")


def lww(request):
    return render(request,"lww.html")


def qyx(request):
    return render(request,"qyx.html")
from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':200,'b':400,'c':600}
    return render(request,'condition.html',context=d)

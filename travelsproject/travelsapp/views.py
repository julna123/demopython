from django.shortcuts import render
from .models import Place, Meet
#from. models import Team
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    item = Meet.objects.all()
    return render(request,"index.html",{'result':obj,'results': item})
#def orgin(request):
    #obj1=Team.objects.all()
    #return render(request, "index.html",{'result1':obj1})



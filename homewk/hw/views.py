from django.shortcuts import render

# Create your views here.
from .models import huluwa

def getall(req):
    data=huluwa.objects.all()
    result={
        'title':"葫芦娃",
        'person':data
    }
    return  render(req,"huluwa.html",result)
#索引查找法
def getkey(req):
    data=req.GET
    kw=data.get("kw")
    res=huluwa.objects.filter(
        name__contains=kw
    )
    res=huluwa.objects.filter(
        height__in=[160,180])
    res=huluwa.objects.filter(
        height__gt=170
    )
    res=huluwa.objects.filter(
        birthday__year=2018
    )
    return render(req,"huluwa.html",{'person':res})

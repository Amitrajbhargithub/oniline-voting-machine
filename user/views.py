from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import datetime
from django.db import connection


# Create your views here.
def home(request):
    pdata = parties.objects.all().order_by('-id')
    aadhar=request.session.get('aadhar')
    cursor = connection.cursor()
    cursor.execute("select p.*, r.* from user_poll p,user_uregister r where r.uadhar=p.aadhar order by p.id desc")
    polldata = cursor.fetchall()
    print(polldata)

    if request.session.get('aadhar'):
        if request.method=='POST':
            a=request.POST.get("partyname","")
            b=request.POST.get("msg","")
            poll(pname=a,comment=b,aadhar=aadhar,pdate=datetime.datetime.now()).save()
            return  HttpResponse("<script>alert('Thanks for sharing your idea..');window.location.href='/user/home/'</script>")

    return render(request, 'user/index.html', {"data": pdata,"poll":polldata})


def contactus(request):
    status = False
    if request.method == 'POST':
        Name = request.POST.get("name", "")
        Email = request.POST.get("email", "")
        Mobile = request.POST.get("mobile", "")
        Message = request.POST.get("msg", "")
        contact(name=Name, email=Email, mobile=Mobile, message=Message).save()
        status = True
    return render(request, 'user/contactus.html', {'S': status})


def uelection(request):
    edata = upcomingelection.objects.all().order_by('-id')
    return render(request, 'user/uelection.html', {"data": edata})


def signup(request):
    if request.method == 'POST':
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        mobile = request.POST.get("mobile", "")
        password = request.POST.get("passwd", "")
        address = request.POST.get("address", "")
        picname = request.FILES['fu']
        profile(name=name, mobile=mobile, email=email, passwd=password, address=address, ppic=picname).save()
        return HttpResponse("<script>alert('You are Registered successfully..');</script>")

    return render(request, 'user/signup.html')


def result(request):
    cursor=connection.cursor()
    cursor.execute("select vparty,count(vparty) from user_vote group by vparty order by count(vparty) desc")
    res=cursor.fetchall()
    print(res)
    return render(request, 'user/result.html',{"vote":res})


def usignin(request):
    if request.method == 'POST':
        name = request.POST.get("uname", "")
        passwd = request.POST.get("upasswd", "")
        data = uregister.objects.filter(uadhar=name, upasswd=passwd)
        if data.count() > 0:
            request.session['aadhar'] = name
            return HttpResponse("<script>window.location.href='/vote';</script>")
        else:
            return HttpResponse(
                "<script>alert('Aadhar no. or Password are Incorrect..');window.location.href='/usignin';</script>")
    return render(request, 'user/usignin.html')


def register(request):
    status = False
    if request.method == 'POST':
        uname = request.POST.get("uname", "")
        ugender = request.POST.get("ugender", "")
        udob = request.POST.get("udob", "")
        umobile = request.POST.get("umobile", "")
        uadhar = request.POST.get("uadhar", "")
        upassword = request.POST.get("upasswd", "")
        ustate = request.POST.get("ustate", "")
        ucity = request.POST.get("ucity", "")
        rdate = request.POST.get("rdate", "")
        upicname = request.FILES['upic']
        a = uregister.objects.filter(uadhar=uadhar).count() > 0
        if a == True:
            return HttpResponse(
                "<script>alert('You are already registered..');window.location.href='/register/';</script>")
        else:
            uregister(uname=uname, ugender=ugender, udob=udob, umobile=umobile, uadhar=uadhar, upasswd=upassword,
                      ustate=ustate, ucity=ucity, rdate=rdate, upic=upicname).save()
            return HttpResponse(
                "<script>alert('You are Registered successfully..');window.location.href='/register/';</script>")
            status = True

    return render(request, 'user/uregistration.html', {'S': status})


def voteforparty(request):
    vdata = parties.objects.all()
    aadharno = request.session.get('aadhar')
    if request.method == "POST":
        a = request.POST.get('vote', '')
        checkvoter=vote.objects.filter(aadhar=aadharno).count()
        if checkvoter>0:
            return HttpResponse("<script>alert('You are alerady atemped..');window.location.href='/user/home/';</script>")
        else:
            vote(aadhar=aadharno, vparty=a, vdate=datetime.datetime.now()).save()
            return HttpResponse("<script>alert('Thanks for vote..');window.location.href='/user/home/';</script>")

    return render(request, 'user/voteforparty.html', {"party": vdata})

def logout(request):
    del request.session['aadhar']
    return render(request,'user/index.html')
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import stud
from django.template import loader
from .models import just_img
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail


def r_works(request):
    return render(request,"home.html")

def home(request):
    return render(request,"home.html")

def video(request):
    return render(request,"video.html")

def images(request):
    return render(request,"image.html")

def map(request):
    return render(request,"map.html")

def certificate(request):
    return render(request,"certificate.html")

def service(request):
    return render(request,"service.html")

def DJ(request):
    return render(request,"dj and sound.html")

def lighting(request):
    return render(request,"lighting.html")

def fitting(request):
    return render(request,"fitting.html")

def repair(request):
    return render(request,"repair.html")


def saved(request):
    return render(request,"saved.html")

def record(request):
    data=stud.objects.all()
    temp=loader.get_template("record.html")
    context={
        'data':data
    }
    return HttpResponse(temp.render(context,request))

@login_required
def about(request):
    if request.method=="POST":
        namee=request.POST.get('namee')
        add=request.POST.get('add')
        pho=request.POST.get('pho')
        pin=request.POST.get('pin')
        mail=request.POST.get('mail')
        mark=request.POST.get('mark')

        s=stud()
        s.name=namee
        s.address=add
        s.phone=pho
        s.pincode=pin
        s.email=mail
        s.remarks=mark
        s.save()
        return redirect('/saved')
    
    return render(request,"about.html")

def delete(request,a):
    x=stud.objects.get(id=a)
    x.delete()
    return redirect("/record")

def updt(request,a):
    x=stud.objects.get(id=a)
    x.updt()
    return redirect('saved')

def update(request,a):
    if request.method=="POST":
        namee=request.POST.get('namee')
        add=request.POST.get('add')
        pho=request.POST.get('pho')
        pin=request.POST.get('pin')
        mail=request.POST.get('mail')
        mark=request.POST.get('mark')

        s=stud.objects.get(id=a)
        s.name=namee
        s.address=add
        s.phone=pho
        s.pincode=pin
        s.email=mail
        s.remarks=mark
        s.save()
        return redirect('/record')
    
    return render(request,"update.html")


def signup(request):
    if request.method =="POST":
        uname = request.POST.get('username')
        phone = request.POST.get('phone')
        eml = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        img = request.FILES.get('img')
        if pass1 != pass2:
            return HttpResponse("password are note same")
        else:
            SUB="WELCOME TO RANA ELECTRICAL WORKS"
            content=f"{uname} WELCOME TO RANA ELECTRICAL WORKS your PASSWORD is {pass1}"
            send_mail( SUB,content,settings.EMAIL_HOST_USER,[eml] )
            
            im = just_img()
            im.image =img
            im.phone =phone
            im.save()
            
            my_user = User.objects.create_user(uname,eml,pass1)
            my_user.save()

            return redirect('/login')

    return render(request,'singhup.html')

def loginp(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass1') 
        user = authenticate(request,username=username, password=pass1)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return HttpResponse("User Name Or Password  Are Not Same")

    return render(request,'login.html')

def LogoutPage(request): 
    logout(request)
    return redirect('/home')

# @login_required
# def SendEmail(request):
#    if request.method == "POST":
#       to = request.POST.get('toemail')
#       content = request.POST.get('content')
#       send_mail( "ANUJ RANA",content,settings.EMAIL_HOST_USER,[to] )
#       return render(request,'email.html',{'title':'send an email'})
#    else:
#       return render(request,'email.html',{'title':'send an email'})




# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, UserLoginForm, UserDetailsForm, UpdateDetailsForm, UpdatePersonalDetails, CommentForm, NumberForm, OTPForm
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .addressdetails import province, skillslist
from django.http import HttpResponse, HttpResponseRedirect
from .models import UserDetails, Comments, ViewsTracker
from django.db.models import Q
from datetime import datetime
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from . import sms
import random

def showusers(request):
    obj_list = UserDetails.objects.filter().distinct()
    paginator = Paginator(obj_list,12)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        obj = paginator.page(page)
    except(EmptyPage, InvalidPage):
        obj = paginator.page(paginator.num_pages)
    context = {"users": obj, "title":"Users on KJagir"}
    return render(request, 'users.html', context)

def deletecomment(request, id, userid):
    obj = get_object_or_404(Comments,id=id)
    if request.method == "POST":
        if(obj.user.id==request.user.id):
            obj.delete()
            return redirect('/accounts/user/'+str(userid))
        else:
            return render(request, 'pages/message.html', {'message':"Sorry, you're not allowed to delete the comment!"})
    context = {
        "obj": obj
    }
    return render(request,"deletecomment.html", context)

def changepassword(request):
    if request.method =='POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.user = request.user
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/')
    else:
        form = PasswordChangeForm(request.user)
    context = {"form":form}
    return render(request, 'changepassword.html', context)

def addemail(request):
    if request.method =='POST':
        form = UpdatePersonalDetails(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UpdatePersonalDetails(instance=request.user)
    context = {"form":form}
    return render(request, 'updatepersonaldetails.html', context)

def enternumber(request):
    form = NumberForm(request.POST or None)
    if form.is_valid():
        number = request.POST['number']
        n = User.objects.filter(username=number).count()
        print(n)
        if (n == 0):
            otp = sms.num_to_register(number)
        else:
            context = {'message':"माफ गर्नुहोस्, नम्बर पहिले नै रजिस्टर भएकाे छ। कृपया, Login गर्नुहाेस्।", 'link':"/accounts/login", 'btnname':"Login"}
            return render(request, 'pages/msg.html', context)
        return redirect('/accounts/enterotp/'+str(otp)+'/'+str(number))

    context = { "title": "Register on KJagir | Enter your mobile number:", "form": form,  }
    return render(request, 'forotp.html', context)

def otpprocess(request, otp, number):
    form_otp = OTPForm(request.POST or None)
    if form_otp.is_valid():
        getotp= request.POST['otp']
        data = { 'number':number }
        form_register = RegistrationForm(initial=data)
        if getotp==str(otp):
            print("Correct OTP, great success")
            context = { "title": "Registration Form", "form": form_register, "number":number }
            return render(request, 'register.html', context)
    context = { "title": "OTP Form", "form": form_otp }
    return render(request, 'enterotp.html', context)

def register(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        number = request.POST['number']
        password1 = request.POST['password1']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        obj=User.objects.create_user(username=number, password=password1, first_name=firstname.title(), last_name=lastname.title())
        obj.save()
        update_session_auth_hash(request, request.user)
        return redirect("/accounts/profile")
    context = {"title": "Registration Form", "form": form}
    return render(request, 'register.html', context)

@login_required(login_url="/accounts/login")
def profile(request):
    try:
        if request.method == 'POST' or None:
            c = check_profile(request)
            if c:
                form = UserDetailsForm(request.POST or None)
                if request.user.is_authenticated and request.POST.get('province')!='none' and request.POST.get('district')!=None and request.POST.get('municipality')!=None:
                    pv = request.POST.get('province')
                    district = request.POST.get('district')
                    municipality = request.POST.get('municipality')
                    wardno = request.POST.get('wardno')
                    aboutSkill = request.POST.get('aboutSkill')
                    s = request.POST.get('skillslist')
                    age = request.POST.get('age')
                    obj = UserDetails(province=pv,district=district,municipality=municipality,ward=wardno,age=age,skills=s,skilldetails=aboutSkill)
                    obj.user = request.user
                    obj.save()
                    return redirect('/accounts/user/'+str(request.user.id))
            else:
                return render(request, 'pages/message.html', {'message':"The profile already exists."})
        else:
            form = UserDetailsForm()
        provinces = province()
        context = {"title": "User Details Form - KJagir", "provinces": provinces, "form":form}
        return render(request, 'profile.html', context)
    except:
        return render(request, 'pages/message.html', {'message':"The profile already exists."})

def check_profile(request):
    count=UserDetails.objects.filter(user__id=request.user.id).count()
    if count>0:
        return False
    else:
        return True

def province1(request):
    return HttpResponse('<h1>Page was found</h1>')

#@login_required(login_url="/accounts/login")
def userinfo(request, id):
    try:
        userdetailsobj = get_object_or_404(UserDetails, user__id=id)
        userobj = get_object_or_404(User, id=id)
        dadded=userdetailsobj.timestamp
        comments = Comments.objects.filter(userdetails=userdetailsobj).order_by('-id')
        if request.method == 'POST' or None:
            form = CommentForm(request.POST or None)
            if form.is_valid():
                comment = request.POST.get('content')
                Comments.objects.create(userdetails=userdetailsobj, user=request.user, content=comment)
                return redirect('/accounts/user/'+str(userdetailsobj.user.id))
        else:
            form = CommentForm()
        title = f"{ userdetailsobj.skills } | { userdetailsobj.municipality } - { userdetailsobj.ward } | { userdetailsobj.district } | { userdetailsobj.province } | KJagir"
        liked=True
        likes=None
        if(request.user.is_authenticated):
            views = ViewsTracker.objects.filter(user=request.user, userdetails=userdetailsobj)
            if (views.exists()==False):
                ViewsTracker.objects.create(userdetails=userdetailsobj, user=request.user)
            if (userdetailsobj.likes.filter(id=request.user.id)):
                liked = True
            else:
                liked = False
            likes = UserDetails.objects.filter(likes=request.user)
        noofviews = ViewsTracker.objects.filter(userdetails=userdetailsobj).count()
        context = { "userdetail": userdetailsobj, "userinfo": userobj, "title":title, "date":dadded, 'comments':comments, 'form':form, 'views':noofviews, 'liked':liked, 'likes':likes }
        context['recommend'] = recommend_profiles(userdetailsobj)
        if(userdetailsobj!=None):        
            return render(request, 'userdetails.html', context)
    except:
        userobject = get_object_or_404(User, id=id)
        context = {'message':"Sorry, the profile doesn't exist.", 'link':"/accounts/profile", 'btnname':"Create Profile", 'userobj':userobject}
        return render(request, 'pages/message.html', context)

def recommend_profiles(obj):
    users = list(UserDetails.objects.filter(skills__icontains = obj.skills))
    random.shuffle(users)
    u = users[:4]
    two = list(UserDetails.objects.all()[:30])
    random.shuffle(two)
    u.extend(two[:2])
    return u

def likeuser(request, id):
    if request.user.is_authenticated:
        obj = get_object_or_404(UserDetails, user__id=id)
        if obj.likes.filter(id=request.user.id).exists():
            obj.likes.remove(request.user)
        else:
            obj.likes.add(request.user)
    return redirect('/accounts/user/'+str(id))

def logout_view(request):
    logout(request)
    return redirect('/')

def signin(request):
    if request.method=="POST":
        form = UserLoginForm(request.POST or None)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
        else:
            context = {'message':"Login unsuccessful!"}
            return render(request, 'pages/message.html', context)
    else:
        form = UserLoginForm()
    return render(request,'login.html',{"form":form})

        
def updatedetails(request, id):
    try:
        userobj = UserDetails.objects.get(user__id=id)
        form = UpdateDetailsForm(instance=userobj)
        if request.method == 'POST':
            form = UpdateDetailsForm(request.POST, instance=userobj)
            if form.is_valid():
                form.user = request.user
                form.save()
                print(userobj.user.id)
                return redirect('/accounts/user/'+str(userobj.user.id))
        context = {"title": "User Details Form", "form":form }
        return render(request, 'updatedetails.html', context)
    except:
        context = {'message':"Sorry, some error occured."}
        return render(request, 'pages/message.html', context)
def showterms(request):
    return render(request, 'pages/terms.html')

def showprivacy(request):
    return render(request, 'pages/privacy.html')
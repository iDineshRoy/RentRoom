from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import AccountsUserdetails, AccountsComments
from .forms import NumberForm, OTPForm, RegistrationForm, UserLoginForm, UserDetailsForm, CommentForm
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from . import sms
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from room.models import Room

def showusers(request):
    obj_list = AccountsUserdetails.objects.filter().distinct()
    # paginator = Paginator(obj_list,12)
    # try:
    #     page = int(request.GET.get('page','1'))
    # except:
    #     page = 1
    # try:
    #     obj = paginator.page(page)
    # except(EmptyPage, InvalidPage):
    #     obj = paginator.page(paginator.num_pages)
    context = {"users": obj_list, "title":"Users on KJagir"}
    return render(request, 'users.html', context)

def enternumber(request):
    form = NumberForm(request.POST or None)
    if form.is_valid():
        number = request.POST['number']
        n = User.objects.filter(username=number).count()
        print(n)
        if (n == 0):
            otp = sms.num_to_register(number)
        else:
            context = {'message':"Sorry, the number is already registered.", 'link':"login", 'btnname':"Login"}
            return render(request, 'pages/msg.html', context)
        return redirect('/accounts/enterotp/'+str(otp)+'/'+str(number))

    context = { "title": "Enter your mobile number:", "form": form,  }
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
        return redirect("profile")
    context = {"title": "Registration Form", "form": form}
    return render(request, 'register.html', context)

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

def showterms(request):
    return render(request, 'pages/terms.html')

@login_required(login_url="login")
def profile(request):
    # try:
    if request.method == 'POST' or None:
        c = check_profile(request)
        if c:
            form = UserDetailsForm(request.POST or None)
            if request.user.is_authenticated and request.POST.get('province')!='none' and request.POST.get('district')!=None and request.POST.get('municipality')!=None:
                pv = request.POST.get('province')
                district = request.POST.get('district')
                municipality = request.POST.get('municipality')
                wardno = request.POST.get('wardno')
                age = request.POST.get('age')
                time=timezone.now()
                obj = AccountsUserdetails(province=pv,district=district,municipality=municipality,ward=wardno,age=age, timestamp=time)
                obj.user_id = request.user.id
                obj.save()
                return redirect('show_user',str(request.user.id))
        else:
            return render(request, 'pages/message.html', {'message':"The profile already exists."})
    else:
        form = UserDetailsForm()
    context = {"title": "User Details Form - KJagir", "form":form}
    return render(request, 'profile.html', context)
    # except:
    #     return render(request, 'pages/message.html', {'message':"The profile already exists."})

def check_profile(request):
    count = AccountsUserdetails.objects.filter(user__id=request.user.id).count()
    if count>0:
        return False
    else:
        return True

def userinfo(request, id):
    try:
        userdetailsobj = get_object_or_404(AccountsUserdetails, user_id=id)
        userobj = get_object_or_404(User, id=id)
        dadded=userdetailsobj.timestamp
        comment = AccountsComments.objects.filter(userdetails_id=id).order_by('-id')
        time = timezone.now()
        if request.method == 'POST' or None:
            form = CommentForm(request.POST or None)
            if form.is_valid():
                comment = request.POST.get('content')
                AccountsComments.objects.create(userdetails_id=id, user_id=request.user.id, content=comment, timestamp=time, rating=5)
                return redirect('show_user', str(id))
        else:
            form = CommentForm()
        likes = Room.objects.filter(likes=request.user)
        title = f"Rent Room | { userdetailsobj.municipality } - { userdetailsobj.ward } | { userdetailsobj.district } | { userdetailsobj.province } | rent.vpit.com.np"
        context = { "userdetail": userdetailsobj, "userinfo": userobj, "title":title, "date":dadded, 'form':form, 'likes':likes, 'comments':comment }
        context['nearby'] = user_products(userdetailsobj)
        context['allusers'] = User.objects.all()
        if(userdetailsobj!=None):        
            return render(request, 'userdetails.html', context)
    except:
        userobject = get_object_or_404(User, id=id)
        context = {'message':"Sorry, the profile doesn't exist.", 'link':"profile", 'btnname':"Create Profile", 'userobj':userobject}
        return render(request, 'pages/message.html', context)

def user_products(user):
    products = Room.objects.filter(seller=user.user_id)
    return products
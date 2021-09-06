from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from .models import Room, Images, RoomComments, RoomViewsTracker
from .forms import RoomForm, ImageForm, RoomCommentForm
from taggit.models import Tag
from accounts.models import AccountsUserdetails
import functools
import operator
from django.db.models import Q
import random
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from PIL import Image
from io import BytesIO
from django.core.files import File


def homepage(request):
    products = Room.objects.all().order_by('-id')[:4]
    context = {
        'products':products,
    }
    context['location'] = get_location()
    context['noofproducts'] = number_of_products()
    context['text_suggestions'] = text_suggestions(list(products))
    context['tags'] = get_tags()
    context['nearby'] = nearby_suggestions(request)
    return render(request, 'base.html', context)

def nearby_suggestions(request):
    try:
        obj = get_object_or_404(AccountsUserdetails, user_id=request.user.id)
        list_accounts = AccountsUserdetails.objects.filter(municipality=obj.municipality).values_list('user_id', flat=True)
        list_seller = User.objects.filter(id__in=list_accounts).values_list('id', flat=True)
        products = list(Room.objects.filter(seller__in=list_seller))
        random.shuffle(products)
        return products[:8]
    except:
        return None

def get_tags():
    tags = list(Tag.objects.all())
    random.shuffle(tags)
    return tags[:10]

def text_suggestions(products):
    suggestions = list(Room.objects.all())
    suggestions = [x for x in suggestions if x not in products]
    random.shuffle(suggestions)
    return suggestions[:12]


def number_of_products():
    return Room.objects.filter(status='Available').count()

def get_location():
    return get_list_or_404(AccountsUserdetails)

@login_required(login_url="/accounts/login")
def create_product(request):
    try:
        c = check_profile(request)
        if c:
            form = RoomForm(request.POST, request.FILES)
            p = check_product(request, request.POST.get('title'))
            if p:
                if form.is_valid():
                    newpost = form.save(commit=False)
                    newpost.seller = request.user
                    if request.FILES.get('image'):
                        i = Image.open(request.FILES.get('image'))
                        i_io = BytesIO()
                        i.save(i_io, 'JPEG', quality=40)
                        t = request.POST.get('title').strip()
                        b = "!@#$/?:!/;"
                        for char in b:
                            t = t.replace(char,"")
                        newpost.image = File(i_io, name=t+".jpg")
                    newpost.save()
                    form.save_m2m()
                    return redirect('show_product',str(newpost.id))
                context = {
                    'form':form,
                }
                return render(request, 'new_product.html',context)
            else:
                context = { 'message':"Sorry, you have already uploaded this product.", 'link':"/", 'btnname':"Go Home" }
                return render(request, 'pages/msg.html', context)
        else:
            return render(request, '/accounts/profile')
    except:
        context = { 'message':"Sorry, we don't have your address details. Please, create your profile first.", 'link':"/accounts/profile", 'btnname':"Create Profile" }
        return render(request, 'pages/msg.html', context)

def check_product(request, title):
    if Room.objects.filter(Q(title=title) & Q(seller=request.user)).exists():
        return False
    else:
        return True

def check_profile(request):
    if AccountsUserdetails.objects.filter(user_id=request.user.id).exists():
        return True
    else:
        return False

def edit_product(request, id):
    obj = get_object_or_404(Room, id=id)
    form = RoomForm(instance=obj)
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.seller = request.user
            if request.FILES.get('image'):
                i = Image.open(request.FILES.get('image'))
                i_io = BytesIO()
                i.save(i_io, 'JPEG', quality=40)
                t = request.POST.get('title').strip()
                b = "!@#$/?:!/;"
                for char in b:
                    t = t.replace(char,"")
                newpost.image = File(i_io, name=t+".jpg")
            newpost.save()
            form.save_m2m()
            return redirect('show_product',str(newpost.id))
    context = {
        'product':obj, 
        'form':form
        # 'address': add
    }
    return render(request, 'new_product.html', context)

def show_product(request, id):
    obj = get_object_or_404(Room, id=id)
    add = get_object_or_404(AccountsUserdetails, user_id=obj.seller.id)
    images = Images.objects.filter(product=obj)
    increase_views(request, obj)
    context = {
        'product':obj,
        'plocation': add,
        'images': images
    }
    context['comments'] = show_comment(request, obj)
    context['form'] = make_comment(request,obj)
    context['views'] = show_noofviews(request, obj)
    context['likes'] = show_likes(request, obj)
    context['liked'] = liked_or_not(request, obj)
    context['products'] = recommendations(obj)
    context['location'] = get_location()
    a = list(context['products'])
    a.append(obj)
    context['text_suggestions'] = text_suggestions(a)
    context['nearby'] = nearby_suggestions(request)
    context['title'] = f"रु { obj.price } | { obj.title } | { add.municipality } - { add.ward } | { add.district } | { add.province } | kbikri.com"
    return render(request, 'show_product.html', context)

def recommendations(product):
    suggestions = list(Room.objects.all().exclude(id=product.id))
    random.shuffle(suggestions)
    return suggestions[:4]

def liked_or_not(request, obj):
    if(request.user.is_authenticated):
        if (obj.likes.filter(id=request.user.id)):
            liked = True
        else:
            liked = False
        return liked

def increase_views(request, obj):
    if(request.user.is_authenticated):
        views = RoomViewsTracker.objects.filter(user=request.user, product=obj)
        if (views.exists()==False):
            RoomViewsTracker.objects.create(product=obj, user=request.user)

def show_likes(request, obj):
    if(request.user.is_authenticated):
        return Room.objects.filter(likes=request.user)

def show_noofviews(request, obj):
    return RoomViewsTracker.objects.filter(product=obj).count()

def show_comment(request, obj):
    return RoomComments.objects.filter(product=obj).order_by('-id')

def make_comment(request, obj):
    if request.method == 'POST' or None:
        form = RoomCommentForm(request.POST or None)
        if form.is_valid():
            comment = request.POST.get('content')
            RoomComments.objects.create(product=obj, user=request.user, content=comment)
            return redirect('show_product',str(obj.id))
    else:
        form = RoomCommentForm()
    return form

def upload_pics(request, id):
    obj = get_object_or_404(Room, id=id)
    form_image = ImageForm(request.POST)
    if request.method == "POST":
        if form_image.is_valid():
            files = request.FILES.getlist('image')
            for f in files:
                instance = Images()
                i = Image.open(f)
                i_io = BytesIO()
                i.save(i_io, 'JPEG', quality=40)
                t = obj.title
                b = "!@#$/?:!/;"
                for char in b:
                    t = t.replace(char,"")
                instance.image = File(i_io, name=t+".jpg")
                instance.product = obj
                instance.save()
            return redirect('show_product',str(obj.id))
    context = {
        'form':form_image
    }
    return render(request, 'new_product.html',context)

def like_product(request, id):
    if request.user.is_authenticated:
        obj = get_object_or_404(Room, id=id)
        if obj.likes.filter(id=request.user.id).exists():
            obj.likes.remove(request.user)
        else:
            obj.likes.add(request.user)
    return redirect('show_product',str(obj.id))

def delete_pictures(request, id):
    product = get_object_or_404(Room, id=id)
    obj = get_list_or_404(Images, product=product)
    for o in obj:
        o.delete()
    return redirect('show_product',str(product.id))
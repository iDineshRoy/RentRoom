from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import RoomSearchQuery
from accounts.models import AccountsUserdetails
from room.models import Room
from django.core.paginator import Paginator, EmptyPage, InvalidPage
import functools
from django.db.models import Q
import operator
from room.views import get_location
from taggit.models import Tag
from googletrans import Translator
import inflect
from room.views import number_of_products, get_tags, text_suggestions


def search_view(request):
    # try:
    p = inflect.engine()
    translator = Translator()
    query = request.GET.get('q', '')
    print(query)
    q = translator.translate(request.GET.get('q', ''))
    qu = q.text.split()
    queries = []
    for a in qu:
        queries.append(p.singular_noun(a))
    raw_queries = request.GET.get('q', '').split()
    for x in query.split():
        queries.append(x)
    query_nep = translator.translate(query, dest='ne')
    query_nep = query_nep.text.split()
    if request.user.is_authenticated:
        context = { "query":query }
        # RoomSearchQuery.objects.create(user=request.user, query=query)
    if query is not None:
        qset_and = functools.reduce(operator.__and__, [
            Q(title__icontains=q) | 
            Q(description__icontains=q)
            for q in raw_queries])
        qset_or = functools.reduce(operator.__or__, [
            Q(title__icontains=q) | 
            Q(description__icontains=q)
            for q in queries])
        qset_nep_or = functools.reduce(operator.__or__, [
            Q(title__icontains=q) | 
            Q(description__icontains=q)
            for q in query_nep])
        qset_nep_and = functools.reduce(operator.__and__, [
            Q(title__icontains=q) | 
            Q(description__icontains=q)
            for q in query_nep])
        obj_list = []
        # obj_list = Product.objects.filter(qset_and).order_by('-id')
        obj_list.extend(list(Room.objects.filter(qset_and, status='Available').order_by('-id')))
        obj_list.extend(list(Room.objects.filter(qset_or, status='Available').order_by('-id')))
        # obj_list.extend(list(Room.objects.filter(qset_nep_and, status='Available').order_by('-id')))
        # obj_list.extend(list(Room.objects.filter(qset_nep_or, status='Available').order_by('-id')))
        obj_list = list(dict.fromkeys(obj_list))
        num = len(obj_list)
        paginator = Paginator(obj_list,12)
        try:
            page = int(request.GET.get('page','1'))
        except:
            page = 1
        try:
            obj = paginator.page(page)
        except(EmptyPage, InvalidPage):
            obj = paginator.page(paginator.num_pages)
        context = { "query":query, "products":obj, "number":num }
        context['location'] = get_location()
        context['noofproducts'] = number_of_products()
        context['text_suggestions'] = text_suggestions(list(obj))
        context['tags'] = get_tags()
    return render(request,'base.html', context)
    # except:
    #     return render(request, 'pages/message.html', {'message':"Error occured!"})

def quick_search(request):
    if request.is_ajax():
        search_text = request.POST.get('search_text')
    else:
        search_text = ''
    items = Room.objects.filter(title__icontains=search_text)[:8]
    context = { 'items':items }
    return render(request,'quicksearch.html', context)

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    products = get_list_or_404(Room, tags=tag)
    context = {
        'tag': tag,
        'products':products
    }
    context['location'] = get_location()
    context['number']=Room.objects.filter(tags=tag).count()
    context['noofproducts'] = Room.objects.filter(status='Available').count()
    context['text_suggestions'] = text_suggestions(list(products))
    context['tags'] = get_tags()
    return render(request, 'base.html', context)
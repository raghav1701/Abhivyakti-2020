from django.views.generic import CreateView
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import UpdateView
from .models import *
from .forms import *
# Create your views here.
# def redirect2(pk,s,towhere):
#     Id =  str(s) + str(pk)
#     k = {'id':Id}

def index(request):
    return render(request, "index.html")


def events(request):
    return render(request, "events.html")


def contact(request):
    return render(request, "contact.html")


def Registration(request):
    if request.method == "POST":
        form = AgtForm(request.POST)
        if form.is_valid():
            if form.is_valid():
                post = form.save(commit=False)
                print(post.pk)
                post.author = request.user
                post.save()
                s = "AGT-"+str(post.pk)
                return render(request, 'agtredirect.html', {'id': s})
    else:
        form = AgtForm()
    return render(request, 'agt.html', {'form': form, 'price' : 100})

def bigroar(request):
    if request.method == "POST":
        form = BigRoarForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            s = "BIGR-"+str(post.pk)
            return render(request, 'agtredirect.html', {'id': s})
    else:
        form = BigRoarForm()
    return render(request, 'bigroar.html', {'form': form, 'price': 100})


def vyak(request):
    if request.method == "POST":
        form = vyaktitvaForms(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            s = "VYAK-"+str(post.pk)
            return render(request, 'agtredirect.html', {'id': s})
    else:
        form = vyaktitvaForms()
    return render(request, 'bigroar.html', {'form': form, 'price': 150})


def antra(request):
    if request.method == "POST":
        form = AntraForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            s = "ANTRA-"+str(post.pk)
            return render(request, 'agtredirect.html', {'id': s})
    else:
        form = AntraForm()
    return render(request, 'bigroar.html', {'form': form, 'price': 150})


def kav(request):
    if request.method == "POST":
        form = KavyanForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            s = "KAVY"+str(post.pk)
            return render(request, 'agtredirect.html', {'id': s})
    else:
        form = KavyanForm()
    return render(request, 'bigroar.html', {'form': form, 'price': 100})


def ToTheBeat1(request):
    if request.method == "POST":
        form = ToTheBeatForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            s = "TOTHEB-"+str(post.pk)
            return render(request, 'agtredirect.html', {'id': s})
    else:
        form = ToTheBeatForm()
    return render(request, 'bigroar.html', {'form': form, 'price': 150})


def ToTheBeatG(request):
    if request.method == "POST":
        form = ToTheBeatGForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            s = "TOTHEBG-"+str(post.pk)
            return render(request, 'agtredirect.html', {'id': s})
    else:
        form = ToTheBeatGForm()
    return render(request, 'tothebeatg.html', {'form': form, 'price': 350})


def Talk(request):
    if request.method == "POST":
        form = TalkForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            s = "TALK-"+str(post.pk)
            return render(request, 'agtredirect.html', {'id': s})
    else:
        form = TalkForm()
    return render(request, 'talk.html', {'form': form, 'price': 150})


def craftix(request):
    if request.method == "POST":
        form = CraftixForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            s = "CRAFT-"+str(post.pk)
            return render(request, 'agtredirect.html', {'id': s})
    else:
        form = CraftixForm()
    return render(request, 'bigroar.html', {'form': form, 'price': 100})

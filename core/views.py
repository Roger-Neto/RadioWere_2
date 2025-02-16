from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import List

# Create your views here.
def home(request):
    songs = List.objects.all()
    return render(request, "index.html", {"songs":songs})

def save(request):
    vsong = request.POST.get("song")
    vlink = request.POST.get("link")
    List.objects.create(song=vsong, link=vlink)
    songs = List.objects.all()
    return render(request, "index.html", {"songs":songs})

def edit(request, id):
    song = List.objects.get(id=id)
    return render(request, "update.html", {"song":song})

def update(request, id):
    vsong = request.POST.get("song")
    vlink = request.POST.get("link")
    songs = List.objects.get(id=id)
    songs.song = vsong
    songs.link = vlink
    songs.save()
    return redirect(home)

def delete(request, id):
    songs = List.objects.get(id=id)
    songs.delete()
    return redirect(home)

@login_required
def update_page(request):
    return render(request, "update.html")

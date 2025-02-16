from django.shortcuts import render, redirect
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

def registrar(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            novo_user = user_form.save(commit=False)
            novo_user.set_password(user_form.cleaned_data['password'])
            novo_user.save()
            return render(request, 'core/registro_realizado.html', {'novo_user': novo_user})
    else:
        user_form = UserRegistrationForm()
    
    return render(request, 'registro.html',{'user_form': user_form})
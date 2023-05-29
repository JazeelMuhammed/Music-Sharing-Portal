from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import MusicUploadForm
from .models import Song
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
def home(request):
    return render(request, 'app/home.html')


def base(request):
    return render(request, 'app/base.html')


@login_required
def upload_view(request):
    songs = Song.objects.all().filter(is_public=True)
    context = {
        'songs': songs
    }
    return render(request, 'app/upload_view.html', context)


@login_required
def profile(request):
    user = request.user
    songs = Song.objects.all().filter(author=user)
    private_songs = [i for i in songs if i.is_private==True]
    context = {
        'private_songs': private_songs
    }
    return render(request, 'app/profile.html', context)


@login_required
def upload(request):
    if request.method == 'POST':
        form = MusicUploadForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data.get('is_protected') == True:
                user = form.save()
                group = Group.objects.get_or_create(name='new_group')
                user.groups.add(group)
                messages.success(request, f'Uploaded successfully')
                return redirect('/')
            elif form.cleaned_data.get('is_protected') == True:
                form.save()
                messages.success(request, f'Uploaded successfully')
                return redirect('/')
            else:
                form.save()
                messages.success(request, f'successfully uploaded')
                return redirect('songs/')
    else:
        form = MusicUploadForm()
    return render(request, 'app/upload.html', {'form': form})


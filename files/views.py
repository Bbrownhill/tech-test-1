from django.shortcuts import render
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from .forms import FileForm
from .models import File


def upload(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileForm()
    return render(request, 'upload.html', {
        'form': form
    })

def file_list(request):
    files = File.objects.all()
    return render(request, 'file_list.html', {
        'files': files
    })

from django.shortcuts import render,redirect
from.models import Directory
from django.urls import reverse
from django.contrib import messages
from .forms import DirectoryForm

# Create your views here.
def index(request):
    all_records = Directory.objects.all()
    context = {
        'record': all_records
    }
    return render(request, 'directory/index.html', context)


def insert(request):
    form = DirectoryForm(request.POST or None, request.FILES or None)
    context = {
        'form': form
    }
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
    return render(request, 'directory/insert.html', context)


def remove(request, id):
    record = Directory.objects.get(id=id)
    record.delete()
    messages.success(request, 'RECORD REMOVED')
    return redirect(reverse('index'))


def amend(request, id):
    instance = Directory.objects.get(id=id)
    form = DirectoryForm(request.POST or None,
                         request.FILES or None, instance=instance)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
        messages.success(request, 'RECORD AMENDED')
        return redirect(reverse('index'))
    return render(request, 'directory/amend.html', context)


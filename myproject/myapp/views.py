from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import UserForm

def home(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            submitted_data = form.cleaned_data
            return render(request, 'myapp/thank_you.html', {'submitted_data': submitted_data})
    else:
        form = UserForm()
    return render(request, 'myapp/index.html', {'form': form})

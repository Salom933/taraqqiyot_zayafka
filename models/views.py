from django.shortcuts import render, redirect
from .models import User
from .form import UserForm
from .bot import get_post
def contact_page(request):
    form = UserForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        get_post(form.data)
        return redirect('success')
    return render(request, 'index.html', {'form': form})



def success(req):
    return render(req, 'success.html', {})
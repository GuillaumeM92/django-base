from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import MyModel

@login_required
def my_view(request):
    objects = MyModel.objects.all()
    context = {"objects": objects}
    return render(request, 'myapp/objects.html', {'context': context})

from django.shortcuts import render
from .models import MyModel

# Create your views here.
def home(request):
    my_models = MyModel.objects.all()
    return render(request, 'myapp/home.html', {'my_models': my_models})

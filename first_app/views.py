from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    var = {'variable1': 'Hey This is a value from templates tags.'}
    return render(request, 'first_app/index.html', context=var)

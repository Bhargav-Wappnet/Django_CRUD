from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    employes = ["Bhargav", "Bhautik", "Aniket", "Harsh"]
    Values = [1, 1, 1, 2, 2, 4, 5, 6, 3, 8]
    return render(request, 'home.html', context={'emp': employes, 'Values': Values})

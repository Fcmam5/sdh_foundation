
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.

# Display the foundation HomeScreen
def home(request):
    return render(request, 'home.html')

# Display the foundation about page
def about(request):
    return render(request, 'about.html')

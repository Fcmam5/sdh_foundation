
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.

# Display the foundation HomeScreen
def home(request):
    return render(request, 'index.html')

# Display the foundation about page
def about(request):
    return render(request, 'about.html')

# Display the User profile
def privacy_policy(request):
    return render(request, 'privacy-policy.html')

def errors_view(request):
    return render(request, '404.html')

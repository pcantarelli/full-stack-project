from django.shortcuts import render

# Create your views here.
def profile(request):
    """ View to display User Profile information"""
    
    template = 'users/profile.html'
    context = {}

    return render(request, template, context)
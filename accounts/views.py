from django.shortcuts import render

# Create your views here.
#from django.shortcuts import render

from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'profile.html')  # Ensure this template exists

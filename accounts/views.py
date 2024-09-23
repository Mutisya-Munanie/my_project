#from django.shortcuts import render

# Create your views here.

#Sfrom django.views.generic import TemplateView

#class ProfileView(TemplateView):
   # template_name = 'profile.html'  # Ensure this template exists in your templates directory

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

@login_required
def profile_update(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')

        # Update the user's profile
        user = request.user
        user.username = username
        user.email = email
        user.save()

        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')  # Redirect to the profile page after updating
    else:
        # If the request method is not POST, redirect to profile page
        return redirect('profile')



        #custom login

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')  # Redirect to the profile page
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')  # Render your custom login template

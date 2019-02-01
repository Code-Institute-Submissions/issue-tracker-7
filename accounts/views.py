from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

# Create your views here.

def registration_view(request):
	"""
	Register a new user
	"""
	if request.method == "POST":
		registration_form = UserRegistrationForm(request.POST)
		if registration_form.is_valid():
			registration_form.save()
			username = registration_form.cleaned_data.get('username')
			user = auth.authenticate(username=username,
									 password=request.POST['password1'])

			if user:
				auth.login(user=user, request=request)
				messages.success(request, f"Welcome {user}! Your account has been created.")
				return redirect('home')
			else:
				messages.error("Account registration failed")
	else:
		registration_form = UserRegistrationForm()
	return render(request, 'register.html', {'form' : registration_form})

@login_required
def profile_view(request):
	"""
	See the profile page of the user currently logged in
	"""
	return render(request, 'profile.html')
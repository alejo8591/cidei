from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect
from django.template import Context, RequestContext

from accounts.models import UserProfile

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login

# Create your views here.
def register(request):
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UseProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_vaild():
			user = user_form.save()

			user.set_password(user.password)

			user.save()

			profile = profile_form.save(commit=False)

			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']


			profile.save()

		else:
			print user_form.errors, profile_form.errors

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	context = {'user_form' : user_form, 'profile_form' : profile_form}
	return render_to_response('accounts/register.html', context, context_instance=RequestContext(request))
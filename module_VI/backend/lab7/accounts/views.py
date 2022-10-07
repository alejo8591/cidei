from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.template import Context, RequestContext

from accounts.models import UserProfile

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login

from django.contrib.auth import logout

from accounts.forms import UserForm, UserProfileForm

from accounts.serializers import UserProfileSerializer, UserSerializer, UsernameSerializer

from rest_framework import viewsets, generics

# Create your views here.
def register(request):
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
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

def user_logout(request):
	logout(request)

	return HttpResponseRedirect('/app/')

def user_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/app/')

			else:
				return HttpResponse("El usuario esta errado")

		else:
			print "Los detalles de acceso son: {0}, {1}".format(username, password)
			return HttpResponse("Datos invalidos")
	else:
		return render_to_response('accounts/login.html', {}, context_instance=RequestContext(request))


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer

class UsernameViewSetOne(generics.ListAPIView):
	serializer_class = UsernameSerializer

	def get_queryset(self):

		print self.kwargs['username']

		username = self.kwargs['username']

		return User.objects.filter(username__istartswith=username)


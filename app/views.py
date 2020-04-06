from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from app import main
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from app.models import URL

# Create your views here.

@csrf_exempt
def index(request):

	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate( username=username,password=password )

		if user is not None:
			auth.login(request, user)
			return render(request, 'home.html')
			#return HttpResponseRedirect(reverse(''))
		else:
			messages.info(request, 'Invalid Credentials')
			return redirect('index')

	return render(request, 'index.html')

def register(request):
	
	if request.method=='POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']

		if User.objects.filter(username=username).exists():
			
			messages.info(request,'username already exist')
			return redirect('register')
		elif User.objects.filter(email=email).exists():
			
			messages.info(request,'email already exist')
			return redirect('register')

		else:
			user = User.objects.create_user(username=username,email=email,password=password)
			user.save()
			return redirect('home')

	return render(request, 'register.html')

	
@csrf_exempt
def home(request):

	if request.method=='POST':
		
		long_url = request.POST['longurl']
		if long_url[:7] != 'http://' and long_url[:8] != 'https://':
			long_url = 'http://'+long_url

		short_url = main.shorten(long_url)

		current_uri = request.build_absolute_uri()[:-9]

		short_url = current_uri + 'go/' + short_url

		add,created = URL.objects.get_or_create(long_url=long_url, short_url=short_url)
	
		if created:
			add.save()

		if len(long_url)>30:
			long_url = long_url[:28] + '...'

		context = {
			'result':True,
			'long_url':long_url,
			'short_url':short_url,
		}
		return render(request, 'home.html',context=context)

	return render(request, 'index.html')

def redirect_user(request,short_url):

	current_url = request.build_absolute_uri()[:-1]
	long_url = URL.objects.filter(short_url=current_url).values()[0]['long_url']
	return redirect(long_url)


def logout(request):
	auth.logout(request)
	return redirect('index')

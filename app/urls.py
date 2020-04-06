from django.conf.urls import url
from django.urls import path
from app import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^register/', views.register,name='register'),
	url(r'^home/', views.index, name='home'),
	url(r'^logout/', views.logout, name='logout'),
	url(r'^generate/', views.home, name='generate'),
	path('go/<str:short_url>/', views.redirect_user, name='redirect_user')
]
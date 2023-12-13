from django.urls import path
from .views import Signup, Login, Logout, Logout, Profile, like

urlpatterns = [
	path('signup/', Signup.as_view(), name = 'signup'),  
	path('login/', Login, name = 'Login'),  
	path('logout/', Logout, name = 'Logout'),  
	path('profile/', Profile, name = 'Profile'),  
	path('like/<int:id>', like, name = 'like')

]



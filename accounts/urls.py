from accounts.views.signin import Signin
from accounts.views.signup import Singnup
from accounts.views.user import GetUser

from django.urls import path

urlpatterns = [
    path('signin', Signin.as_view()),
    path('signup', Singnup.as_view()),
    path('users', GetUser.as_view())
]
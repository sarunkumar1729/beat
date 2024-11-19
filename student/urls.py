from django.urls import path  
from .import views

urlpatterns = [
      path('register_trainer',views.register_trainer,name='register_trainer'),
      path('login_trainer',views.login_trainer,name='login_trainer'),
      path('trainer_home',views.trainer_home,name='trainer_home'),
      path('logout_trainer',views.logout_trainer,name='logout_trainer')
]
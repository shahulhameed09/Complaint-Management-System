from django.urls import path
from app.views import auth_views, user_views, officer_views
from django.contrib.auth import views as auth_view
# from .views import PasswordsChangeView

urlpatterns = [
    path('', auth_views.logins, name="login"),
    path('logouts', auth_view.LogoutView.as_view(), name="logouts"),
    path('user_register', auth_views.user_register, name="user_register"),
    path('officer_register', auth_views.officer_register, name="officer_register"),
    
    # Officer's urls
    path('allComplaints',officer_views.allComplaints, name="allComplaints"),
    path('counter',officer_views.counter, name="counter"),
    path('solved',officer_views.solved, name="solved"),
    path('inProgress',officer_views.inProgress, name="inProgress"),
    path('pending',officer_views.pending, name="pending"),
    path('view_details/<ID>',officer_views.view_details, name="view_details"),
    path('reset_password',officer_views.PasswordsChangeView.as_view(template_name='Officer/reset_password.html')),
    path('officer_profile', officer_views.officer_profile, name="officer_profile" ),
    path('update_officer_profile', officer_views.update_officer_profiles, name="update_officer_profile" ),

    # User's urls
    path('user_home',user_views.home, name="user_home"),
    path('my_profile', user_views.my_profile, name="my_profile" ),
    path('update_profile', user_views.update_profiles, name="update_profile" ),
    path('contact_us', user_views.contact_us, name="contact_us" ),
    path('user_reset_password',user_views.PasswordsChangeView.as_view(template_name='Users/reset_password.html')),
    path('view_status', user_views.view_status, name="view_status"),
    path('view_complaint/<ID>', user_views.view_complaint, name="view_complaint"),
    path('delete_complaint/<ID>', user_views.delete_complaint, name="delete_complaint"),
    
]

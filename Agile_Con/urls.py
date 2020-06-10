from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('presenters/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('presenters/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('accounts/login/presenter_landing/', views.presenter_landing, name="presenter_landing"),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('attendees_list/', views.attendees_list, name='attendees_list'),
    path('', views.customer_order_list, name='customer_order_list'),
    path('customer_order_list', views.customer_order_list, name='customer_order_list'),
    path('customer_order/<int:pk>/edit/', views.customer_order_edit, name='customer_order_edit'),
    path('customer_order/<int:pk>/delete/', views.customer_order_delete, name='customer_order_delete'),
    path('about/', views.about, name="about"),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('presentations/', views.presentations, name="presentations"),
    path('accounts/login/attendee_landing/', views.attendee_landing, name="attendee_landing"),
    path('accounts/login/login_landing/', views.login_landing, name='login_landing'),

]
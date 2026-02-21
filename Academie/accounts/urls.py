from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register_page'),
    path('login/', views.LoginView.as_view(), name='login_page'),
    path('logout/', views.LogoutView.as_view(), name='logout_page'),
    path('activate/<str:code>/', views.ActivateAccountView.as_view(), name='activate_account'),
    path('user-panel/', views.UserPanelView.as_view(), name='user_panel'),
]
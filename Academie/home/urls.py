from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('consulting/', views.ConsultationView.as_view(), name='consultation'),
    path('cooperation/', views.CooperationView.as_view(), name='cooperation'),
    path('question/', views.QuestionView.as_view(), name='question'),
    path('Request-for-advice/', views.RequestForAdviceView.as_view(), name='Request_for_advice'),
]
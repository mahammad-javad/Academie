from django.urls import path
from . import views

urlpatterns = [
    path('', views.SkillsRoadmapView.as_view(), name='roadmap_page'),
]
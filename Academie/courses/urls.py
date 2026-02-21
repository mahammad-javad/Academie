from django.urls import path
from . import views

urlpatterns = [
    path('', views.CourseListView.as_view(), name='list_course'),
    path('course/request/<int:course_id>/', views.request_course_view, name='request_course'),
    path('<slug:slug>/', views.CourseDetailView.as_view(), name='course_detail'),
]
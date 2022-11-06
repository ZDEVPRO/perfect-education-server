from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('course-detail/<int:id>/', views.course_detail, name='course-detail'),
    path('teachers/', views.teachers, name='teachers'),
    path('teacher-detail/<int:id>/', views.teacher_detail, name='teacher-detail'),
    path('results/', views.results, name='results'),
    path('enroll-course/<int:id>/', views.enroll_course, name='enroll-course'),
    path('contact/', views.contact, name='contact'),
]


from django.urls import path
from quiz import views

app_name = 'quiz'
urlpatterns = [
    path('', views.index, name='section'),
    path('<int:id>/',views.subsection_detail, name='subsection_detail'),
    path('subsection/<int:id>/', views.headquiz_detail, name='headquiz_detail'),
     path('question/<int:id>/', views.question_view, name='question_view'),
     path('dashboard/',views.dashboard, name='dashboard')
    
]

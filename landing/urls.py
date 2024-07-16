from django.urls import path
from landing import views

app_name = 'landing'
urlpatterns = [
    path('', views.index, name='index'),
    
    # path('<int:id>/',views.subsection_detail, name='subsection_detail'),
    # path('subsection/<int:id>/', views.headquiz_detail, name='headquiz_detail'),
    #  path('question/<int:id>/', views.question_view, name='question_view'),
    
]

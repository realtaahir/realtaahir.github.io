# users/urls.py

from django.urls import path
from .views import signup_view, login_view, logout_view, CustomPasswordResetView ,profile_view


app_name = 'users'
urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
]
# users/urls.py

urlpatterns += [
    path('profile/', profile_view, name='profile'),
]


#  This will use for real password reset
# from django.urls import path
# from django.contrib.auth import views as auth_views
# from .views import CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView

# app_name = 'users'

# urlpatterns += [
#     path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
#     path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
#     path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
# ]

from django.urls import path
from .views import CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView

app_name = 'users'

urlpatterns += [
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

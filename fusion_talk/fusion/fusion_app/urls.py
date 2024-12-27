from django.urls import path
from .views import RegisterUserView, LoginUserView, LogoutUserView, GetUserProfileView, UpdateUserProfileView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('logout/', LogoutUserView.as_view(), name='logout_user'),
    path('profile/', GetUserProfileView.as_view(), name='get_user_profile'),
    path('profile/update/', UpdateUserProfileView.as_view(), name='update_user_profile'),
]

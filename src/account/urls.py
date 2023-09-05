from django.urls import path

from src.account.views import GetTokenAccount, RegistrationView, LoginView, LogoutView

urlpatterns = [
    path('telegram-token/', GetTokenAccount.as_view()),
    path('register/', RegistrationView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]
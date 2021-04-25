from django.urls import path
from . import views

app_name = 'banking'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('transfer/', views.TransferView.as_view(), name = 'transfer'),
    path( 'history/', views.HistoryView.as_view(), name = 'history'),
    path( 'sign-in/', views.SignInView.as_view(), name = 'sign-in'),
    path('dashboard/', views.DashboardView.as_view(), name = 'dahsboard'),
    path('log-out/', views.LogoutView, name = 'logout'),
    path('search/', views.HistorySearchView.as_view(), name = 'search'),
    path('verify-with-otp/<reqID>/', views.verifyView.as_view(), name = 'verify'),
    path('verify-with-otp/', views.verifyView.as_view(), name = 'verify_'),
]

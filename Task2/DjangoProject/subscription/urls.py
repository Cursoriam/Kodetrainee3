from django.urls import path
    
from .views import SubscriptionView

app_name = "subscriptions"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('subscriptions/', SubscriptionView.as_view()),
    path('subscriptions/email=<str:email>&ticker=<str:ticker>/', SubscriptionView.as_view()),
]    
from django.urls import path,include
from ml.api import views

urlpatterns = [
    path('lists/', views.paymentLists.as_view(), name='payment-lists'),
    path('predict/', views.PredictView.as_view(), name='predict'),
]

from django.urls import path
from .views import *

urlpatterns = [
    path('menu/',MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>',MenuDetailView.as_view(), name='menu-item')
    # path('booking',BookingView.as_view(), name='booking')
]
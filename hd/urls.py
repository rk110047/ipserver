from django.urls import path
from .views import Hd_Plus_AuthAPIView,HdPlusSubscriptionAPIView

urlpatterns=[
	path('auth/',Hd_Plus_AuthAPIView.as_view(),name="OTT Password Validation API"),
	path('subscription-create/',HdPlusSubscriptionAPIView.as_view(),name="Hd Plus Subscription Create")
]
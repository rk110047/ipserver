from django.urls import path
from .views import Hd_Plus_AuthAPIView,HdPlusSubscriptionAPIView,OTT_password_genAPIView

urlpatterns=[
	path('auth/',Hd_Plus_AuthAPIView.as_view(),name="OTT Password Validation API"),
	path('subscription-create/',HdPlusSubscriptionAPIView.as_view(),name="Hd Plus Subscription Create"),
	path('ott_generator/',OTT_password_genAPIView.as_view(),name="ott password generator")
]
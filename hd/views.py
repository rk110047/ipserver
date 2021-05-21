from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .models import HdPlusSubscription,HdRegistration
from .serializers import Hd_Plus_Authentication_serializer,HdPlusSubscriptionSerializer
# Create your views here.



class Hd_Plus_AuthAPIView(generics.GenericAPIView):
	serializer_class 		=		Hd_Plus_Authentication_serializer


	def post(self,request):
		hd_plus_number 	=	request.POST['hd_plus_number']
		hd_plus 		=	HdRegistration.objects.get_or_create(hd_plus_number=hd_plus_number)
		hd_plus_account = 	HdRegistration.objects.get(hd_plus_number=hd_plus_number)
		if hd_plus_account.mobile_number:
			response 	=	{
				"mobile_number":True
			}
			return Response(response)
		response 		=	{
			"mobile_number":False	
			}
		return Response(response)


class HdPlusSubscriptionAPIView(generics.CreateAPIView):
	serializer_class 		=	HdPlusSubscriptionSerializer
	queryset 				=	HdPlusSubscription.objects.all()
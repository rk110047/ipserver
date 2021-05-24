from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .models import HdPlusSubscription,HdRegistration
from .serializers import Hd_Plus_Authentication_serializer,HdPlusSubscriptionSerializer
from authentication.models import (
     User , BlackList, UserProfile, UserDevices
)
# from django.contrib.auth import get_user_model
# Create your views here.

#hmac
import hmac
import hashlib
from random import randrange


# User  = get_user_model()


class Hd_Plus_AuthAPIView(generics.GenericAPIView):
	serializer_class 		=		Hd_Plus_Authentication_serializer


	def post(self,request):

		hd_plus_number 	=	request.POST['hd_plus_number']
		ott_password 	= 	request.POST['ott_password']

		if len(hd_plus_number)==12 and len(ott_password)==8:

			hd_number = hd_plus_number

			keys =	("3F0A034741030D04420EC4A0DC931EAE1001546388BDE1CF48A5E1EDB0F2CFD2C1684F6F826235B3CFDCFDF452DC1394022E13B382A39570C5B7C3F93028851C",
			"DB8DCA853E8DBCFCFFD11AD62A90AFCE61F6B5F18E85725366032CD9838CEA90FB83C27B1B569A0BE8EE3638A27F71E1375525FF93220661A99346F3C7387371",
			"8E08311705AA03DBAC29862B96C102EF189A3537C101144D29C2B5A69A736D55952F66600C090B7E3C0F468B33E0D759D9C2C27F71A41264B835FEDB162B813B")

			key_out_number = ott_password[0] 
			key = keys[int(ott_password[0]) - 1]
			key = key.encode('utf-8')
			dig = hmac.new(key=key, msg=hd_number.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()
			password = str(int(dig , 16) % 10**7)

			if len(password)==7:
				hd_ott_password = str(key_out_number) + str(password)
				if ott_password == hd_ott_password:
					hd_plus 		=	HdRegistration.objects.get_or_create(hd_plus_number=hd_plus_number)
					print(hd_plus_number)
					user 	=	User.objects.get_or_create(username=hd_plus_number)
					user 	=	User.objects.get(username=hd_plus_number)
					return Response({"message":"OTT Access granted","status":200,"token":user.token})
				else:
					return Response({"message":"OTT Access denied","status":401})

			else:
				zero = 7 - len(password)
				hd_ott_password = (zero * "0") + str(password)
				hd_ott_password = str(key_out_number) + str(hd_ott_password)
				if ott_password == hd_ott_password:
					hd_plus 		=	HdRegistration.objects.get_or_create(hd_plus_number=hd_plus_number)
					print(hd_plus_number)
					user 	=	User.objects.get_or_create(username=hd_plus_number)
					user 	=	User.objects.get(username=hd_plus_number)
					return Response({"message":"OTT Access granted","status":200,"token":user.token})
				else:
					return Response({"message":"OTT Access denied","status":401})

			# hd_plus 		=	HdRegistration.objects.get_or_create(hd_plus_number=hd_plus_number)
			# hd_plus_account = 	HdRegistration.objects.get(hd_plus_number=hd_plus_number)
			# if hd_plus_account.mobile_number:
			# 	response 	=	{
			# 		"mobile_number":True
			# 	}
			# 	return Response(response)
			# response 		=	{
			# 	"mobile_number":False	
			# 	}
			# return Response(response)
		return Response({"message":"incorrect HD Number or OTT Password","status":406})


class HdPlusSubscriptionAPIView(generics.CreateAPIView):
	serializer_class 		=	HdPlusSubscriptionSerializer
	queryset 				=	HdPlusSubscription.objects.all()




class OTT_password_genAPIView(generics.GenericAPIView):
	def get(self,request):
		hd_plus_number 		=	self.request.GET.get("hd_plus_number")

		if len(hd_plus_number)==12:

			hd_number = hd_plus_number

			keys =	("3F0A034741030D04420EC4A0DC931EAE1001546388BDE1CF48A5E1EDB0F2CFD2C1684F6F826235B3CFDCFDF452DC1394022E13B382A39570C5B7C3F93028851C",
			"DB8DCA853E8DBCFCFFD11AD62A90AFCE61F6B5F18E85725366032CD9838CEA90FB83C27B1B569A0BE8EE3638A27F71E1375525FF93220661A99346F3C7387371",
			"8E08311705AA03DBAC29862B96C102EF189A3537C101144D29C2B5A69A736D55952F66600C090B7E3C0F468B33E0D759D9C2C27F71A41264B835FEDB162B813B")

			key_number = randrange(3)
			key_out_number = key_number + 1
			key = keys[key_number]
			key = key.encode('utf-8')
			dig = hmac.new(key=key, msg=hd_number.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()
			password = str(int(dig , 16) % 10**7)
			if len(password)==7:
				ott_password = str(key_out_number) + str(password)
				return Response({
							"hd_plus_number":hd_plus_number,
							"ott_password":ott_password})

			else:
				zero = 7 - len(password)
				ott_password = (zero * "0") + str(password)
				ott_password = str(key_out_number) + str(ott_password)
				return Response({
							"hd_plus_number":hd_plus_number,
							"ott_password":ott_password})

		return Response({"message":"hd+ number invalid"})
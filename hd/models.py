from django.db import models

# Create your models here.
class HdRegistration(models.Model):
	hd_plus_number 		=		models.CharField(max_length=120,unique=True)
	mobile_number 		=		models.CharField(max_length=120,unique=True,blank=True,null=True)

	def __str__(self):
		return self.hd_plus_number

class OtpVerification(models.Model):
	mobile_number 		=		models.CharField(max_length=120,unique=True,blank=True,null=True)
	otp 				=		models.CharField(max_length=120,blank=True,null=True)

	def __str__(self):
		return self.mobile_number

class HdPlusSubscription(models.Model):
	choices 	=	(("YES","yes"),("NO","no"))
	hd_plus_number 		=		models.CharField(max_length=120,unique=True)
	start_date			=		models.DateField()
	longer_valid 		=		models.DateField()
	DTH_HD_Subscription =		models.CharField(choices=choices,max_length=120)


	def __str__(self):
		return self.hd_plus_number

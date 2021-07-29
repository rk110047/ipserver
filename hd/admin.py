from django.contrib import admin
from .models import HdPlusSubscription,HdRegistration,OtpVerification

# Register your models here.


admin.site.register(HdPlusSubscription)
admin.site.register(HdRegistration)
admin.site.register(OtpVerification)

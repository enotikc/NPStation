# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
#from zinnia.models import Entry
#from zinnia.admin.entry import EntryAdmin

#-------------------API---------------------------------------------------------
class UserProfile(models.Model):
	user = models.ForeignKey( User, null = True )
	you_session = models.CharField(max_length=512)
	api_key = models.CharField(max_length=512)

	def user_post_save(sender, instance, **kwargs):
		( profile, new ) = UserProfile.objects.get_or_create(user=instance)

		
def user_post_save(sender, instance, **kwargs):
		( profile, new ) = UserProfile.objects.get_or_create(user=instance)

models.signals.post_save.connect(user_post_save, sender=User)


#----------------------END-API-------------------------------------------------
	
class PasswordType(models.Model): #Пароли вводимые с устройства
	email = models.CharField(max_length=60)
	for_date = models.DateField()
	url_site = models.CharField(max_length=120)

	def __unicode__(self):
		return self.email

class ClientStatus(models.Model): #Статус устройств
	user = models.ForeignKey( User, null = True )
	model = models.CharField(max_length=50)
	alarm = models.BooleanField(default=False)
	warning = models.BooleanField(default=False)
	blocking = models.BooleanField(default=False)
	privacy = models.BooleanField(default=False)
	search_status = models.BooleanField(default=False)
	monitor_status = models.BooleanField(default=False)
	
	def __unicode__(self, request):
		return self.name


class Device(models.Model): #Здесь хранятся все устройства
	user = models.ForeignKey(User, null = True)
	model = models.CharField(max_length=50)
	imei = models.CharField(max_length=18)
	phone_number = models.CharField(max_length=32)
	mac = models.CharField(max_length=20)
	usbidcode = models.CharField(max_length=30)
	latitude = models.CharField(max_length=50)
	longitude = models.CharField(max_length=50)
	height = models.CharField(max_length=50)
	cell_id = models.BooleanField(default=False)
	ip_info = models.CharField(max_length=128)
	wifi_info = models.CharField(max_length=512)
	battery_info = models.CharField(max_length=128)
	webcam_picture = models.CharField(max_length=128)
	
	def __unicode__(self, request):
		return self.name
		
class CellId(models.Model): #Координаты устройств от вышек
	user = models.ForeignKey( User, null = True )
	model = models.CharField(max_length=50)
	mcc = models.BigIntegerField(default=0)
	mnc = models.BigIntegerField(default=0)
	lac = models.IntegerField(default=0)
	cid = models.IntegerField(default=0)
	
	def __unicode__(self, request):
		return self.name
	
class Research(models.Model): #
	user = models.ForeignKey( User, null = True )
	geo_info = models.BooleanField(default=False)
	wifi_info = models.BooleanField(default=False)
	webcam = models.BooleanField(default=False)
	
	def __unicode__(self, request):
		return self.name
		
class Action(models.Model): #Действия над устройством с терминала
	user = models.ForeignKey( User, null = True )
	alarm = models.BooleanField(default=False)
	warning = models.BooleanField(default=False)
	blocking = models.BooleanField(default=False)
	privacy = models.BooleanField(default=False)
	
	def __unicode__(self, request):
		return self.name
	
class Report(models.Model): #Отчеты по которым можно получать данные
	user = models.ForeignKey( User, null = True )
	all = models.BooleanField(default=False)
	report_text = models.TextField()
	
	def __unicode__(self, request):
		return self.name
	
class OS(models.Model):
	name_os = models.CharField(max_length=128)
	version = models.CharField(max_length=128)
	core = models.CharField(max_length=128)
	
	def __unicode__(self, request):
		return self.name_os
		
class SmsCommands(models.Model):
	user = models.ForeignKey( User, null = True )
	status = models.BooleanField(default=False)
	alarm = models.BooleanField(default=False)
	message = models.BooleanField(default=False)
	sound_on = models.BooleanField(default=False)
	sound_off = models.BooleanField(default=False)
	speak = models.BooleanField(default=False)
	data_start = models.BooleanField(default=False)
	data_stop = models.BooleanField(default=False)
	wifi_start = models.BooleanField(default=False)
	wifi_stop = models.BooleanField(default=False)
	call = models.BooleanField(default=False)
	hangup = models.BooleanField(default=False)
	recordsound = models.BooleanField(default=False)
	apn_copy = models.BooleanField(default=False)
	apn_remove = models.BooleanField(default=False)
	apn_enable = models.BooleanField(default=False)
	apn_disable = models.BooleanField(default=False)
	gps_on = models.BooleanField(default=False)
	block = models.BooleanField(default=False)
	unblock = models.BooleanField(default=False)
	startapp = models.BooleanField(default=False)
	erasesdcard = models.BooleanField(default=False)
	wipe = models.BooleanField(default=False)
	
	def __unicode__(self, request):
		return self.name
		
# class MobileClient(models.Model):
	# os_support = models.CharField(max_length=512)
	# version = models.CharField(max_length=128)
	# url_for_installer = models.CharField(max_length=512)
	# installer = models.FileField()
	
import datetime
	
class UpdateDevice(models.Model): #Хранение последних трех координат устройства
	model = models.CharField(max_length=50)
	imei = models.CharField(max_length=18)
	date1 = models.DateTimeField(default=datetime.date.today(), blank=True)
	latitude1 = models.CharField(max_length=50)
	longitude1 = models.CharField(max_length=50)
	height1 = models.CharField(max_length=50)
	date2 = models.DateTimeField(default=datetime.date.today(), blank=True)
	latitude2 = models.CharField(max_length=50)
	longitude2 = models.CharField(max_length=50)
	height2 = models.CharField(max_length=50)
	date3 = models.DateTimeField(default=datetime.date.today(), blank=True)
	latitude3 = models.CharField(max_length=50)
	longitude3 = models.CharField(max_length=50)
	height3 = models.CharField(max_length=50)
	
	def __unicode__(self, request):
		return self.model
	
#-----------------------------------------------
		
# class Task(models.Model):
	# user = models.ForeignKey( User, null = True )
	# status = models.BooleanField(default=False)
	# task = models.CharField(max_length=512)
	# term = models.DateField(blank=True, null=True)
	# cost = models.BigIntegerField(default=0)
	# karma = models.IntegerField(default=0)
	

# -*- coding: utf-8 -*-
from django.db import models
from settings import *

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length = 80,verbose_name='Заголовок')
    desc  = models.TextField(verbose_name='Описание')
    
    def __unicode__(self):
	return self.title
    class Meta:
        verbose_name = "Новости сайта"
        verbose_name_plural ="Новости сайта"



#-------------------------
class Directions(models.Model):
    title = models.CharField(max_length = 80,verbose_name='Название')
    desc  = models.TextField(verbose_name='Описание')
    city  = models.CharField(max_length = 30,blank=True,verbose_name='Город')
    
    def __unicode__(self):
	return self.title

    class Meta:
        verbose_name = "Направления"
        verbose_name_plural ="Направления"


#------------------------
class Services(models.Model):
    title = models.CharField(max_length = 80,verbose_name='Название')
    SEASON_CHOICES = (
        ('w','зима'),
	('s','весна'),
	('sm','лето'),
	('a','осень'),        
    )
    CURRENCY_CHOICES = (
        ('grn',u'гривен'),
        ('usd',u'долларов'),
        ('euro',u'евро'),
    )
    LNG_CHOICES = (
        ('rus','русский'),
        ('ukr','украинский'),
        ('eng','английский'),
    )
    season = models.CharField(max_length=2, choices=SEASON_CHOICES,verbose_name='Время года')
    direct = models.ManyToManyField(Directions)
    lng = models.CharField(max_length=3, choices=LNG_CHOICES,verbose_name='Язык')
    desc  = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2,blank=True,null=True,verbose_name='Цена')
    currency =  models.CharField(max_length=4, choices=CURRENCY_CHOICES,blank=True,verbose_name='валюта')
    date_out = models.DateField(blank=True,null=True,verbose_name='Выезд')
    date_in  = models.DateField(blank=True,null=True,verbose_name='Прибытие')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Программы лагеря"
        verbose_name_plural ="Программы лагеря"

#------------------------
class Vogatie(models.Model):
    name  = models.CharField(max_length = 80,verbose_name='Имя')
    desc  = models.TextField(verbose_name='Описание')
    email = models.EmailField(blank=True,verbose_name='e-mail')
    foto = models.ImageField(upload_to=MEDIA_ROOT,blank=True,verbose_name='Фото')

    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = "Вожатые"
        verbose_name_plural ="Вожатые"
#----------------------------
class Info(models.Model):
    INFO_CHOICES = (
        ('line',u'Бегущая строка'),
        ('contacts',u'Контакты'),
        ('parents',u'Информация Родителям'),
        ('common',u'Информация Общая'),
    )
    tp = models.CharField(max_length=10, choices=INFO_CHOICES,verbose_name='Тип')
    name = models.CharField(max_length = 80,verbose_name='Имя')
    desc = models.TextField(verbose_name='Описание')
    
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = "Информационные листы"
        verbose_name_plural ="Информационные листы"
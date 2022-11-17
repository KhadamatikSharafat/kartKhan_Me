from django.db import models
from django.utils.translation import ugettext_lazy as _

from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget

# Create your models here.

class login(models.Model):
    codeMeli = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=30)

    class Meta:
        db_table = 'web_login'
        verbose_name = _('کاربر')
        verbose_name_plural = _('کاربران')

    def __str__(self):
        return self.codeMeli

class register(models.Model):
    name = models.CharField(_('نام'), max_length=20)
    family = models.CharField(_('نام خانوادگی'), max_length=25)
    fatherName = models.CharField(_('نام پدر'), max_length=20)
    birthday = models.DateField(_('تاریخ تولد'))
    codeMeli = models.ForeignKey(login,verbose_name=_('کدملی'), on_delete=models.CASCADE, to_field='codeMeli')
    serialMeli = models.CharField(_('سریال پشت کارت ملی'), max_length=10, blank=True)
    shomareSh = models.CharField(_('شماره شناسنامه/کدثبتی'),max_length=10)
    serialSh = models.CharField(_('سریال شناسنامه'),max_length=6)
    seriSh = models.CharField(_('سری شناسنامه'),max_length=3)
    sadereh = models.CharField(_('صادره از/ثبت شده در'),max_length=50)
    ostan = models.CharField(_('استان'),max_length=50)
    shahr = models.CharField(_('شهر'),max_length=50)
    neshaniShop = models.CharField(_('نشانی فروشگاه/شرکت'),max_length=300)
    codePosti = models.CharField(_('کدپستی محل نصب'),max_length=10)
    telephonShop = models.CharField(_('تلفن فروشگاه'),max_length=8)
    shomareParvane = models.CharField(_('شماره پروانه کسب/شماره صنفی اجاره نامه'),max_length=50)
    codeRehgiri = models.CharField(_('کد رهگیری مالیاتی'),max_length=50)
    senf = models.CharField(_('صنف'),max_length=25)
    teleHamrah = models.CharField(_('تلفن همراه'),max_length=11)
    bestarType = [
        ('Dialup', 'Dialup Type'),
        ('GPRS', 'GPRS Type'),
        ('Combo', 'Combo Type'),
        ('WIFI', 'WIFI Type'),
    ]
    bestareErtebat = models.CharField(_('بستر ارتباطی'),max_length=6, choices=bestarType, default='Dialup') #Dialup, GPRS, Combo, WIFI
    malekType = [
        ('ملکی', 'نوع ملکی'),
        ('سرقفلی', 'نوع سرقفلی'),
        ('استیجاری', 'نوع استیجاری'),
    ]
    malekiyat = models.CharField(_('نوع مالکیت محل نصب'),max_length=8, choices=malekType, default='ملکی') #ملکی، سرقفلی، استیجاری
    mohlateEjareFrom =  models.DateField(_('مهلت اجاره نامه از تاریخ'), blank=True)
    mohlateEjareTo = models.DateField(_('مهلت اجاره نامه تا تاریخ'), blank=True)
    nameMoaref = models.CharField(_('نام معرف اول'),max_length=20)
    familyMoaref = models.CharField(_('نام خانوادگی معرف اول'),max_length=25)
    telMoaref = models.CharField(_('تلفن همراه معرف اول'),max_length=11)
    neshaniMoaref = models.CharField(_('نشانی محل سکونت معرف اول'),max_length=300)
    shomareHesab = models.CharField(_('شماره حساب اول'),max_length=20)
    nameBank = models.CharField(_('نام بانک اول'),max_length=50)
    shomareShaba = models.CharField(_('شماره شبا اول'),max_length=16)
    shomareHesabTow = models.CharField(_('شماره حساب دوم'),max_length=20)
    nameBankTwo = models.CharField(_('نام بانک دوم'),max_length=50)
    shomareShabaTwo = models.CharField(_('شماره شبا دوم'),max_length=16)
    paziresh = models.BooleanField(_('تایید اطلاعات'),default=False)
    javazKasb = models.FileField(_('جواز کسب'), upload_to='registerDouc/%Y/%m/%d/')
    ejarehName = models.FileField(_('اجاره نامه'), upload_to='registerDouc/%Y/%m/%d/', blank=True)
    sanadMalek = models.FileField(_('سند مالکیت'), upload_to='registerDouc/%Y/%m/%d/', blank=True)
    tsvirShenasnameh = models.FileField(_('تصویر دو صفحه اول شناسنامه'), upload_to='registerDouc/%Y/%m/%d/')
    rooyeCartmeli = models.FileField(_('تصویر رو کارت ملی'), upload_to='registerDouc/%Y/%m/%d/')
    poshtCartmeli = models.FileField(_('تصویر پشت کارت ملی'), upload_to='registerDouc/%Y/%m/%d/')
    tsvirEmzaMohr = models.FileField(_('تصویر مهر و امضا'), upload_to='registerDouc/%Y/%m/%d/')
    sabinFormFirst = models.FileField(_('تصویر صفحه اول فرم سابین'), upload_to='registerDouc/%Y/%m/%d/')
    sabinFormTwo = models.FileField(_('تصویر صفحه دوم فرم سابین'), upload_to='registerDouc/%Y/%m/%d/')

    # Fields outside the form
    nameFamilyKarshenas = models.CharField(_('نام کارشناس'),max_length=100,default="کارشناس پذیرش")
    cerated_time = models.DateTimeField(_('زمان ثبت درخواست'), auto_now_add=True)
    updated_time = models.DateTimeField(_('زمان بروزرسانی '), auto_now=True)
    status_type = [
        ('در انتظار بررسی ', 'در انتظار بررسی'),
        ('مشاهده درخواست', 'مشاهده درخواست'),
        ('درحال بررسی', 'درحال بررسی'),
        ('موافقت با درخواست', 'موافقت با درخواست'),
        ('رد درخواست', 'رد درخواست'),
        ('در حال صدور', 'در حال صدور'),
        ('تکمیل شده', 'تکمیل شده'),
    ]
    status = models.CharField(_('وضعیت'), max_length=60, choices=status_type, default='در انتظار بررسی', blank=True)

    class Meta:
        db_table = 'web_register'
        verbose_name = _('درخواست کارتخوان')
        verbose_name_plural = _('درخواست های کارتخوان')

    def __str__(self):
        return  _('درخواست') + self.codeMeli
from django.db import models




class SiteInfo(models.Model):
    name = models.CharField(max_length=100, default="DEVIO",verbose_name="اسم سایت")
    tagline = models.CharField(max_length=255, blank=True,verbose_name=' توضیح کوتاه')
    about_text = models.TextField(blank=True,verbose_name='درباره ما')
    goals_text = models.TextField(blank=True,verbose_name='اهداف آکادمی')
    logo = models.FileField(upload_to='site/logo/', blank=True, null=True,verbose_name='لوگو سایت')
    favicon = models.FileField(upload_to='site/icon/', blank=True, null=True,verbose_name='آیکون سایت')
    facebook = models.URLField(blank=True,null=True,verbose_name='ادرس فیسبوک')
    instagram = models.URLField(blank=True,null=True,verbose_name='ادرس اینستاگرام')
    linkedin = models.URLField(blank=True,null=True,verbose_name='ادرس لینکدین')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ساخت')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='تاریخ آپدیت')
    hero_video = models.FileField(upload_to='site/videos/',blank=True,null=True,help_text='ویدیوی پس‌زمینه صفحه اصلی (mp4)')
    email = models.EmailField(default='sudowebsite@gmail.com',verbose_name='ایمیل')
    number = models.CharField(default='09337480645',verbose_name='تلفن')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'اطلاعات سایت'
        verbose_name_plural = 'اطلاعات سایت'


class Activity(models.Model):
    site = models.ForeignKey(SiteInfo,verbose_name='اطلاعات سایت', on_delete=models.CASCADE, related_name='activities')
    description = models.TextField(blank=True, verbose_name='توضیحات')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')

    def __str__(self):
        return self.description


    class Meta:
        verbose_name = 'هدف'
        verbose_name_plural = 'اهداف'

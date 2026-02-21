from django.contrib import admin

from home.models import SiteInfo,Activity


# Register your models here.


@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ['name']



@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['description']
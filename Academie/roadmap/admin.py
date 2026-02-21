from django.contrib import admin

from roadmap.models import Job,Skill,SkillLevel


# Register your models here.


@admin.register(SkillLevel)
class SkillLevelAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['name','description']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['title','description',]

    filter_horizontal = ('jobs',)
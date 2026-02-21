from django.db import models
from django.utils.text import slugify


# شاخه اصلی شغلی
class Job(models.Model):
    name = models.CharField("عنوان شغل", max_length=100)
    description = models.TextField("توضیح شغل", blank=True)
    icon_class = models.CharField("آیکون (کلاس FontAwesome)", max_length=50, blank=True)


    class Meta:
        verbose_name = "شاخه شغلی"
        verbose_name_plural = "شاخه‌های شغلی"

    def __str__(self):
        return self.name


class SkillLevel(models.Model):
    LEVEL_CHOICES = [
        ("beginner", "مقدماتی"),
        ("intermediate", "متوسط"),
        ("advanced", "پیشرفته"),
    ]
    name = models.CharField("نام سطح", max_length=20, choices=LEVEL_CHOICES, unique=True)

    class Meta:
        verbose_name = "سطح مهارت"
        verbose_name_plural = "سطوح مهارت"

    def __str__(self):
        return self.get_name_display()


# مهارت‌ها
class Skill(models.Model):
    jobs = models.ManyToManyField(Job, verbose_name="شغل‌های مرتبط", related_name="skills")
    title = models.CharField("عنوان مهارت", max_length=100)
    level = models.ForeignKey(SkillLevel,blank=True,null=True, on_delete=models.CASCADE, verbose_name="سطح", related_name="skills")
    tag = models.CharField("تگ", max_length=50, blank=True)
    description = models.TextField("توضیح کوتاه")
    duration_hours = models.CharField("مدت زمان یادگیری", max_length=100)
    level_value = models.PositiveIntegerField(
        "سطح مهارت (0 تا 100)",
        default=0,
        help_text="عدد بین 0 تا 100 برای تعیین سطح مهارت"
    )
    icon_class = models.CharField("آیکون (کلاس FontAwesome)", max_length=50, blank=True)

    class Meta:
        verbose_name = "مهارت"
        verbose_name_plural = "مهارت‌ها"

    def __str__(self):
        return self.title

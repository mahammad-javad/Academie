from django.db import models
from accounts.models import User
from django.utils.text import slugify




class Course(models.Model):

    STATUS_CHOICES = (('REGISTRATION', 'در حال ثبت‌نام'),('ONGOING', 'در حال برگزاری'),('FINISHED', 'پایان یافته'),)
    title = models.CharField(max_length=200,verbose_name='عنوان دوره')
    slug = models.SlugField(max_length=220,unique=True,blank=True,verbose_name='اسلاگ')
    short_description = models.CharField(max_length=300,verbose_name='توضیح کوتاه')
    description = models.TextField(verbose_name='توضیحات کامل')
    teacher = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,limit_choices_to={'role': 'TEACHER'},related_name='courses',verbose_name='مدرس')
    start_date = models.DateField(verbose_name='تاریخ شروع')
    end_date = models.DateField(verbose_name='تاریخ اتمام', null=True, blank=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='REGISTRATION',verbose_name='وضعیت دوره')
    image = models.ImageField(upload_to='courses/images/',null=True,blank=True,verbose_name='تصویر دوره')
    capacity = models.PositiveIntegerField(null=True,blank=True,verbose_name='ظرفیت دوره')
    requirements = models.TextField(blank=True,null=True, verbose_name="پیش نیازهای دوره")
    skills_after = models.TextField(blank=True,null=True, verbose_name="مهارت‌های بعد از دوره")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')


    class Meta:
        verbose_name = 'دوره'
        verbose_name_plural = 'دوره‌ها'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)



class CourseRequest(models.Model):
    user = models.ForeignKey(User,verbose_name='کاربر', on_delete=models.CASCADE, related_name='course_requests')
    course = models.ForeignKey(Course,verbose_name='دوره', on_delete=models.CASCADE, related_name='course_requests')
    status = models.CharField(
        verbose_name='وضعیت',
        max_length=10,
        choices=[('PENDING','در انتظار تایید'), ('APPROVED','تایید شده'), ('REJECTED','رد شده')],
        default='PENDING'
    )
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='زمان درخواست')

    def __str__(self):
        return f'{self.user} {self.course} {self.status}'


    class Meta:
        verbose_name ='درخواست'
        verbose_name_plural = 'درخواست ها'



class CourseEnrollment(models.Model):
    user = models.ForeignKey(User, verbose_name='کاربر', on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, verbose_name='دوره', on_delete=models.CASCADE, related_name='enrollments')
    payment_proof = models.ImageField(upload_to='payment_proofs/', null=True, blank=True, verbose_name='فیش واریزی')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان ثبت نام نهایی')

    class Meta:
        verbose_name = 'شاگرد'
        verbose_name_plural = 'شاگردان'
        ordering = ['-created_at']
        unique_together = ('user', 'course')  # هر کاربر فقط یک ثبت نام نهایی برای هر دوره

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"
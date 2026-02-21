from django.contrib import admin
from courses.forms import CourseRequestAdminForm
from courses.models import Course, CourseRequest, CourseEnrollment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title','teacher']




@admin.register(CourseEnrollment)
class CourseEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'created_at')
    list_filter = ('course', 'created_at')
    verbose_name = 'شاگرد'
    verbose_name_plural = 'شاگردان'




@admin.register(CourseRequest)
class CourseRequestAdmin(admin.ModelAdmin):
    form = CourseRequestAdminForm
    list_display = ['user', 'course', 'status', 'created_at']
    list_filter = ['status', 'course']

    def save_model(self, request, obj, form, change):
        # بررسی تغییر وضعیت به تایید شده
        is_new_approval = False
        if change:
            old_obj = CourseRequest.objects.get(pk=obj.pk)
            if old_obj.status != 'APPROVED' and obj.status == 'APPROVED':
                is_new_approval = True

        super().save_model(request, obj, form, change)

        if is_new_approval:
            # ایجاد رکورد Enrollment
            enrollment, created = CourseEnrollment.objects.get_or_create(
                user=obj.user,
                course=obj.course
            )
            # اگر ادمین فیش آپلود کرده، ذخیره کن
            payment_proof = form.cleaned_data.get('payment_proof')
            if payment_proof:
                enrollment.payment_proof = payment_proof
                enrollment.save()

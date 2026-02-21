from django import forms
from django.contrib import admin

from courses.models import CourseRequest


class CourseRequestAdminForm(forms.ModelForm):
    payment_proof = forms.ImageField(required=False, label="آپلود فیش واریزی")

    class Meta:
        model = CourseRequest
        fields = ['user', 'course', 'status', 'payment_proof']


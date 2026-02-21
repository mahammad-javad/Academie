from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from utils.email_utils import send_custom_email
from .models import Course, CourseRequest

# Create your views here.


class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'courses/list_courses.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = Course.objects.all()

        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)

        return queryset.order_by('-created_at')





@login_required(login_url='/accounts/login/')
def request_course_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    # بررسی اینکه کاربر قبلاً درخواست داده یا نه
    if CourseRequest.objects.filter(user=request.user, course=course).exists():
        messages.warning(request, 'شما از قبل داخل این دوره شرکت کرده‌اید.')
    else:
        # ایجاد درخواست جدید
        CourseRequest.objects.create(user=request.user, course=course)
        messages.success(request, 'درخواست شما با موفقیت ثبت شد. کارشناسان ما به زودی با شما تماس میگیرند.')

        # ارسال ایمیل اطلاع‌رسانی
        email_context = {
            'user': request.user,
            'course': course,
            'message': 'درخواست شما برای شرکت در دوره ثبت شد. لطفاً منتظر تماس کارشناسان ما باشید.'
        }
        send_custom_email(
            subject=f'ثبت درخواست دوره: {course.title}',
            to=request.user.email,
            context=email_context,
            template_name='emails/add_course.html'
        )

    # هدایت کاربر به همان صفحه دوره یا هر صفحه دیگر
    return redirect('course_detail', slug=course.slug)


class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'courses/detail_course.html'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     # ارسال ایمیل تستی هر بار که وارد DetailView می‌شویم
    #     send_custom_email(
    #         subject=f"شما وارد صفحه دوره {self.object.title} شدید",
    #         message=f"سلام! شما دوره {self.object.title} را مشاهده کردید.",
    #         recipient_list=['gharagozlooarman@gmail.com']
    #     )
    #
    #     return context

    # def get_object(self, queryset=None):
    #     # گرفتن شی Course
    #     obj = super().get_object(queryset)
    #
    #     # ایمیل تستی به یک کاربر ثابت
    #     try:
    #         user = User.objects.get(email='gharagozlooarman@gmail.com')
    #         send_custom_email(
    #             subject=f"شما در حال مشاهده دوره: {obj.title} هستید",
    #             to=user.email,
    #             context={'user': user, 'course': obj},
    #             template_name='emails/course_visit.html'
    #         )
    #     except User.DoesNotExist:
    #         pass  # اگه کاربر پیدا نشد، نادیده بگیر
    #
    #     return obj
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Job, Skill


class SkillsRoadmapView(TemplateView):
    template_name = "roadmap/index.html"  # مسیر تمپلیت شما

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # کشیدن همه شغل‌ها
        jobs = Job.objects.all().prefetch_related('skills')
        context['jobs'] = jobs

        # می‌تونیم همه مهارت‌ها رو هم جدا بکشیم اگر لازم بود
        skills = Skill.objects.all()
        context['skills'] = skills

        return context

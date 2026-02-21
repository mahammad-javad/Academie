from django.shortcuts import render
from django.views.generic import TemplateView

from home.models import SiteInfo


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        site_info= SiteInfo.objects.first()
        context['site_info'] = site_info

        activities = list(site_info.activities.all())

        columns = [
            activities[0::3],
            activities[1::3],
            activities[2::3],
        ]
        context['columns'] = columns
        return context


class ConsultationView(TemplateView):
    template_name = 'home/Consulting.html'


class CooperationView(TemplateView):
    template_name = 'home/cooperation.html'




class QuestionView(TemplateView):
    template_name = 'home/question.html'


class RequestForAdviceView(TemplateView):
    template_name = 'home/Request_for_advice.html'



def site_header_partial(request):
    context = {
        'site_info': SiteInfo.objects.all().first()
    }
    return render(request,'shared/site_header.html',context)



def site_footer_partial(request):
    context = {
        'site_info': SiteInfo.objects.all().first()
    }
    return render(request,'shared/site_footer.html',context)
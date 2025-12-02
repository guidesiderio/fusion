from django.views.generic import TemplateView
from .models import Service, TeamMember


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = super(IndexView, self).get_context_data(**kwargs)
        context["services"] = Service.objects.all()
        context["team_members"] = TeamMember.objects.all()
        return context

from django.views.generic import FormView
from .models import Service, TeamMember
from .forms import ContactForm
from django.urls import reverse_lazy
from django.contrib import messages


class IndexView(FormView):
    template_name = "index.html"
    form_class = ContactForm
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = super(IndexView, self).get_context_data(**kwargs)
        context["services"] = Service.objects.order_by("?").all()
        context["team_members"] = TeamMember.objects.order_by("?").all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_email()
        messages.success(self.request, "Your message has been sent successfully!")
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(
            self.request, "There was an error sending your message. Please try again."
        )
        return super(IndexView, self).form_invalid(form, *args, **kwargs)

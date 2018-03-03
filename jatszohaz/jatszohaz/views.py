import logging
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, RedirectView

from braces.views import PermissionRequiredMixin

from .forms import JhUserForm
from inventory.models import GameGroup
from .models import JhUser

logger = logging.getLogger(__name__)


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        if not self.request.user.is_anonymous:
            ctx['username'] = self.request.user.full_name2()
        return ctx


class CalendarView(TemplateView):
    template_name = "calendar.html"


class GamesView(ListView):
    model = GameGroup
    template_name = "games.html"
    ordering = "name"


class MyProfileView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = JhUser
    success_url = reverse_lazy('my-profile')
    success_message = _("Successfully updated!")
    form_class = JhUserForm
    template_name = "profile.html"

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        user = self.request.user
        user.checked_profile = True
        user.save()

        return super().form_valid(form)


class ProfileView(PermissionRequiredMixin, DetailView):
    model = JhUser
    template_name = "profile_detail.html"
    permission_required = 'jatszohaz.view_all'


class AboutUsView(TemplateView):
    template_name = "static_pages/about_us.html"


class FaqView(TemplateView):
    template_name = "static_pages/faq.html"


class AfterLoginView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if not self.request.user.checked_profile:
            messages.info(self.request, _("Please check your profile data and click the Update button!"))
            return reverse_lazy('my-profile')

        return reverse_lazy('home')

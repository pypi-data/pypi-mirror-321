from typing import Any

from django.views.generic.base import TemplateView
from edc_dashboard.utils import get_bootstrap_version
from edc_dashboard.view_mixins import EdcViewMixin
from edc_navbar import NavbarViewMixin

from ..admin_site import edc_consent_admin
from ..site_consents import site_consents


class HomeView(EdcViewMixin, NavbarViewMixin, TemplateView):
    template_name = f"edc_consent/bootstrap{get_bootstrap_version()}/home.html"
    navbar_name = "edc_consent"
    navbar_selected_item = "consent"

    def __init__(self, *args, **kwargs):
        super(HomeView, self).__init__(*args, **kwargs)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        kwargs.update(
            edc_consent_admin=edc_consent_admin,
            consent_definitions=site_consents.get_consent_definitions,
        )
        return super().get_context_data(**kwargs)

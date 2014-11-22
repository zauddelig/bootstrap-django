from django.views.generic.edit import FormView

from .forms import TestForm


class FormView(FormView):
    template_name = 'index.html'
    form_class = TestForm
    success_url = '/'
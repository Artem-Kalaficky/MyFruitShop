from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from bank.models import Bank
from fruits.models import Fruit, Log
from users.models import Message


class TestView(LoginView):
    template_name = 'users/index.html'

    def get_success_url(self):
        return reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['fruits'] = Fruit.objects.all()
        context['messages'] = Message.objects.all()
        context['bank'] = Bank.objects.first()
        context['logs'] = Log.objects.all()
        return self.render_to_response(context)


class UserLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'users/index.html'
    next_page = reverse_lazy('login')

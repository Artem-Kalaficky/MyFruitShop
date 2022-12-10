import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from bank.models import Bank, Declaration
from fruits.models import Fruit, Log
from users.models import Message


class MainView(LoginView):
    template_name = 'users/main_page.html'

    def get_redirect_url(self):
        return reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fruits'] = Fruit.objects.all()
        context['messages'] = Message.objects.all()[:40][::-1]
        context['bank'] = Bank.objects.first()
        context['count_docs'] = len(Declaration.objects.filter(date__day=datetime.datetime.now().strftime('%d')))
        context['logs'] = Log.objects.all()
        return context


class UserLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'users/main_page.html'
    next_page = reverse_lazy('main')

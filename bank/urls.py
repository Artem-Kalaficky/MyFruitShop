from django.urls import path

from bank.views import update_bank_account, start_audit

urlpatterns = [
    path('ajax-top-up-account/', update_bank_account, name='update_bank_account'),
    path('ajax-start-audit/', start_audit, name='start_audit')
]

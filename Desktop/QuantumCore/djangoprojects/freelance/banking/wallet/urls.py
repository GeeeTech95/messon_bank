from django.urls import path,include
from .views import Transfer,CompleteTransaction




urlpatterns = [
  path('transfer-in-bank',Transfer.InBank.as_view(),name='in-bank-transfer'),
  path('complete-transacton/<str:transact_id>/',CompleteTransaction.as_view(),name='complete-transaction')
]
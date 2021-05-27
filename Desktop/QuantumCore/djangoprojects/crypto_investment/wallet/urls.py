from django.urls import include,path
from .transaction import Deposit,Withdrawal,DepositComplete


urlpatterns = [
    path('<slug:slug>/invest/',Deposit.as_view(),name ='deposit'),
    path('<slug:slug>/<str:coin>/invest/payment-complete',DepositComplete.as_view(),name ='payment-complete'),
    path('widthdraw/',Withdrawal.as_view(),name ='deposit'),
]
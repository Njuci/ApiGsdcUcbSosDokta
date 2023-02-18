
from django.urls import path,include
from .views import touslesHopital,UnseulHopital
urlpatterns = [

    path('ApiTousleshopitaux/',touslesHopital().as_view()),
    path('unseulHopital/',UnseulHopital.as_view()),
    ]

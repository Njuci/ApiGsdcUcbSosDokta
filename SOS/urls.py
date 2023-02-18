
from django.urls import path,include
from .views import touslesHopital
urlpatterns = [

    path('ApiTousleshopitaux/',touslesHopital().as_view()),
    ]

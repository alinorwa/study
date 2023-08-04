from django.urls import path
from .views import *


urlpatterns = [
    path('' , home , name='home'),
    path('like/',like,name='like'),
    path('detail/<int:id>' , detail , name='detail'),
    path('comment/' , comment , name='commet'),
    path('contact/' , contact , name='contact'),
    
]
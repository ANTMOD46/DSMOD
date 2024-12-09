from django.urls import path
from . views import *

urlpatterns = [
    path('A/',A,name ='A'),
    path('B/',B,name ='B' ),
    path('C/',C,name ='C' ),
    path('D/<str:pk>',D.as_view(),name ='D' ),
    path('E/<str:pk>',E.as_view(),name ='E' ),
    
   
]
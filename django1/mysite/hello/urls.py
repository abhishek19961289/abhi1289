from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path('dict/', views.index1, name='index1'),
    path('page/', views.index, name='index'),
    path('dict2/', views.my_view, name='my_view'),    
    path('dict11/', views.index3, name='index3'),
    path('dynamic-image/', views.dynamic_image_view, name='dynamic_image'),
    path('dynamic-image10/', views.dynamic_image_view1, name='dynamic_image'),
    path('my-page/', views.my_page, name='my_page'),
    
    
]
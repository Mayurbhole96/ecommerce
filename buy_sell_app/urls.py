from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Login to ZIEGLER AEROSPACE"
admin.site.site_title = "Welcome to ZIEGLER's Dashboard"
admin.site.index_title = "Welcome to this ZIEGLER Portal"

urlpatterns = [
    # path('',views.home,name="home"),
    path('s_list', views.product_list, name='s_listpage'),
    path('s_cart', views.product_cart, name='s_cartpage'),

    path('welcome1', views.welcomepage1, name='welcomepage1'),
    path('add_product', views.add_product, name='add_product'),
    path('see_products', views.see_products, name='see_products'),

    path('welcome', views.welcomepage, name='welcomepage'),
    path('',views.loginuser,name="loginuser"),
    path('signnewuser', views.signnewuser,name='signnewuser'),
    path('logout',views.logoutpage,name="logoutpage"),

    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
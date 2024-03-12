from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from.import views 

from django.contrib import admin
from r_works.views import *

urlpatterns=[
    # path('',views.r_works,name='members'),
    path('admin/', admin.site.urls),
    path('',views.home),
    path('image/',views.images),
    path('video/',views.video),
    path('map/',views.map),
    path('certificate/',views.certificate),
    path('service/',views.service),
    path('dj and sound/',views.DJ),
    path('lighting/',views.lighting),
    path('fitting/',views.fitting),
    path('repair',views.repair),
    path('record',views.record),
    path('saved',views.saved),
    path('delete/<int:a>/',views.delete),
    path('about/',views.about),
    path('updt/',views.updt),
    path('update/<int:a>/',views.update),
    path('login/', views.loginp),
    path('home/', views.home),
    path('logout/', views.LogoutPage, name="Lout"),
    path('signup/',views.signup),
    # path('send/',views.SendEmail, name="email"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



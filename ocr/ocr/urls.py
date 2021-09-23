"""ocr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
#from django.urls import path

from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [
    url(r'^', include('mainpage.urls')),
    url(r'^rotate/', include('rotate.urls')),
    url(r'^angle_detection/', include('angle_detection.urls')),
    url(r'^search_txt_6/', include('search_txt_6.urls')),
    url(r'^fakt_morele/', include('fakt_morele.urls')),
    url(r'^img_crop/', include('img_crop.urls')),
    url(r'^correct_skew_old/', include('correct_skew_old.urls')),
    url(r'^pdf2jpg/', include('pdf2jpg.urls')),
    url(r'^ocr_core/', include('ocr_core.urls')),
    url(r'^admin/', admin.site.urls),
]

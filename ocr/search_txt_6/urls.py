from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'search_txt_6' 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.button),
    url(r'^output', views.output,name="script"),
    url(r'^external', views.external),
]

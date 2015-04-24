from django.conf.urls import patterns, include, url
from django.contrib import admin
from czat import views # importujemy zdefiniowane w pliku views.py widoki

admin.autodiscover() # potrzebne tylko w Django 1.6

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'czat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^rejestruj/', views.rejestruj, name='rejestruj'),
    url(r'^loguj/', views.loguj, name='loguj'),
    url(r'^wyloguj/', views.wyloguj, name='wyloguj'),
    url(r'^wiadomosci/', views.wiadomosci, name='wiadomosci'),

    url(r'^admin/', include(admin.site.urls)),
)

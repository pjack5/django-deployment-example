# from django.conf.urls import url
from basic_app import views
from django.urls import path, include

# TEMPLATE TAGGING
# need to set global var name called app_name, Django will look for this
# should be set equal to app name

app_name = 'basic_app'


# looking at project patterns, if you have a url that has "domain.com/basic_app/"...
## now look at these patterns, to see if it's domain.com/basic_app/relative for example,
## or /other for example

urlpatterns = [
    path('', views.index, name='index'),
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other')
]

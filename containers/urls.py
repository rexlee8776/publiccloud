from django.conf.urls import url

from containers import views


urlpatterns = [
    url('^containers$', views.containers, name="containers"),
    url('^create$', views.create, name="create"),
]

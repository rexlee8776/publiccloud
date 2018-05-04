from django.conf.urls import url

from users import views


urlpatterns = [
    url('^login$', views.login, name="login"),
    url('^register$', views.register, name="register"),
    url('^logout$', views.logout, name="logout"),
    url('^unauthenticate$', views.unauthenticate, name="unauthenticate"),
]

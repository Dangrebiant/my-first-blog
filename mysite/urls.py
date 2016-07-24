
from django.conf.urls import url, include
from django.contrib import admin
admin.autodiscover()

from accounts.views import (login_view, register_view, logout_view)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', 'mysite.views.home', name='home'),
    url(r'^blog/', include('testapp.urls')),
  ]

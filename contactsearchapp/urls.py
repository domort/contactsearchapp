from django.conf.urls import url, include
from django.contrib import admin

from contacts.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', index, name="index")
]

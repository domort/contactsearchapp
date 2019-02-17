from django.conf.urls import url
from django.contrib import admin

from contacts.views import ContactSearchView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', ContactSearchView.as_view(), name="contact-search")
]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView
from contacts.data.contact_store import ContactStore


class ContactSearchView(TemplateView):
    template_name = 'contact-search.html'
    contact_store = ContactStore()

    def get(self, *args, **kwargs):
        return self.render_to_response({})

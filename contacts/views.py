# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404, JsonResponse
from django.views.generic import TemplateView
from django.template.loader import render_to_string

from contacts.data.contact_store import ContactStore


class ContactSearchView(TemplateView):
    template_name = 'contact-search.html'
    contacts_template = 'contact-table.html'
    contact_store = ContactStore()

    def render_table(self, contacts):
        return render_to_string(self.contacts_template, {'contacts': contacts})

    def get(self, request, *args, **kwargs):
        contacts = self.contact_store.all_contacts
        return self.render_to_response({'contact_table': self.render_table(contacts)})

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            raise Http404()
        else:
            term = request.POST.get('term', None)
            matches = None
            if term:
                try:
                    term = unicode(term).lower()
                except (TypeError, ValueError):
                    term = None

                matches = self.contact_store.search_for_contacts(term)

            if not matches:
                matches = self.contact_store.all_contacts
            return JsonResponse({'contact_table': self.render_table(matches)})

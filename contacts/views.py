# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404, JsonResponse
from django.views.generic import TemplateView
from contacts.data.contact_store import ContactStore


class ContactSearchView(TemplateView):
    template_name = 'contact-search.html'
    contact_store = ContactStore()

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            raise Http404()
        else:
            term = request.POST.get('term', None)
            if term:
                try:
                    term = unicode(term).lower()
                except (TypeError, ValueError):
                    term = None

                matches = self.contact_store.search_for_contacts(term)
                return JsonResponse({'contacts': matches})

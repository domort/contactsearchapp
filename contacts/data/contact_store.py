import json


class ContactStore(object):
    contact_tree = {}

    def __init__(self):
        self.load_contacts_from_file()

    @classmethod
    def extract_terms(cls, item):
        if isinstance(item, dict):
            for k, v in item.iteritems():
                for t in cls.extract_terms(v):
                    yield t
        elif isinstance(item, list):
            for v in item:
                for t in cls.extract_terms(v):
                    yield t
        else:
            try:
                item = unicode(item)
            except:
                pass
            else:
                yield item.lower()

    @classmethod
    def build_search_tree(cls, contacts):
        tree = {}
        for contact in contacts:
            contact_terms = cls.extract_terms(contact)
            terms_str = u' '.join(contact_terms)
            tree[terms_str] = contact
        return tree

    def load_contacts_from_file(self):
        try:
            with open(u'contacts/data/contacts.json') as f:
                contacts = json.load(f)
                self.contact_tree = self.build_search_tree(contacts)
        except:
            pass

    def search_for_contacts(self, term):
        matches = []
        if term:
            try:
                term = unicode(term).lower()
            except:
                raise ValueError(u'Search term must be a valid string')

            for k, v in self.contact_tree.iteritems():
                if term in k:
                    matches.append(v)

        return matches or self.all_contacts

    @property
    def all_contacts(self):
        return self.contact_tree.values()

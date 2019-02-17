import json

from collections import OrderedDict


class ContactStore(object):
    """
        Builds and holds contact tree in a search friendly format
    """
    contact_tree = {}

    def __init__(self):
        self.load_contacts_from_file()

    @classmethod
    def extract_terms(cls, item):
        """
        Extracts searchable terms from a given object
        :param item: anything
        :return: generator object of searchable terms
        """
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
        """
        Builds contact tree used by the search function by mapping extracted terms to contact dicts
        :param contacts: list of contacts
        :return: dictionary in the following format: {representative_string: contact_dict}
        """
        tree = OrderedDict({})
        for contact in sorted(contacts, key=lambda c: c.get('name', '')):
            contact_terms = cls.extract_terms(contact)
            terms_str = u' '.join(contact_terms)
            tree[terms_str] = contact
        return tree

    def load_contacts_from_file(self):
        """
        Loads contacts from a json file and uses them to build a search tree
        :return: None
        """
        try:
            with open(u'contacts/data/contacts.json') as f:
                contacts = json.load(f)
                self.contact_tree = self.build_search_tree(contacts)
        except:
            pass

    def search_for_contacts(self, term):
        """
        Searches through contact list and returns contacts matching to the given term.
        Returns all contacts if there are no matches.
        :param term: a string to filter contacts by
        :return: list of matching contacts
        """
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
        """
        Shortcut to get all contacts
        """
        return self.contact_tree.values()

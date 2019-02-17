import json


class ContactStore(object):
    contact_tree = {}

    @classmethod
    def load_contacts_from_file(cls):
        contacts = []
        try:
            with open(u'contacts/data/contacts.json') as f:
                contacts = json.load(f)
        except:
            pass
        return contacts

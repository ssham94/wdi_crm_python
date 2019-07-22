class Contact:
    contacts = []
    next_id = 1
    
    def __str__(self):
        return f"First name: {self.first_name}, Last name: {self.last_name}, Email: {self.email}, Note: {self.note}"

    def __init__(self, given_name, surname, user_email, user_note):
        """This method should initialize the contact's attributes"""
        self.first_name = given_name
        self.last_name = surname
        self.email = user_email
        self.note = user_note
        self.id = Contact.next_id
        Contact.next_id += 1

    @classmethod
    def convert_string(cls, self, attribute_type):
        attributes = {'first_name': self.first_name, 'last_name': 'last_name', 'email': 'email', 'note': 'note'}

    @classmethod
    def create(cls, given_name, surname, user_email, user_note):
        """This method should call the initializer,
        store the newly created contact, and then return it
        """
        new_contact = Contact(given_name, surname, user_email, user_note)
        cls.contacts.append(new_contact)
        return new_contact

    @classmethod
    def all(cls):
        """This method should return all of the existing contacts"""
        for contact in Contact.contacts:
            print(contact)

    @classmethod
    def find(cls, search_id):
        """ This method should accept an id as an argument
        and return the contact who has that id
        """
        for contact in Contact.contacts:
            if search_id == contact.id:
                print(contact)
                return contact
            else:
                return False

    def update(self, attribute_type, attribute_update = ''):
        """ This method should allow you to specify
        1. which of the contact's attributes you want to update
        2. the new value for that attribute
        and then make the appropriate change to the contact
        """
        if attribute_type == 'first_name':
            self.first_name = attribute_update
        elif attribute_type == 'last_name':
            self.last_name = attribute_update
        elif attribute_type == 'email':
            self.email = attribute_update
        elif attribute_type == 'note':
            self.note = attribute_update


    @classmethod
    def find_by(cls, attribute_type, search_by):
        """This method should work similarly to the find method above
        but it should allow you to search for a contact using attributes other than id
        by specifying both the name of the attribute and the value
        eg. searching for 'first_name', 'Betty' should return the first contact named Betty
        """
        for contact in Contact.contacts:
            if attribute_type == 'first_name' and contact.first_name == search_by:
                return contact
            elif attribute_type == 'last_name' and contact.last_name == search_by:
                return contact
            elif attribute_type == 'email' and contact.email == search_by:
                return contact
            elif attribute_type == 'note' and contact.note == search_by:
                return contact
        print(f"Cannot find user based on {attribute_type}, please check that you have the right identifier")
        return False

    @classmethod
    def delete_all(cls):
        """This method should delete all of the contacts"""
        Contact.contacts.clear()


    def full_name(self):
        """Returns the full (first and last) name of the contact"""
        return f'{self.first_name} {self.last_name}'


    def delete(self):
        """This method should delete the contact
        HINT: Check the Array class docs for built-in methods that might be useful here
        """
        Contact.contacts.remove(self)
    # Feel free to add other methods here, if you need them.


# # Creating new contacts and checking create function
# contact1 = Contact.create('Betty', 'Maker', 'bettymakes@bitmakerlabs.com', 'Loves Pokemon')
# contact2 = Contact.create('Bit', 'Bot', 'bitbot@bitmakerlabs.com', 'beep boop')
# print(contact1.first_name)
# print(contact1.id)
# print('')
# print(contact2.first_name)
# print(contact2.id)
# print('')

# # Testing all and find functions
# print(len(Contact.contacts))
# Contact.all()
# print(Contact.find(1))
# print('')

# # Testing update function
# print(contact1.update('full name'))
# contact1.update('first_name', 'stanley')
# print(contact1.first_name)
# print('')

# # Testing find by
# print(Contact.find_by('first_name', 'stanley'))
# print(Contact.find_by('first_name', 'betty'))
# print('')

# # Testing delete all
# # Contact.delete_all() # Commented out so that delete function below works
# print(Contact.contacts) # Should return an empty list
# print('')

# # Testing full name function
# print(contact1.full_name())
# print('')

# # Testing delete
# contact1.delete()
# print(Contact.contacts)

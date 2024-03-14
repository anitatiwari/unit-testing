class Person:
    name = []

    def set_name(self, user_name):
        self.name.append(user_name)
        return len(self.name) - 1

   def get_name(self, user_id):
        if user_id >= len(self.name) or user_id < 0:  # Modified condition
            raise IndexError('Invalid user ID')  # Raise an exception for invalid user IDs
        else:
            return self.name[user_id]


if __name__ == '__main__':
    person = Person()
    print('User Abbas has been added with id ', person.set_name('Abbas'))
    print('User associated with id 0 is ', person.get_name(0))

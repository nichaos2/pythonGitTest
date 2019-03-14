'''
Created on 1 mars 2019

@author: nioannou
'''
import sy
print(sys.version)

from model.Person import Person
if __name__ == '__main__':
    person = Person()
    print('User Abbas has been added with id ', person.set_name('Abbas'))
    print('User associated with id 0 is ', person.get_name(0))

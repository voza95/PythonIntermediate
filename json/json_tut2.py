import json


class User:

    def __init__(self,name,age):
        self.name = name
        self.age = age


user = User('Max',27)

def encode_user(o):
    if isinstance(o, User):
        return {'name':o.name, 'age':o.age, o.__class__.__name__:True}
    else:
        o_name = o.__class__.__name__
        return TypeError(f'Object of type {o_name} is not JSON serializable')  

# First way to convert user object to serializalbe
# userJSON = json.dumps(user, default=encode_user)
# print(userJSON)

from json import JSONEncoder

class UserEncoder(JSONEncoder):

    def default(self,o):
        if isinstance(o, User):
            return {'name':o.name, 'age':o.age, o.__class__.__name__:True}
        return JSONEncoder.default(self,o)

# Second way
# userJSON = json.dumps(user, cls=UserEncoder)
# or
userJSON = UserEncoder().encode(user)
print(userJSON)

# By default on decode user object is dict to convert it into User class object.
# from json import JSONDecoder

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct    

user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)

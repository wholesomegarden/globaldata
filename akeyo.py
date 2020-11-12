#akeyo.py

from gd import *
import uuid

def new_id(ob = None):
    t = str(type(ob))
    if "." in t:
        t = t.split(".")[-1]
    s = t[0]+"_"
    n = s.capitalize()+t[1:]

    r = uuid.uuid4().hex
    return s + r, s

class Entity(obj):
    def __init__(self):
        id, s = new_id(self)
        super().__init__(id="akeyo/entities/"+id)
        self.id = id
        # if id not in xo.IDs.kids():
        #     xo.akeyo.entities[s + id] = [s.capitalize()+str(type(self))[1:],time.time()]


class Omega(Entity):
    def __init__(self):
        super().__init__()

    def placeOrder(self):
        new = order(self)
        return new


class Alpha(Entity):
    def __init__(self):
        super().__init__()


class aKey(Entity):
    def __init__(self):
        super().__init__()


class order(obj):
        def __init__(self,omega):
            id, s = new_id(self)
            super().__init__(id="akeyo/orders/"+id)
            self.id = id
            # if id not in xo.IDs.kids():
            #     xo.akeyo.entities[s + id] = [s.capitalize()+t[1:],time.time()]

            self.info.status = "Init"
            self.info.created = time.time()
            self.omega = omega
            self.key = None
            self.alphas = []
            self.details.extra = None
            self.details.main = None

class Item:

    def __init__(self, id, name, pickup_description, description, type, pool, recharge, unlock):
        self.id = id
        self.name = name
        self.pickup_description = pickup_description
        self.description = description
        self.type = type
        self.pool = pool

        if recharge is not None:
            self.recharge = recharge

        if unlock is not None:
            self.unlock = unlock

class Trinket:

    def __init__(self, id, name, pickup_description, description, unlock):
        self.id = id
        self.name = name
        self.pickup_description = pickup_description
        self.description = description

        if unlock is not None:
            self.unlock = unlock
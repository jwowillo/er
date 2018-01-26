class ER(object):

    def __init__(self, ers):
        self.entities = []
        self.relations = []
        for er in ers:
            if isinstance(er, Entity):
                self.entities.append(er)
            else:
                self.relations.append(er)


class Many(object):

    def __init__(self, entity):
        self.entity = entity


class One(object):

    def __init__(self, entity):
        self.entity = entity


class Attribute(object):

    def __init__(self, name):
        self.name = name


class Entity(object):

    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes


class Relation(object):

    def __init__(self, name, entities):
        self.name = name
        self.entities = entities




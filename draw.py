import random
import string

import graphviz

from er import One


def rand(n):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))


def draw(file_name, er):
    dot = graphviz.Digraph(engine='neato', format='png')
    rendered = set()
    for entity in er.entities:
        rendered.add(entity.name)
        dot.node(entity.name, entity.name, shape='box')
        for attr in entity.attributes:
            name = attr.name + rand(4)
            dot.node(name, attr.name)
            dot.edge(entity.name, name, arrowsize='0')
    for relation in er.relations:
        dot.node(relation.name, relation.name, shape='diamond')
        for entity in relation.entities:
            if entity.entity.name in rendered:
                continue
            rendered.add(entity.entity.name)
            dot.node(entity.entity.name, entity.entity.name, shape='box')
            for attr in entity.entity.attributes:
                name = attr.name + rand(4)
                dot.node(name, attr.name)
                dot.edge(entity.entity.name, name, arrowsize='0')
    for relation in er.relations:
        for entity in relation.entities:
            if isinstance(entity, One):
                dot.edge(relation.name, entity.entity.name)
            else:
                dot.edge(relation.name, entity.entity.name, arrowsize='0')
    dot.render(file_name)


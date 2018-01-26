from draw import draw
from er import Attribute, Entity, Relation, ER, One, Many

# TODO: Relationship attributes.
# TODO: Clean up draw.
# TODO: Delete out file.


if __name__ == '__main__':
    stars = Entity('Stars', [Attribute('name'), Attribute('address')])
    studios = Entity('Studios', [Attribute('name'), Attribute('address')])
    movies = Entity('Movies', [
        Attribute('title'),
        Attribute('year'),
        Attribute('length'),
        Attribute('genre')
    ])
    stars_in = Relation('Stars-In', [Many(stars), One(movies)])
    owns = Relation('Owns', [One(studios), Many(movies)])
    draw('out', ER([stars_in, owns]))

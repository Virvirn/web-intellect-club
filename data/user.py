import sqlalchemy
import sqlalchemy.ext.declarative as dec

SqlAlchemyBase = dec.declarative_base()


class User(SqlAlchemyBase):
    __tablename__ = 'people'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    phone = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    age = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    course = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    def __repr__(self):
        return '<User %r' % self.id


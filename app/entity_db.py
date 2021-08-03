import databases
import sqlalchemy

DATABASE_URL = "postgresql://postgres:pwd864@localhost/document_entity"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

entities = sqlalchemy.Table(
    'entities',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String),
    sqlalchemy.Column('date', sqlalchemy.DateTime),
    sqlalchemy.Column('content', sqlalchemy.Text),
    sqlalchemy.Column('owner', sqlalchemy.String),

)

engine = sqlalchemy.create_engine(DATABASE_URL)

metadata.create_all(engine)

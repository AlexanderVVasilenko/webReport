from peewee import SqliteDatabase, Model, CharField

db = SqliteDatabase("f1_racing.db")


class BaseModel(Model):
    class Meta:
        database = db


class Racer(BaseModel):
    name = CharField()
    team = CharField()
    lap_time = CharField()
    driver_id = CharField(unique=True)


db.connect()
db.create_tables([Racer])

# new_racer = Racer.create(name='Lewis Hamilton', team='Mercedes', lap_time='1:30.000', driver_id='HAM')

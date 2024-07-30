from peewee import *

database = MySQLDatabase('bookorders', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': 'localhost', 'user': 'bookorders', 'password': 'imp0rtUser'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Bookorders(BaseModel):
    age = IntegerField(column_name='Age', null=True)
    comment = CharField(column_name='COMMENT', null=True)
    colony_street_village = CharField(column_name='ColonyStreetVillage', null=True)
    country = CharField(column_name='Country', null=True)
    date_created = DateTimeField(column_name='DateCreated', null=True)
    email = CharField(column_name='Email', null=True)
    first_name = CharField(column_name='FirstName', null=True)
    flat_house_building = CharField(column_name='FlatHouseBuilding', null=True)
    language = CharField(column_name='LANGUAGE', null=True)
    landmark = CharField(column_name='Landmark', null=True)
    last_name = CharField(column_name='LastName', null=True)
    mobile_number = TextField(column_name='MobileNumber', null=True)
    order_date = DateTimeField(column_name='OrderDate', null=True)
    order_id = AutoField(column_name='OrderID')
    order_reason = CharField(column_name='OrderReason', null=True)
    pin_postal_zip_code = CharField(column_name='PinPostalZipCode', null=True)
    quantity = IntegerField(column_name='Quantity', null=True)
    status = IntegerField(column_name='STATUS', null=True)
    state_prov = CharField(column_name='StateProv', null=True)
    town_city = CharField(column_name='TownCity', null=True)

    class Meta:
        table_name = 'bookorders'

if __name__ == "__main__":
    bo = Bookorders()
    print(dir(bo))

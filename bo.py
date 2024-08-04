#!/usr/bin/env python

import sys
import peewee
#import pymysql
import keyring

passwd = keyring.get_password('remote_mariadb', 'bookorders')
_DB = 'bookorders'
_USER = 'bookorders'
_PASSWD = passwd
_HOST = 'venus.mine.nu'

database = peewee.MySQLDatabase(_DB, **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': _HOST, 'user': _USER, 'password': _PASSWD})

class UnknownField(object):
    def __init__(self, *_, **__): 
        pass

class BaseModel(peewee.Model):
    class Meta:
        database = database

class Bookorders(BaseModel):
    age = peewee.IntegerField(column_name='Age', null=True)
    comment = peewee.CharField(column_name='COMMENT', null=True)
    colony_street_village = peewee.CharField(column_name='ColonyStreetVillage', null=True)
    country = peewee.CharField(column_name='Country', null=True)
    date_created = peewee.DateTimeField(column_name='DateCreated', null=True)
    email = peewee.CharField(column_name='Email', null=True)
    first_name = peewee.CharField(column_name='FirstName', null=True)
    flat_house_building = peewee.CharField(column_name='FlatHouseBuilding', null=True)
    language = peewee.CharField(column_name='LANGUAGE', null=True)
    landmark = peewee.CharField(column_name='Landmark', null=True)
    last_name = peewee.CharField(column_name='LastName', null=True)
    mobile_number = peewee.TextField(column_name='MobileNumber', null=True)
    order_date = peewee.DateTimeField(column_name='OrderDate', null=True)
    order_id = peewee.AutoField(column_name='OrderID')
    order_reason = peewee.CharField(column_name='OrderReason', null=True)
    pin_postal_zip_code = peewee.CharField(column_name='PinPostalZipCode', null=True)
    quantity = peewee.IntegerField(column_name='Quantity', null=True)
    status = peewee.IntegerField(column_name='STATUS', null=True)
    state_prov = peewee.CharField(column_name='StateProv', null=True)
    town_city = peewee.CharField(column_name='TownCity', null=True)

    class Meta:
        table_name = 'bookorders'
        
    def show(self):
        rc = "Bookorder[order_id:" + str(self.order_id) + ", Name:" + self.first_name + ", Email:" + self.email + "]"
        return rc
        
if __name__ == "__main__":
    # oneOrder = Bookorders()
    # oneOrder.first_name = "New1"
    # oneOrder.last_name = "Order1"
    # oneOrder.email = "new1.order1@gmail.com"
    # oneOrder.mobile_number = "+11012013001"
    # oneOrder.create_table([Bookorders,])
    # print(dir(database))
    # print(database.database)
    try:
        database.create_tables(Bookorders)
    except:
        print(sys.exc_info())
    # oneOrder = Bookorders()
    # oneOrder.first_name = "New3"
    # oneOrder.last_name = "Order3"
    # oneOrder.email = "new1.order3@gmail.com"
    # oneOrder.mobile_number = "+31012013003"
    # oneOrder.save()
    # allOrders = oneOrder.select()
    # for o in allOrders:
        # print("%d %s %s %s" % (o.order_id, o.first_name, o.last_name, o.email))

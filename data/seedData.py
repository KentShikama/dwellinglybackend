from db import db
from models.user import UserModel
from models.property import PropertyModel
from models.revoked_tokens import RevokedTokensModel


def seedData():
    user = UserModel(email="user1@dwellingly.org", role="admin", firstName="user1", lastName="tester", password="1234", archived=0)
    db.session.add(user)
    user = UserModel(email="user2@dwellingly.org", role="admin", firstName="user2", lastName="tester", password="1234", archived=0)
    db.session.add(user)
    user = UserModel(email="user3@dwellingly.org", role="admin", firstName="user3", lastName="tester", password="1234", archived=0)
    db.session.add(user)
    user = UserModel(email="MisterSir@dwellingly.org", role="property-manager", firstName="Mr.", lastName="Sir", password="1234", archived=0)
    db.session.add(user)
    user = UserModel(email="user3@dwellingly.org", role="property-manager", firstName="Gray", lastName="Pouponn", password="1234", archived=0)
    db.session.add(user)
    user = UserModel(email="pendinguser@dwellingly.org", role="pending", firstName="pending", lastName="user", password="1234", archived=0)
    db.session.add(user)

    newProperty = PropertyModel(name="test1", address="123 NE FLanders St", city="Portland", state="OR", zipcode="97207", propertyManager=5, tenants=3, dateAdded="2020-04-12", archived=0)
    db.session.add(newProperty)
    newProperty = PropertyModel(name="Meerkat Manor", address="Privet Drive", city="Portland", state="OR", zipcode="97207", propertyManager=4, tenants=6, dateAdded="2020-04-12", archived=0)
    db.session.add(newProperty)
    newProperty = PropertyModel(name="The Reginald", address="Aristocrat Avenue", city="Portland", state="OR", zipcode="97207", propertyManager=5, tenants=4, dateAdded="2020-04-12", archived=0)
    db.session.add(newProperty)

    revokedToken = RevokedTokensModel(jti="855c5cb8-c871-4a61-b3d8-90249f979601")
    db.session.add(revokedToken)

    db.session.commit()


from datetime import datetime

from mongoengine import StringField, DateTimeField, Document, IntField, BooleanField


class LeaveBase(Document):
    user_id = IntField(required=False)
    name = StringField(max_length=50, required=False)
    applied_on = DateTimeField(default=datetime.now())
    starting_from = DateTimeField()
    ending_on = DateTimeField()
    no_of_days = IntField()
    id_approved = BooleanField(default=False)
    reason = StringField(max_length=400, required=True)

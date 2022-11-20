from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import validates, column_property
from sqlalchemy.ext.hybrid import hybrid_property

import datetime
import six

db = SQLAlchemy()
ma = Marshmallow()


class Option(db.Model):
    __tablename__ = "k_option"
    id = db.Column(db.Integer, primary_key=True)
    option = db.Column(db.JSON)
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id")
    )

    def __init__(self, *args, **kwargs):
        super(Option, self).__init__(**kwargs)

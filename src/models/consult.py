from marshmallow import  Schema, fields
from sqlalchemy import Column, String, DateTime, Integer, Boolean
from .model import Model, Base
from datetime import datetime, timedelta
from uuid import uuid4
import argon2

class Consult(Model, Base):
  __tablename__ = 'consults'

  injury_type = Column(String)
  shape = Column(String)
  injuries_count = Column(Integer)
  distribution = Column(String)
  color = Column(String)
  photo_url = Column(String)
  user_id = Column(Integer)
  automatic = Column(Boolean)
  specialist_id = Column(Integer, nullable=True)
  city = Column(String)
  status = Column(Integer) # 0: PENDING, 1: CONFIRMED, 2: REJECTED
  diagnosis = Column(String, nullable=True)

  def __init__(self, injury_type, shape, injuries_count, distribution, color, photo_url, user_id, automatic, city, status, specialist_id = None, diagnosis = None):
    Model.__init__(self)
    self.injury_type = injury_type
    self.shape = shape
    self.injuries_count = injuries_count
    self.distribution = distribution
    self.color = color
    self.photo_url = photo_url
    self.user_id = user_id
    self.automatic = automatic
    self.city = city
    self.status = status
    self.specialist_id = specialist_id
    self.diagnosis = diagnosis

class ConsultSchema(Schema):
  injury_type = fields.Str()
  shape = fields.Str()
  injuries_count = fields.Number()
  distribution = fields.Str()
  color = fields.Str()
  photo_url = fields.Str()
  user_id = fields.Number()
  automatic = fields.Boolean()
  specialist_id = fields.Number(allow_none=True)
  city = fields.Str()
  status = fields.Integer()
  diagnosis = fields.Str()

class ConsultJsonSchema(Schema):
  id = fields.Number()
  created_at = fields.DateTime()
  injury_type = fields.Str()
  shape = fields.Str()
  injuries_count = fields.Number()
  distribution = fields.Str()
  color = fields.Str()
  photo_url = fields.Str()
  user_id = fields.Number()
  automatic = fields.Boolean()
  specialist_id = fields.Number()
  city = fields.Str()
  status = fields.Integer()
  diagnosis = fields.Str()

class ConsultJsonSchemaReadable(Schema):
  id = fields.Number()
  created_at = fields.DateTime()
  updated_at = fields.DateTime()
  injury_type = fields.Str()
  shape = fields.Str()
  injuries_count = fields.Number()
  distribution = fields.Str()
  color = fields.Str()
  photo_url = fields.Str()
  user_name = fields.Str()
  user_email = fields.Str()
  automatic = fields.Boolean()
  specialist_name = fields.Str()
  city = fields.Str()
  status = fields.Integer()
  diagnosis = fields.Str()

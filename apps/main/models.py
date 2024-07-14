from apps import db
from datetime import datetime
import pytz

class Send_Emails(db.Model):
    __tablename__ = 'send_emails'
    
    id = db.Column(db.BigInteger, primary_key=True)
    event_id = db.Column(db.Integer)
    celery_id = db.Column(db.String(120), nullable=True)
    
    email_subject = db.Column(db.String(120), nullable=True)
    email_content = db.Column(db.Text, nullable=True)
    
    status = db.Column(db.SmallInteger, default=0) # 0: pending, 1: sended, -1: failed, -2:canceled
    send_date = db.Column(db.DateTime(timezone=True), default=datetime.now(pytz.timezone('Asia/Singapore')))
    
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now(pytz.timezone('Asia/Singapore')))
    
    def __repr__(self):
        return f'<id: {self.id}, Email: {self.email}>'
    
class Recipient_Emails(db.Model):
    __tablename__ = 'recipient_emails'
    
    id = db.Column(db.BigInteger, primary_key=True)
    send_emails_id = db.Column(db.BigInteger, db.ForeignKey('send_emails.id'), nullable=False)
    
    email = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now(pytz.timezone('Asia/Singapore')))
    
    campaign = db.relationship('Send_Emails', backref='recipient_emails')
    
    def __repr__(self):
        return f'<id: {self.id}, Email: {self.email}>'
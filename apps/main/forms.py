from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, DateTimeField, FieldList, FormField
from wtforms.validators import DataRequired, Length, Email
from datetime import datetime


class EmailForm(FlaskForm):
    event_id = IntegerField('Event ID', default=0, validators=[DataRequired()], render_kw={'id': 'event_id', 'class': 'form-control'})
    subject = StringField('Subject', validators=[Length(max=500)], render_kw={'id':'subject', 'class': 'form-control'})
    body = TextAreaField('Message', render_kw={'id': 'body', 'class': 'form-control'})
    send_date = DateTimeField('Date and Time', format='%d %b %Y %H:%M', default=datetime.now, render_kw={'id': 'send_date', 'class': 'form-control'})
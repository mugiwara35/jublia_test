from flask import Blueprint, render_template, jsonify, request
from .forms import EmailForm
from .models import Send_Emails, Recipient_Emails
from apps import db
from apps.tasks import send_async_email, cancel_task
import pytz
from sqlalchemy import desc

main_bp = Blueprint('main', __name__, template_folder='templates')

@main_bp.route('/')
def index():
    email_form = EmailForm()
    list_data_email = Send_Emails.query.order_by(desc(Send_Emails.id)).all()

    data_with_recipients = []
    for data in list_data_email:
        recipients = Recipient_Emails.query.filter_by(send_emails_id=data.id).all()
        recipient_list = [recipient.email for recipient in recipients]

        # Append dalam bentuk dict
        data_with_recipients.append({
            'id': data.id,
            'event_id': data.event_id,
            'email_subject': data.email_subject,
            'email_content': data.email_content,
            'send_date': data.send_date,
            'status': data.status,
            'recipients': recipient_list
        })
    context = {
        'list_data_email': data_with_recipients
    }
    
    return render_template('index.html', email_form=email_form, **context)

@main_bp.route('/save_emails', methods=["POST"])
def save_emails():
    form = EmailForm(request.form)
    
    # print("Form Data Received:", request.form)
    # print("CSRF Token Received:", request.form.get('csrf_token'))

    if form.validate():
        event_id = form.event_id.data
        emails = request.form.getlist('emails')
        subject = form.subject.data
        body = form.body.data
        send_date = form.send_date.data
        
        new_email = Send_Emails(
                                event_id = event_id,
                                email_subject = subject,
                                email_content = body, 
                                send_date= send_date,
                            )        
        
        db.session.add(new_email)
        db.session.commit()
        
        for email in emails:
            new_recipient = Recipient_Emails(send_emails_id=new_email.id, email=email)
            db.session.add(new_recipient)
            db.session.commit()
        
        singapore_tz = pytz.timezone('Asia/Singapore')
        singapore_time = singapore_tz.localize(send_date)
        utc_time = singapore_time.astimezone(pytz.utc)
        
        celery_id = send_async_email.apply_async(args=[new_email.id], eta=utc_time)
        new_email.celery_id = celery_id.id
        db.session.commit()
        
        return jsonify({'message': 'Emails saved successfully!'}), 200
    else:
        errors = form.errors
        print("Errors: ", errors)
        return jsonify({'errors': errors}), 400
    
    
@main_bp.route('/get_emails/<int:id>', methods=["GET"])
def get_emails(id):
    data_send_emails = Send_Emails.query.filter_by(id=id).first()
    
        
        
    if data_send_emails:
        recipients = Recipient_Emails.query.filter_by(send_emails_id=id).all()
        recipient_list = [recipient.email for recipient in recipients]
        
        return jsonify({
            'event_id': data_send_emails.event_id,
            'email': recipient_list,
            'email_subject': data_send_emails.email_subject,
            'email_content': data_send_emails.email_content, 
            'status': data_send_emails.status,
            'send_date': data_send_emails.send_date,
             
        }), 200
    else:
        return jsonify({'message': 'Email not found'}), 404
    
@main_bp.route('/cancel_emails/<int:id>', methods=["GET"])
def cancel_emails(id):
    data_send_emails = Send_Emails.query.filter_by(id=id).first()
    if data_send_emails:
        if data_send_emails.status == 0:
            cancel_task(data_send_emails.celery_id)
            data_send_emails.status = -2
            db.session.commit()
            
            return jsonify({
                'event_id': data_send_emails.event_id,
                'email': "",
                'email_subject': data_send_emails.email_subject,
                'email_content': data_send_emails.email_content, 
                'status': data_send_emails.status,
                'send_date': data_send_emails.send_date,
                
            }), 200
        elif data_send_emails.status == 1:
            return jsonify({'message': 'Cannot be cancelled, because this email has been successfully sent'}), 400
        else:
            return jsonify({'message': 'This email has already been cancelled'}), 400
    else:
        return jsonify({'message': 'Email not found'}), 404


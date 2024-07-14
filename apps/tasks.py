from apps import create_app
from flask_mail import Message
from apps import mail, db
from apps import create_celery
from celery import Celery
import logging
from apps.main.models import Send_Emails, Recipient_Emails

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

celery = Celery('tasks')
celery.conf.update(broker_url='redis://localhost:6379/0', result_backend='redis://localhost:6379/0')

@celery.task(name='tasks.send_async_email')
def send_async_email(id):
    logger.info("Starting send_async_email task")
    try:
        app = create_app()
        with app.app_context():
            logger.info("App context created successfully")

            # Ensure configuration is correct
            logger.info(f"Mail server: {app.config['MAIL_SERVER']}")
            logger.info(f"Mail port: {app.config['MAIL_PORT']}")

            from apps import mail  # Import mail instance here to avoid circular import
        
            db_send_email = Send_Emails.query.filter_by(id=id).first()
            if db_send_email:
                db_recipient_email = Recipient_Emails.query.filter_by(send_emails_id=id).all()
                email_list = [recipient.email for recipient in db_recipient_email]
                logger.info(f"Mail LIST: {email_list}")
                
                msg = Message(db_send_email.email_subject, recipients=email_list)
                msg.body = db_send_email.email_content
                mail.send(msg)

                db_send_email.status = 1
                db.session.commit()
            else:
                logger.info(f"Mail port: {app.config['MAIL_PORT']}")
                
                
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        
def cancel_task(task_id):
    celery.control.revoke(task_id, terminate=True)
    logger.info(f"Task {task_id} has been revoked.")
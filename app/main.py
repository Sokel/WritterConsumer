import pika
import settings
from db.postgreWritter import DbWrapper

# DECLARE QUEUE PROCESS
connection = pika.BlockingConnection(pika.ConnectionParameters(settings.RABBIT_HOST))
channel = connection.channel()
channel.queue_declare(queue=settings.QUEUE)

# DECLARE DB CONTEXT
db = DbWrapper()


def write_to_db(ch, method, properties, body):
    cursor = db.get_cursor()
    cursor.execute()


def main_context():
    channel.basic_consume(write_to_db,
                          queue='hello',
                          no_ack=True)
    channel.start_consuming()

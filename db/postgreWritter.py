import psycopg2
import settings


class DbWrapper:
    connection = psycopg2.connect(
        host=settings.DB_HOST,
        user=settings.DB_USER,
        password=settings.DB_PASS
    )

    def get_cursor(self):
        return self.connection.cursor()

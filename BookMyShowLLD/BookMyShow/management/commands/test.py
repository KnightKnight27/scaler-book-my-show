from django.core.management import BaseCommand
from django.db import connection


class Command(BaseCommand):
    def handle(self, *args, **options):
        with connection.cursor() as conn:
            conn.execute("select * from django_migrations")
            results = conn.fetchall()
            for result in results:
                print(result)
        queries = connection.queries
        print("Number of queries", len(queries))
        for q in queries:
            print(q)
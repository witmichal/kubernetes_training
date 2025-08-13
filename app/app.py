from typing import Optional
from flask import Flask
import psycopg2
import os

app = Flask(__name__)


'''
export DB_HOST=localhost
export DB_NAME=postgres
export DB_USER=postgres
export DB_PASS=mypassword

docker run -p 5432:5432 --name postgres-db -e POSTGRES_PASSWORD=mypassword postgres
psql -h localhost -U postgres -d postgres
'''
def fetch_postgres_version() -> Optional[str]:
	try:
		host = os.environ['DB_HOST']
		name = os.environ['DB_NAME']
		user = os.environ['DB_USER']
		password = os.environ['DB_PASS']

		#conn = psycopg2.connect(f"dbname='postgres' user='postgres' host='localhost' password='mypassword'")
		conn = psycopg2.connect(f"dbname='{name}' user='{user}' host='{host}' password='{password}'")
		with conn.cursor() as curs:
			try:
				curs.execute("SELECT version()")
				single_row = curs.fetchone()
				return str(single_row)
			except (Exception, psycopg2.DatabaseError) as error:
				print(error)
	except Exception as e:
		print(repr(e))
		print("I am unable to connect to the database")


@app.route('/')
def hello():
	pg_version = fetch_postgres_version()
	return f"Hello World! - PG version: {pg_version}"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)

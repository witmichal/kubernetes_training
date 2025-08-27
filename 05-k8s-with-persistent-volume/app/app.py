from typing import Optional
from flask import Flask
import psycopg2
import os
from pathlib import Path

app = Flask(__name__)


def read_env_var(key: str) -> Optional[str]:
	try:
		return os.environ[key]
	except KeyError as e:
		print(repr(e) + f" - no env var defined: {key}")
		return None


'''
export DB_HOST=localhost
export DB_NAME=postgres
export DB_USER=postgres
export DB_PASS=mypassword

docker run -p 5432:5432 --name postgres-db -e POSTGRES_PASSWORD=mypassword postgres
psql -h localhost -U postgres -d postgres
'''
def build_connection_string() -> str:
	host = read_env_var('DB_HOST')
	name = read_env_var('DB_NAME')
	user = read_env_var('DB_USER')
	password = read_env_var('DB_PASS')

	creds_mount = "/etc/creds"
	if password is None:
		password = Path(f"{creds_mount}/db-password").read_text().strip()
	if user is None:
		user = Path(f"{creds_mount}/db-username").read_text().strip()

	return f"dbname='{name}' user='{user}' host='{host}' password='{password}'"


def fetch_postgres_version() -> Optional[str]:
	def go(curs) -> str:
		curs.execute("SELECT version()")
		single_row = curs.fetchone()
		return str(single_row)
	return db_operation(go)


def increase_counter_in_db() -> Optional[str]:
	def go(curs) -> str:
		curs.execute("UPDATE visits.visits SET counter = counter + 1")
		updated_row_count = curs.rowcount
		return str(updated_row_count)
	return db_operation(go)


def reset_counter_in_db() -> Optional[str]:
	def go(curs) -> str:
		curs.execute("UPDATE visits.visits SET counter = 0")
		updated_row_count = curs.rowcount
		return str(updated_row_count)
	return db_operation(go)


def fetch_counter_from_db() -> Optional[str]:
	def go(curs) -> str:
		curs.execute("SELECT counter FROM visits.visits")
		single_row = curs.fetchone()
		return str(single_row)
	return db_operation(go)


def db_operation(procedure) -> Optional[str]:
	try:
		#"dbname='postgres' user='postgres' host='localhost' password='mypassword'"
		connection_string = build_connection_string()
		print(f"Connecting to: [{connection_string}]")

		with psycopg2.connect(connection_string) as conn:
			with conn.cursor() as curs:
				try:
					return procedure(curs)
				except (Exception, psycopg2.DatabaseError) as error:
					print(repr(error))
			conn.commit()

	except Exception as e:
		print(repr(e))
		print("I am unable to connect to the database")


@app.route('/')
def hello():
	pg_version = fetch_postgres_version()
	return f"Hello World! - PG version: {pg_version}"


@app.route('/counter/increase', methods = ['POST'])
def increase_counter():
	pg_version = increase_counter_in_db()
	return f"Increasing counter result: {pg_version}"


@app.route('/counter/reset', methods = ['POST'])
def reset_counter():
	pg_version = reset_counter_in_db()
	return f"Increasing counter result: {pg_version}"


@app.route('/counter', methods = ['GET'])
def fetch_counter():
	pg_version = fetch_counter_from_db()
	return f"Counter: {pg_version}"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)

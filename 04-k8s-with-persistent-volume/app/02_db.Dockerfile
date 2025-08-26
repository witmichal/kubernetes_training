FROM postgres:17.5

# RUN ["mkdir", "/docker-entrypoint-initdb.d"]
ADD init.sql /docker-entrypoint-initdb.d/init.sql

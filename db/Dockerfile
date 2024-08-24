FROM postgres:15

COPY ./docker-entrypoint-initdb.d/init.sql /docker-entrypoint-initdb.d/
COPY ./docker-entrypoint-initdb.d/init-db.sh /docker-entrypoint-initdb.d/

RUN chmod +x /docker-entrypoint-initdb.d/init-db.sh

EXPOSE 5432

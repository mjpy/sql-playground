FROM postgres

RUN apt-get update
RUN apt install wget unzip -y

COPY entrypoint/* /docker-entrypoint-initdb.d/

WORKDIR /dvdrental
RUN wget https://www.postgresqltutorial.com/wp-content/uploads/2019/05/dvdrental.zip
RUN unzip dvdrental.zip

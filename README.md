# sql-playground

### Overview

A stack with sample database and [Metabase](https://www.metabase.com) set up. Includes example queries.

Metabase is a BI Tool, allows you to run SQL, create visualisations, dashboards and many more.

Created to help people learn SQL / BI Tools - all you need to do is to deploy the stack and you have Metabase ready with access to a popular [dvdrental](https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/) database.

You need [docker compose](https://docs.docker.com/compose/).


### Links

[DVD rental database](https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/)

[Metabase docs](https://www.metabase.com/docs/latest/)

[Docker compose](https://docs.docker.com/compose/)


### Important

On Mac M1 - this ain't working, problems with metabase images on M1, sometimes it can work, usually it won't.

On Windows - run this before running the stack (TODO: add a script for this):
```
    sed -i -e 's/\r$//' postgres/entrypoint/03-load-dvdrental-db.sh
```


### How to

1. Get docker-compose: https://docs.docker.com/compose/  
2. `docker compose up`  
3. Go to http://localhost:3000 in your browser.  
    - Wait like a minute after previous step for the user setup to run. If you see registration form, refresh the page after few seconds.  
    - You can change port in `.env` file.  
4. Email: `admin@metabase.com` Password: `MetaPass123`.  
    - You can change that in `.env` file.  
    - Metabase doesn't allow easy passwords.  
5. You can start working with `dvdrental` database.  
    https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/  

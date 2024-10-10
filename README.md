# Gym Log

Full Stack Django & React Web App with JWT authentication.

This repo can be used as a starting point for developing a production-ready application using Django, React, and
Postgres in a Dockerized environment with deployment to Heroku.

## Motivation for creating the app

I liked the mobile version of the [strong app](https://www.strong.app/) that allows logging workouts, viewing them, and
getting a list of available exercises. So I implemented the basic functionality of
the [strong app](https://www.strong.app/) in a CRUD Web Application with Django & React.

## Local deployment

1) Install docker: https://docs.docker.com/get-docker/
2) Clone github repo.
3) Run: `docker-compose up --build`.

To access the fronted part of application open [http://localhost:3000](http://localhost:3000) in your browser.

To view `Swagger API endpoints` open [http://localhost:8000/swagger/](http://localhost:8000/swagger/) in your browser.

To view `Django admin site` open [http://localhost:8000/admin/](http://localhost:8000/admin/) in your browser.

## Production deployment

1) [Create Heroku Account](https://signup.heroku.com/dc)
2) [Download/Install/Setup Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)
3) After installation, log into Heroku CLI: `heroku login`.
4) Run: `heroku create <your app name>` to create the Heroku application.
5) Run: `heroku stack:set container` so Heroku knows this is a containerized application.
6) Run: `heroku addons:create heroku-postgresql:hobby-dev` which creates the postgres add-on for Heroku.
7) Set a `SECRET_KEY` in Heroku config vars settings.
8) Set the URL of your application, e.g. `https://<app name>.herokuapp.com`, into environment variable `HOST_NAME` in
   Heroku config vars settings.
9) Deploy your app by running: `git push heroku master`.
10) Go to `<your app name>.herokuapp.com` to see the published web application.

### Main tools and libraries

Backend:

- `Django` as a web framework.
- `Django REST framework` for building web APIs, serialization, and deserialization.
- `JWT authentication` for securely transmitting information between frontend and backend applications.
- `PostgreSQL` as a database in production.

Frontend:

- `React` for building user interface.
- `React Bootstrap` for simplifying the creation and styling of React components.
- `React Query` for managing server state, getting data from the backend, and updating it.
- `Redux` for managing application state. And `Redux Persist` to store state between page reloads.
- `Formik` and `Yup` for object schema validation for login and register pages.

### Ideas for improvement

- Add logic for email confirmation on registration.
- Add logic for password reset on the login page.
- Add internationalization for several languages.

# MyPinterest Project

## Introduction

MyPinterest is a web application developed in Python using the Flask framework. The objective of this project is to replicate some features of the Pinterest platform, allowing users to create profiles, share images and view the main feed with all photos published by other users. The project was developed with the aim of practice and study, using technologies such as Python, Flask, SQLAlchemy to interact with the database, and HTML, CSS and Bootstrap to build the templates.

## Functionalities

- **User Registration**: Users can register on the platform by providing a username, email address and password.
- **Authentication**: The system has an authentication mechanism to ensure that only authenticated users have access to protected functionalities.
- **User Profile**: Each user has a profile where they can add their photos.
- **Main Feed**: Users can view a feed with all photos published by other users.
- **Image Upload**: Users can upload their own images to share with the community.

## Technologies Used

- **Python**: Programming language used to develop the application.
- **Flask**: Web framework used to create the application and manage routes.
- **SQLAlchemy**: ORM (Object-Relational Mapping) library used to interact with the database.
- **HTML, CSS, Bootstrap**: Technologies used to create templates and style the user interface.
- **bcrypt**: Library used to hash passwords for secure storage in the database.
- **Flask-WTF**: Flask extension used to handle web forms.

## Project Structure

The project is structured as follows:

- **routes.py**: Contains the application routes, including the logic for rendering pages, handling forms and interacting with the database.
- **forms.py**: Defines the classes of forms used in the application, using the Flask-WTF extension for data validation.
- **models.py**: Defines the structure of the database tables using SQLAlchemy, including the User and Image tables.
- **templates/**: Directory containing the HTML templates used to render the application pages.
- **static/**: Directory containing static files such as CSS, JavaScript and images.


## Conclusion

MyPinterest is a project designed to practice and study web development with Python and Flask. It offers a simple platform to share images and interact with other users in a similar way to Pinterest. This project can be expanded with new functionality and user interface improvements to create an even richer experience for end users.

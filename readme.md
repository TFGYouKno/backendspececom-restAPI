Lesson 1: Assignment | REST API Design Patterns
Remember to take your time and work through each question diligently! Test your code, make sure it works, and try to find ways to improve. Once you are happy and satisfied with your code, upload it to Github, then turn in your Github link at the bottom of the page!

Don't forget. Make sure this assignment is in it's own repository. Not mixed in with others!

Building a Modular Factory Management System with Flask
Objective: The aim of this assignment is to start development on an E_commerce API, incorporating the Factory Application Pattern, Flask Blueprints for modular design, and implementing API throttling and rate limiting with Flask-Limiter. This assignment will help students understand how to structure large Flask applications, improve code organization, and manage API access efficiently.

Problem Statement: You are tasked with building e_commerece website's api capable of handling the websites customers, products, and orders made by customers. To ensure scalability and maintainability, you need to implement the Factory Application Pattern for configuration and implementation, utilize Flask Blueprints for modular design, and incorporate API throttling and rate limiting using Flask-Limiter. Use the following Models as a base.

Task 1: Implement Factory Application Pattern

Configure the Flask application using the Factory Application Pattern to enable easy configuration and instantiation of the application.
Organize the application structure into modules for better code organization and maintainability.
Project folder
├── app.py
├── config.py
├── database.py
├── controllers
│   ├── __init__.py
├── models
│   ├── __init__.py
│   └── schemas
│       ├── __init__.py
├── requirements.txt
├── routes
│   ├── __init__.py
└── services
    ├── __init__.py
Task 2: Utilize Flask Blueprints for Modular Design

Create Flask Blueprints to modularize different aspects of the factory management system, such as customer management,  product additions and removal, and the creation of orders.
Register these Blueprints with the Flask application to enable modularity and separation of concerns.
-create blueprint for customer, product, and order
- from .blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)
- from .blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)
    return app
Task 3: Implement API Throttling and Rate Limiting

Integrate Flask-Limiter into the application to implement API throttling and rate limiting functionality.
Configure rate limits for different API endpoints to prevent abuse and ensure fair usage of resources.
Task 4: Create Endpoints for CRUD Operations

For the models (Product, Order, Customer), create endpoints for performing Create and Fetching All operations.
Remember there will be a many-to-many relationship between Order and Product which will need to handled with an association table.
Use the REST Resource Naming Conventions to design the endpoint URLs and methods.
Ensure that the endpoints adhere to the principles of RESTful API design, including the use of nouns for resource names, plural nouns for collection names, hyphens to separate words, and lowercase letters.
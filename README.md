# MindLink

## Packages

**app** - our flask application

**app/static** -- utilities for UI

**app/templates** -- html scripts for UI

### Dependencies

To install needed dependencies run 

* pip install -r requirements.txt

## Future reference for project stucture:

mindlink

    /app

        __init__.py

        routes.py

        models.py

        forms.py

    /templates

        layout.html

        index.html

        results.html
        ...

    /static

        /css

        /js

        /img

    config.py

    run.py

**/mindlink:** This is the root directory of your Flask project.

**/app:** This directory contains the core application code.

**init.py:** This file initializes the Flask application and any extensions.

**routes.py:** This file contains the route definitions for your application.

**models.py:** This file contains the database models using SQL.

**forms.py:** This file contains Flask-WTF forms for user input validation.

**/templates:** This directory contains HTML templates that Flask will render to generate dynamic web pages.

**layout.html:** This is the base template that other templates extend from. It typically includes the common structure of your web pages (e.g., header, navigation bar, footer).

**index.html:** Template for the homepage where users can submit their questions or problems.

**results.html:** Template for displaying the results or responses to the user's input.

**/static:** This directory contains static files such as CSS, JavaScript, and images.

**/css:** Store your CSS files here.

**/js:** Store your JavaScript files here.

**/img:** Store image files here.

**config.py:** This file contains configuration variables for your Flask app, such as database URI, secret key, etc.

**run.py:** This file is used to run your Flask application. It initializes the Flask app and starts the development server.



# yardwrk - Job Finding App

Yardwrk creates an an easy to use interface where cache valley residents can post outside jobs/chores that need to be performed in exchange for payment. Individuals (especially teenagers and young people) looking to earn money can sign up and complete these jobs.

## Workspace Layout

Documentation for this project will be stored in the *docs* folder. This will contain the project plan, use case diagrams, and others as the project progresses.

The project itself will be kept in the *app* folder.

## Version Control Procedures

We will be using git for version control on this project. We will meet up often to discuss changes that we make to the app, check up on what each of us is contributing, and resolve any conflicts (merge conflicts, disagreements about the direction we are taking the app, etc.).

Contributors will have access to David Storey’s repository, and will have access to commit, push, and pull as the development process demands. Branches should be committed and pushed, but not merged until they are reviewed in a team meeting.

## Tool Stack Description and Set Up Procedure

We will be using Django, a back-end python web framework, as the main framework for this project. Django will handle all of the back-end functions, including all database related actions. We will also utilize technologies such as CSS, HTML5, and JavaScript in conjunction with this framework.

We will use front-end frameworks like Bootstrap and Vue. These front end frameworks that will help us make the site look good. Bootstrap is good for mobile minded design, and Vue is lightweight and useful for a simpler design.

## Build Instructions

Clone repository

    git clone git@github.com:davevstorey/9-usu-cs3450-sp2022.git

Initialize Database

    python manage.py migrate

Create Admin Account

    python manage.py createsuperuser

Add models to Database

    python manage.py makemigrations app-name

Update Database with new additions

    python manage.py migrate

Start server

    python manage.py runserver

> The **Create Admin Account** instruction will prompt you to enter your desired identification/authorization information for the admin account

> In the **Add models to Database** instruction includes *app-name* as a parameter. This will be updated later with the actual project name.

## Unit Testing Instructions

For unit testing, we will be using the python's *unittest* library. Documentation for this library can be found at https://docs.python.org/3/library/unittest.html. To run the tests, run *unittests.py* with the tests you want to run as command line arguments. No command line arguments will lead to all tests running.

## System Testing Instructions

For system testing, launch the app in the browser. You'll be able to navigate around the site and test it as any actor.

You will also be able to check that the graphic and user interface parts of the app are working correctly.

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

Navigate to App

    cd 9-usu-cs3450-sp2022/app/yardWrk/
    
Pip Install Python Dependencies

    pip install django-crispy-forms
    pip install django-phonenumber-field[phonenumberslite]
    pip install lorem

Initialize Database

    python manage.py makemigrations
    python manage.py migrate

Start server

    python manage.py runserver

Navigate to yardWrk

    http://127.0.0.1:8000/yardsite/

## Accessing the owner account.

For accessing the owner account, log in with username: owner , and password: password .

Afterwords you have the ability to change account information from inside the app.

## System Testing Instructions

For system testing, launch the app in the browser. You'll be able to navigate around the site and test it as any actor. You can go to the docs folder and find the SystemTesting document. That will have detailed tests and the requirements they fulfill.

You will also be able to check that the graphic and user interface parts of the app are working correctly. 

## Sprint Reports

Sprint reports are found by navigating to the following directory.

    docs/Cs3450StandUps

## Rubric.md

For the rubric entailing how we finished each requirement on the assignment navigate into docs

    docs/rubric.md

## Project Plan

# Summary

The goal of this project is to create a website that allows customers to hire individuals to do various yard working jobs. Customers will submit jobs that they want done, and workers will be able to accept these jobs in exchange for money. This app will mainly target pc users, but will accommodate mobile users as well. Website owners will receive 10% of all transactions.

# Team Organization

- Project Manager: Quinn Ormond (We plan on rotating the position)
- Designers and Developers: David Storey, Ian Adams, and Jake Epperson

# Overall Software Development Process (provided by the instructor)

- Each phase will be a little like a Sprint in an Agile method and a little like an iteration in a Spiral process.  Specifically, each phase will be like a Sprint, in that work to be done will be organized into small tasks, placed into a sprint backlog, and prioritized.   Then, using on time-box scheduling, the team will decide which tasks the phase (Sprint) will address.  The team will use a GitHub Repository to keep track of tasks (issues) in the product backlog. Those tasks that will be part of the current Sprint will be kept in the GitHub Project, those in progress, and those that are done.

- Each phase will also be a little like an iteration in a Spiral process, in that each phase will include some risk analysis and that any development activity (requirements capture, analysis, design, implementation, etc.) can be done during any phase.  Early phases will focus on understanding (requirements capture and analysis) and subsequent phases will focus on design and implementation.  Each phase will include a retrospective.

# Policies, procedures, or tools for communication, including plans for team meetings, online-coordination, reporting, etc.

- Discord for text and voice communication.
- Google Drive for storing files and writing documentation.
- Github Repository for project files, version control, and communication with Professor Dan Watson and Rob Johnson.
- app.diagrams.net for creating visual diagrams.

# Risk analysis
- Database Structure: We are using Django for all database related tasks within this application. Django is a well built back-end framework that is currently being supported with bug-fixes/patches. Django also uses an object relational mapper which provides extra security from certain attacks. Our database will be quite secure. However, if it was hacked the consequences would be extremely bad. All customer data would be compromised, and the application may even stop working depending on the severity of the hack. A workaround we could use is to backup the database files at certain time intervals on the server. This feature is essential for our application to work.
- Host Server: The possibility of a security issue occurring in the host server is low. However, if an issue occurred there would be notable consequences. The entire service could go down, rendering the project useless. We could workaround this issue by using a professional hosting service that is more reliable than one person’s hosting machine. 
- User Authentication: While it is unlikely that user authentication errors may occur it is important that we handle them accordingly. Such errors could prevent users from entering and using the application as intended leading to an unsatisfactory or even harmful experience. Django’s built-in 'django.contrib.auth' library will be used to ensure that user authentication is handled safely and securely.
- User Interface: The probability of security concerns through the user interface is rather low. The user interface will be created through django which is generally quite safe to create and use as previously mentioned. Successful hacks or other problems to the user interface will cause the user to be unable to interact with the system in a meaningful manner. There is not a work around to this though as the user interface is a mandatory insertion to this project.
- Job Assignment System: As previously mentioned, the technologies we are using are up-to-date and secure, so the likely-hood of this system being compromised is very low. If this were to be hacked, the severity would be at medium levels. Some user data may be compromised, but the bigger problem would be that the application wouldn’t work properly. Customers wouldn’t be able to get their requests fulfilled.
- Job Fulfillment System: The job fulfillment system, although unlikely to be a major cause for concern, could be more damaging if issues were to occur. This would be when a worker would be getting paid so issues occurring here could cause payment leak or payment delay. Creating large irritations. There is not a great work around though as payment is still necessary for the website to function.
- reference to the README.md for the configuration management plan
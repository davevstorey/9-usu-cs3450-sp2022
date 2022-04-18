# Requirements Definition

## Introduction and Context

Homeowners of Cache valley have a lot to worry about. Their careers, family, hobbies, and house
Upkeep takes up all the time they have in a given day. In this day and age there should be a way for the average
Cache valley homeowner to take a much needed break. There are parents in this beautiful valley trying to find
Ways to instill a hard working spirit in their children. Our application, yardwrk, aims to satisfy these needs.

yardwrk connects homeowners to a plethora of individuals willing to do outside house chores for a fee 
Set by the homeowner. This way, the homeowner can have more free time in their day, while the workers doing 
The task may earn money and work experience.

Homeowners will be able to post different jobs such as lawn mowing, leaf raking, and snow shoveling to 
The application. The potential workers will look through the list of available jobs, and sign up for one. The
Homeowners will have the ability to review the worker to accept or reject them. If the worker is 
accepted, they will be given the customers contact information and be expected to show up and do the job.

Finally, the worker can submit the job being finished allowing the customer to review their work and pay 
them for their work. This reviewing system will allow all customers to be able to pick and choose who they would
like doing the work based on previous customers' reviews. They will also have the capability to blacklist a worker
if they had a terrible experience with the worker.

By connecting customers in need of lawn care or other similar tasks with workers we hope to provide
working opportunities to young individuals across Cache valley, while also clearing yards for those who don’t
want to do it themself.

## Users and their Goals

* Owner - Admin of the site, will be able to edit available jobs and assign user permissions.
* Customer - Posts jobs that they want completed in exchange for money.
* Worker - Accepts posted jobs and completes them in exchange for money.

## Functional Requirements

1. User Authentication and Access\
&emsp;1.1 User must be able to navigate to log in page\
&emsp;1.2 User must be able to log in using username and password\
&emsp;&emsp;1.2.1 User cannot login if information is incorrect\
&emsp;1.3 User must be able to create a new account\
&emsp;&emsp;1.3.1 User will be taken to a new page to create a new account\
&emsp;&emsp;1.3.2 Accounts with duplicate user names will not be allowed\
&emsp;&emsp;1.3.3 Accounts with duplicate emails will not be allowed\
&emsp;&emsp;1.3.4 Accounts with invalid emails will not be allowed\
&emsp;&emsp;1.3.5 Accounts with invalid phone numbers will not be allowed\
&emsp;1.4 Users are authorized to have a mix any of the following features and rights\
&emsp;&emsp;1.4.1 All users should have access to both customer profile features and worker profile features. Given to them in two separate windows.\
&emsp;&emsp;1.4.2 Users with owner status will have access to all customer, worker, and owner profile features.\
2. User Profile Features\
&emsp;2.1 Users will be able to have any combination of the following types: Worker, Customer, Owner\
&emsp;2.2 User will be able to edit their account information\
&emsp;&emsp;2.2.1 User will be able to edit their name\
&emsp;&emsp;2.2.2 User will be able to edit their address\
&emsp;&emsp;2.2.3 User will be able to edit their zip code\
&emsp;&emsp;2.2.4 User will be able to edit their phone number\
&emsp;&emsp;2.2.5 User will be able to edit their username\
&emsp;&emsp;2.2.6 User will be able to edit their email\
&emsp;&emsp;2.2.7 User will be able to edit their city\
&emsp;&emsp;2.2.8 User will be able to edit their state\
&emsp;&emsp;2.2.9 User will be able to change password information\
&emsp;2.3 Worker Profile Features\
&emsp;&emsp;2.3.1 User will be able to accept jobs\
&emsp;&emsp;2.3.2 User will be able to receive money\
&emsp;&emsp;2.3.3 User will be able to view job information from the worker dashboard\
&emsp;&emsp;2.3.4 User will be able to view a list of all assigned jobs to the current user\
&emsp;&emsp;2.3.5 User will be able to view a list of all available jobs to take.\
&emsp;&emsp;2.3.6 User will be able to view a list of jobs they have completed.\
&emsp;&emsp;2.3.7 User will be able to complete a job.\
&emsp;2.4 Customer Profile Features\
&emsp;&emsp;2.4.1 User will be able to post jobs\
&emsp;&emsp;2.4.2 User will offer money for jobs\
&emsp;&emsp;2.4.3 User will be able to load money on their account\
&emsp;&emsp;2.4.4 User will be able to delete their pending jobs\
&emsp;&emsp;2.4.5 User’s job posts will be primarily shown to workers in their area\
&emsp;&emsp;2.4.6 User will be able to view all information on their jobs\
&emsp;&emsp;2.4.7 User will be able to edit job information\
&emsp;&emsp;2.4.8 User will be able to view a list of jobs they created\
3. Owner Profile Features\
&emsp;3.1 Owner will be able to change between profile types\
&emsp;3.3 Owner will be able to edit transactions\
&emsp;&emsp;3.3.1 Take money out of a worker’s account\
&emsp;&emsp;3.3.2 Take money out of a customer’s account\
&emsp;&emsp;3.3.3 Put money into a worker’s account\
&emsp;&emsp;3.3.4 Put money into a customer’s account\
&emsp;3.4 Owner will be able to escalate other users to owner status.\
&emsp;3.5 Owner will be able to create new job/task descriptions (i.e. washing windows, etc.)\

## Non-functional Requirements

* Non-functional Requirements
    * Database System (SQLite)
        * Models
            * Account
                * Username
                * Email
                * Phone Number
                * Password (handle securely!)
                * Address
                * Zip Code
                * Privileges (owner, worker, customer)
            * Work Post
                * Username
                * Contact information
                * Job Description
                * Accepted
                * Completed
            * Review
                * Worker
                * Job Description
                * Rating
                * Review Comment
  * Version Control System (Git)
  * Application is deployable
    * Deployable locally
    * Deployable using a third party hosting service
  * Front-end (UI)
    * Web-browser compatibility
    * Mobile device compatibility
    * Accessibility

## Future Features

* Map Integration
* Email Notifications
* Phone push notifications
* Debit and Credit Card transactions

## Glossary

* Customer: User who posts jobs to the website
* Django: Back-end web framework for Python
* Owner: User who has administrative privileges
* User: Anyone who uses the website
* Worker: User who does the jobs listed on the website







[![Build Status](https://travis-ci.org/JBroks/unicornattractor_issue_tracker.svg?branch=master)](https://travis-ci.org/JBroks/unicornattractor_issue_tracker)

# Unicorn Attracktor Tracker - issue tracker application

## Project Intro
Stream Four Project: Full Stack Frameworks with Django - Milestone Project

![alt text](https://github.com/JBroks/unicornattractor_issue_tracker/blob/master/design/gif/unicornattractor.gif "Gif")

This project is part of the 'Full Stack Frameworks with Django' module of the Code Institute Full Stack Software Development course.

## Project Scope
To complete this module the task was to create an issue tracking application that allows users to submit their tickets.

Users are allowed to submit two types of tickets i.e. bugs and features. In order to prioritize their tickets users are able to upvote them. The more upvotes a ticket has the faster it will be look after by a developer. However, the difference is that bugs can be upvoted for free, while user has to donate minimum €5 to upvote a feature. Users are also able to comment on tickets.

Additional features were developed, these include: data dashboard, forum, like / dislike mechanism for forum, search bar.

## Project Overview

Project consists of the following sections:

**1. Homepage** - Containing 'Sign up' button when user is not authenticated and 'Add ticket' and 'Forum' buttons when user is logged into his / her account. Home page also contains description of main tracking app features, about Unicorn Attractor app section and Apple / Google store badges.

**2. Sign in form** - Page containing the form that enables user to log into their account to use the app.

**3. Sign up form** - Page containing the form that enables user to sign up for the Unicorn Attractor Issue Tracking app.
 
**4. All tickets page** - Page containing paginated tickets and filters that enable user to filter tickets by type and status.

**5. Single ticket view page** - Page containing a detail information about a given ticket, a comment form and paginated comments.

**6. Add / edit ticket page** - Page containing add / edit ticket form.

**7. Forum page** - Page containing paginated forum threads.

**8. Thread view page** - Page containing a single thread and all associated posts.

**9. Add / edit thread page** - Page containing add / edit thread form.

**10. Data dashboard page** - Page containing summary statistics and charts presenting analysis of all tickets submited by app users.

**11. Search results page** - Page containing any application content that matches the search term.

**12. Profile page** - Page containing user information, such as username, last seen (date and time), and all content that a given user added, commented, upvoted, liked or disliked.

**13. Edit profile page** - Page containing edit profile form that enables a user to upload a profile photo and update any personal information.

**14. Reset password pages** - Pages that display instructions on password reset and password reset form.

## Table of Contents

- [Demo](#demo)
- [UX](#ux)
- [Database](#database)
- [Features](#features)
- [Technologies used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

<a name="demo"/>

## Demo

Website demo is available [here](https://unicornattractor-issue-tracker.herokuapp.com/ "unicornattractor-issue-tracker").

<a name="ux"/>

## UX

### UX Design

In this project I was aiming to achieve a simple and user friendly user design, while providing all required information. All sections are arranged in a logical order to provide intuitive user experience e.g. any content that users can review is placed under 'Explore' menu, while forms for creating new content are placed under 'Create' menu.

In keeping with the unicorn theme I decided on blue (`#2e3190`), purple (`#5854a5`, `#bcb3bf`), pink (`#e89e93`, `#fcdcd7`) pallete of colors. Additionally yellow (`#fcd731`), green (`#63d37b`), red (`#ee5140`) colors were used for the data dashboard and back to top button.

### Target Audience

This app was created to serve users of the (fictional) sourcing and recruiting application called "Unicorn Attractor". This application enables these users to submit any tickets describing the existing bugs and issues that they are having, as well as suggest any new features to be implemented.

Therefore, th main objective of the website is to provide a user with a tool that will enable them to submit tickets, upvote and donate for any features, comment tickets, create forum threads / posts, like threads / posts, review ticket statistics.

### User Stories

The following user stories were used to design this project:

**User Story 1:** As a user I would like to create an account to access all the app features such as e.g. ticket creation.

**User Story 2:** As a user I would like to be able to delete my account and all content added by me at any point.

**User Story 3:** As a user I would like to have an option to login and logout of my account so nobody else can access it.

**User Story 4:** As a user I would like to be able to add a ticket of any of both types (bug or feature).

**User Story 5:** As a user I would like to be able to donate to support any feature of my choice.

**User Story 6:** As a user I would like to be able to add a new or remove my upvote.

**User Story 7:** As a user I would like to be able to comment on any ticket submitted by me or any other user.

**User Story 8:** As a user I would like to be able to filter out specific tickets depending on their type or status.

**User Story 9:** As a user I would like to be able to search through the website content.

**User Story 10:** As a user I would like to be able to start a new discussion on the website's forum.

**User Story 11:** As a user I would like to be able to express my opinion on threads / post via like / dislike system.

**User Story 12:** As a user I would like to have an overview on the ticket progress and overall statistics.

**User Story 13:** As a user I would like to see all of my inputs within the app (i.e. tickets, comments, upvotes, likes / dislikes, threads, posts) in case I would like to edit or delete them.

**User Story 14:** As a user I would like to be able to edit my profile information.

**User Story 15:** As a user I would like to be able to reset my password in case I forget it.

### Mockups & Wireframes

The following wireframe sketches were created to design the project layout options for:

- [large](https://github.com/JBroks/unicornattractor_issue_tracker/blob/master/design/wireframes/unicornAttractor_large.pdf),

- [medium](https://github.com/JBroks/unicornattractor_issue_tracker/blob/master/design/wireframes/unicornAttractor_medium.pdf), and 

- [mobile displays](https://github.com/JBroks/unicornattractor_issue_tracker/blob/master/design/wireframes/unicornAttractor_mobile.pdf).

<a name="database"/>

## Database

### Database Type

#### SQLite

SQLite is a simple, very lightweight database management system used for the project to store data locally and test my application.

#### PostgreSQL

Heroku's PostgreSQL relational database was used for the project to store the data for the deployed application.

My database consists of the following tables: users, user profiles, tickets, comments, upvotes, donations, threads, posts, thread votes, post votes.

### Database Design

Picture below presents the database schema outlining structure of each collection and relationship between each collection.

![alt text](https://github.com/JBroks/unicornattractor_issue_tracker/blob/master/design/database-design/db-schema.png "database-schema")

The main point of database schema preparation was to think through the structure of each Django model. Django model is then coverted into SQL code and creates the database tables and fields.

The example of Django model below:
```python
class Ticket(models.Model):
    '''
    Ticket model that will store all the fields below in a tabel called 'Ticket'
    '''
    TYPE_CHOICES = (
        ('Bug', 'Bug'),
        ('Feature', 'Feature'),
        )
    STATUS_CHOICES = (
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Closed', 'Closed'),
        )
    
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE)
    ticket_type = models.CharField(
        max_length=7,
        choices=TYPE_CHOICES)
    ticket_status = models.CharField(
        max_length=11,
        choices=STATUS_CHOICES)
    subject = models.CharField(
        max_length=100,
        blank=False)
    description = models.TextField(
        max_length=30000,
        blank=False)
    date_created = models.DateTimeField(
        blank=False,
        null=False,
        auto_now_add=True)
    date_updated = models.DateTimeField(
        blank=False,
        null=False,
        auto_now=True,
        )
        
    class Meta:
        ordering = ['-id']
```

<a name="features"/>

## Features

### Existing Features

The project consists of various features presented below.

#### Page loading

- **Spinner** - jQuery method `show()` and `hide()` was used to create spinner showing while page is loading;

- **Overlay** - overlay that fades out the background while page is loading;

#### Buttons

- **App Store/Google Play Buttons** - buttons load Apple App Store / Google Play store in a new browser tab. Since the Unicorn Attractor app is not a real application buttons redirect user to the homepage of each store;

- **Sign Up Button** - this buttons redirects a user to the registration page, where they can sign up for a new account;

- **Sign In Button** - this button redirect a user to the login form page where he or she can log into their account;

-  **Sign Out Button** - this button allows a user to log out of their account. When button is clicked the user session ends end they are redirected to the homepage;

- **Add Ticket / Thread Buttons** - these buttons redirect user to the add ticket / add thread page, where they can add a new ticket / a new thread;

- **Add Ticket / Forum / Sign Up Buttons on Jumbotron** - these buttons are placed on the jumbotrone that contains a welcome message. Unauthenticated users will see Sign Up button on the jumbotrone, while authenticated users will see Add Ticket and Forum button;

- **Back to Forum Button** - this button is available on the page that contains a single thread view. It enables user to go back to the forum table view;

- **Back to Top Button** - static back to top button was implemented at the bottom of the page so user can go back to the top of the page without scrolling back. The feature is especially useful on mobile devices;

- **View / Edit / Delete Button** - favicons were used to create view / edit / delete buttons that enable user to take an appropriate action when it comes to tickets / threads / posts;

- **Show more / Show less buttons** - buttons used to toggle Bootstrap class="truncate" to manage very long comments;

- **Form Buttons** -  each form was supplied with a Cancel and Sumbit  / Save  button. Cancel button enables users to get out of the edit, delete or create a new content mode, while Submit / Save button enable user to approve the action;

- **Like / Dislike button** - voting buttons enabling user to like or dislike a thread or a post;

- **Upvote / Downvote** - upvote buttons enables user to upvote any ticket, however a small donation is required when upvoting a feature. Users can remove their upvote by clicking downvote button that will appear after a ticket was upvoted by a given user;

- **Filter button** - button applies filters specified by a user;

- **Reset filter** - button that resets all filters and shows all tickets;

#### Forms

- **Sign Up Form** -  registration form that enables user to use the app. User input includes first name, last name, username, email address, and password (that has to be repeated);

- **Sign In** - login form that enables user to sign into the user account;

- **Reset Password Forms** - a set of forms that include instructions on how to reset a password. First form asks for the user's email address so an email with the reset password link can be send. User then clicks the link and gets to the page where he or she can set up a new password. When the process is successful message appears informing the user that they are now able to sing into their account;

- **Edit Profile Details Form** - at any point user can upload their profile image and update any personal details by using the Update Profile Form;

- **Add Comment / Post Form** - users can post their comments for each ticket, and posts for each forum thread by using these forms;

- **Add Ticket / Thread Form** - users are able to add a ticket / thread by filling out the appropriate form. Add Ticket Form requests information such as ticket type, subject and description. Add Thread Form requires only subject and description;

- **Edit Comment / Post Form** - users are able to edit any comment / post created by them by clicking edit icon displayed in the comment's / post's card header. When edit button is clicked the displayed comment / post disappears and editable text form appears;

- **Edit Ticket / Thread Form** - edit ticket / thread form displays information about a given ticket / thread in the eaditable format. User can edit any ticket / thread earlier added by them;

- **Donation Form** - donation form pops up when a user tries to upvote a feature. Donation uses Stripe API to process the payment;

#### Structure

- **Navbar** - the navbar stays collapsed on medium and small devices. To create Bootstrap mobile collapsed button `class="collapse navbar-collapse"` was applied. The navbar contains brand logo and links to associated sections i.e. Home, Explore, Create, Account / Profile;

- **Footer** - contains disclaimer GitHub link and copyrights information;

#### Alerts

- **Toast messages** - **Bootstrap** toasts were used to style flash messages and present them as toast messages to the user;

- **Delete confirmation alerts** - alerts created using **Bootstrap** framework modals that asks user to confirm deletion.

#### Other

- **Pagination** - flask paginations styled with Bootstrap classes is used for the project to paginate content such as tickets, threads, post, comment etc.;

- **Accordion** - Bootstrap accordion feature that stores user personal information, activity, delete profile and update profile buttons on user profile page (mobile displays only);

- **Pills** - Bootstrap pills were used to organise content and create a neat and compact look. Pills were implemented on the profile page, search results page and inside some cards on the dashboard page;

- **Bootstrap cards** - feature used to present comments / posts added by users and charts & statistics on data dashboard;

- **Search bar** - search bar that enables users to search any ticket, comment, thread, and post.

- **Jumbotron** - Bootstrap jumbotrone is used to prominently display a welcome message on the homepage;

- **Filter** - filter fields were created so users can select only tickets within a specific type and / or status;

- **Highcharts charts** - data dashboard uses Highcharts API to display analysis of tickets by type and status using a pie chart and stacked bar chart elements.

### Features left to implement

List of features to be implemented in the future:

- additional filters by e.g. a user who added it, by date added;

- adding information on how many views each ticket or forum thread has;

- contact us form or report to admin functionality;

- notifications for users so they know e.g. if the feature they supported is being developed;

- notification for users that the content that they added is being liked or upvoted.

<a name="technologies-used"/>

## Technologies used

### Programming languages

- **HTML** - the project used HTML to define structure and layout of the web page;

- **CSS** - the project used CSS stylesheets to specify style of the web document elements;

- **JavaScript** - the project used jQuery as the primary JavaScript functionality. JavaScript is also used to implement Stripe and Highcharts APIs;

- **Python** - the project back-end functions are written using Python. Django and Python is used to build views functions;

### Libraries

- [jQuery](https://code.jquery.com/jquery-3.4.1.min.js) - used to initialize elements of Bootstrap framework, to manage spinner overlay (fade out), back to top button (smooth scroll), read more / less button, reset filters button, navbar hide / show effect;

- [Bootswatch](https://bootswatch.com/) - the project used Bootswatch "LUX" theme for setting styling for all pages;

- [Font Awesome](https://fontawesome.com/v4.7.0/) - various Font Awesome icons were used for the project;

### Frameworks & Extensions

- [Bootstrap](https://getbootstrap.com/) - the project used Bootstrap to create nice grid layout, and position elements within grids. The framework was also used to create and customize the navbar element and implement various elements such as modals, tooltips, pills etc.;

- [Django](https://www.djangoproject.com/) - python-based free and open-source web framework that follows the model-template-view architectural pattern;

- [django-forms-bootstrap](https://pypi.org/project/django-forms-bootstrap/) - used to style django form with Bootstrap styling;

- [django-storages](https://django-storages.readthedocs.io/en/latest/) and [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - both packages used to connect Django to S3;

### Database

- [Postgres](https://www.heroku.com/postgres) - a relational database management systems hosted on Heroku;

- **SQLite** - a lightweight database management system used when running and testing app locally;

### API

- [Highcharts](https://www.highcharts.com/) - Charting API used to create interactive charts for the data dashboard;

- [Stripe API](https://stripe.com) - Stripe was used to make secure payments when users upvote features.

### Other

- [Gifox](https://gifox.io/) - Tool was used to record the gif presented in the demo section of this README files;

- [Multi Devices Mockup Generator](https://techsini.com/multi-mockup/) - Online tool was used to display the project on various devices;

- [MockFlow WireframePro](https://www.mockflow.com/) - Online tool that was used to create wireframes;

- [DBDiagram](https://dbdiagram.io/home) - A relational database diagram design tool used to create database schema;

- [Placeholder](https://placeholder.com/) - Online tool to create custom placeholder images. It was used to create image placeholder in cases when user did not upload his / her profile image;

- [npm](https://getbootstrap.com/docs/4.0/getting-started/webpack/) - Bootstrap and Bootswatch theme installed as a Node.js module using npm to customize SCSS;

- [Popper](https://popper.js.org/) - **jQuery** and **Popper** are Bootstrap's peerDependencies and had to be added to enable me to customize the SCSS;

<a name="testing"/>

## Testing

### Code validation

#### CSS

CSS code was validated using the [W3C CSS Validation Service - Jigsaw](https://jigsaw.w3.org/css-validator/). It is important to mention that I only validated my custom code and not the Bootstrap modules.

No errors were found in the code.

#### HTML

HTML code was validated using the [W3C Markup Validation Service](https://validator.w3.org/).

The following issues were captured by the validator:

- For most of the templates this issue appeared:
    ```
    Section lacks heading. Consider using h2-h6 elements to add identifying headings to all sections.
    ```
    This warning was ignored as no additional heading is required.
    
- The following issue was highlighted for the homepage template:
    ```
    Consider using the h1 element as a top-level heading only (all h1 elements are treated as top-level headings by many screen readers and other tools).
    ```
    This warning was ignored as h1 was purposely put by me inside the jumbotrone element.

All warnings related to Jinja templates syntax were ignored as they are not recognised by the HTML validator.

#### JavaScript

JavaScript code was validated using [JSHint](https://jshint.com/).

Validator has indicated that there are two unknown / undefined variables, namely `$`, and `Stripe`. The warning was ignored as I believe it is due to the fact that these libraries are separated and the validator does not have access to them.

#### Python

Python code was validated using[PEP8 Online](http://pep8online.com). All errors and warnings were fixed to validate the code agains the PEP8 requirements.

The only warning that was not fixed in some cases was the following:
```
blank line contains whitespace
```

This issue apppeared when I added spaces between some blocks of code to make it more readable, which is allowed as per the following PEP8 rule:
**"Extra blank lines may be used (sparingly) to separate groups of related functions."**

### Travis Continuous Integration

....

### Automated testing

.....testing and coverage description....

### Features testing

.....

### Responsiveness testing

.......

#### Bugs:

....

### Peer-code-review

.....

#### Bugs

....

### User stories testing

**User Story 1:**

- Solution:  .......

**User Story 2:**

- Solution:  .......

<a name="deployment"/>

## Deployment

### GitHub

....

### Heroku

.....

<a name="credits"/>

## Credits

### Content

....

### Media

....

### Acknowledgements

....

### Disclaimer

*This is for educational use.*
[![Build Status](https://travis-ci.org/JBroks/unicornattractor_issue_tracker.svg?branch=master)](https://travis-ci.org/JBroks/unicornattractor_issue_tracker)

# Unicorn Attracktor Tracker - Issue Tracker Application

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

1. [Demo](#demo)
2. [UX](#ux)
    - [UX Design](#ux-design)
    - [Target Audience](#target-audience)
    - [User Stories](#user-stories)
    - [Mockup & Wireframes](#wireframes)
3. [Database](#database)
    - [Database Type](#database-type)
    - [Database Design](#database-design)
4. [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left To Implement](#features-left)
5. [Technologies Used](#technologies-used)
    - [Programming Languages](#programming-languages)
    - [Libraries](#libraries)
    - [Frameworks & Extensions](#frameworks)
    - [Database](#tech-database)
    - [API](#API)
    - [Version-control System](#ver-control-system)
    - [Hosting](#hosting)
    - [Other](#tech-other)
6. [Testing](#testing)
    - [Code Validation](#code-validation)
    - [Travis Continuous Integration](#travis)
    - [Automated Testing](#auto-testing)
    - [Functionality Testing](#functionality-testing)
    - [Responsiveness Testing](#responsiveness-testing)
    - [Peer-code-review & Additional Testing](#additional-testing)
    - [User Stories Testing](#us-testing)
    - [Interesting Bugs - Resolved](#resolved-bugs)
    - [Unresolved Bugs](#unresolved-bugs)
7. [Deployment Process](#deployment-process)
    - [AWS S3 Bucket](#S3)
    - [Version Control](#version-control)
    - [Running Code Locally](#run-code-locally)
    - [Deployment](#deployment)
8. [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)
    - [Disclaimer](#disclaimer)

<a name="demo"/>

## Demo

Website demo is available [here](https://unicornattractor-issue-tracker.herokuapp.com/ "unicornattractor-issue-tracker").

<a name="ux"/>

## UX

<a name="ux-design"/>

### UX Design

In this project I was aiming to achieve a simple and user friendly user design, while providing all required information. All sections are arranged in a logical order to provide intuitive user experience e.g. any content that users can review is placed under 'Explore' menu, while forms for creating new content are placed under 'Create' menu.

In keeping with the unicorn theme I decided on blue (`#2e3190`), purple (`#5854a5`, `#bcb3bf`), pink (`#e89e93`, `#fcdcd7`) pallete of colors. Additionally yellow (`#fcd731`), green (`#63d37b`), red (`#ee5140`) colors were used for the data dashboard and back to top button.

<a name="target-audience"/>

### Target Audience

This app was created to serve users of the (fictional) sourcing and recruiting application called "Unicorn Attractor". This application enables these users to submit any tickets describing the existing bugs and issues that they are having, as well as suggest any new features to be implemented.

Therefore, the main objective of the website is to provide a user with a tool that will enable them to submit tickets, upvote and donate for any features, comment tickets, create forum threads / posts, like threads / posts, review ticket statistics.

<a name="user-stories"/>

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

<a name="wireframes"/>

### Mockups & Wireframes

The following wireframe sketches were created to design the project layout options for:

- [large](https://github.com/JBroks/unicornattractor_issue_tracker/blob/master/design/wireframes/unicornAttractor_large.pdf),

- [medium](https://github.com/JBroks/unicornattractor_issue_tracker/blob/master/design/wireframes/unicornAttractor_medium.pdf), and 

- [mobile displays](https://github.com/JBroks/unicornattractor_issue_tracker/blob/master/design/wireframes/unicornAttractor_mobile.pdf).

<a name="database"/>

## Database

<a name="database-type"/>

### Database Type

#### SQLite

SQLite is a simple, very lightweight database management system used for the project to store data locally and test my application.

#### PostgreSQL

Heroku's PostgreSQL relational database was used for the project to store the data for the deployed application.

My database consists of the following tables: users, user profiles, tickets, comments, upvotes, donations, threads, posts, thread votes, post votes.

<a name="database-design"/>

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

<a name="existing-features"/>

### Existing Features

The project consists of various features presented below.

#### Page Loading

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

- **Login modal popups** - when user is not authenticated and treis to e.g. like a post or add a comment a pop up will appear asking him or her to sign in first;

#### Other

- **Pagination** - flask paginations styled with Bootstrap classes is used for the project to paginate content such as tickets, threads, post, comment etc.;

- **Accordion** - Bootstrap accordion feature that stores user personal information, activity, delete profile and update profile buttons on user profile page (mobile displays only);

- **Pills** - Bootstrap pills were used to organise content and create a neat and compact look. Pills were implemented on the profile page, search results page and inside some cards on the dashboard page;

- **Bootstrap cards** - feature used to present comments / posts added by users and charts & statistics on data dashboard;

- **Search bar** - search bar that enables users to search any ticket, comment, thread, and post.

- **Jumbotron** - Bootstrap jumbotrone is used to prominently display a welcome message on the homepage;

- **Filter** - filter fields were created so users can select only tickets within a specific type and / or status;

- **Highcharts charts** - data dashboard uses Highcharts API to display analysis of tickets by type and status using a pie chart and stacked bar chart elements.

<a name="features-left"/>

### Features Left to Implement

List of features to be implemented in the future:

- additional filters by e.g. a user who added it, by date added;

- adding sorting feature to tables;

- adding information on how many views each ticket or forum thread has;

- adding function that will resize profile photos to avoid issues with images when displayed inside of cards, navbar and profile page;

- adding more charts and statistics that would show how tickets are resolved over time (week, month, year);

- contact us form or report to admin functionality;

- notifications for users so they know e.g. if the feature they supported is being developed;

- notification for users that the content that they added is being liked or upvoted.

Additionally, I am planning to upgrade my app to Django v3 and Stripe v3 when I have more time.

<a name="technologies-used"/>

## Technologies Used

<a name="programming-languages"/>

### Programming Languages

- **HTML** - the project used HTML to define structure and layout of the web page;

- **CSS** - the project used CSS stylesheets to specify style of the web document elements;

- **JavaScript** - the project used jQuery as the primary JavaScript functionality. JavaScript is also used to implement Stripe and Highcharts APIs;

- **Python** - the project back-end functions are written using Python. Django and Python is used to build views functions;

<a name="libraries"/>

### Libraries

- [jQuery](https://code.jquery.com/jquery-3.4.1.min.js) - used to initialize elements of Bootstrap framework, to manage spinner overlay (fade out), back to top button (smooth scroll), read more / less button, reset filters button, navbar hide / show effect;

- [Bootswatch](https://bootswatch.com/) - the project used Bootswatch "LUX" theme for setting styling for all pages;

- [Font Awesome](https://fontawesome.com/v4.7.0/) - various Font Awesome icons were used for the project;

<a name="frameworks"/>

### Frameworks & Extensions

- [Bootstrap](https://getbootstrap.com/) - the project used Bootstrap to create nice grid layout, and position elements within grids. The framework was also used to create and customize the navbar element and implement various elements such as modals, tooltips, pills etc.;

- [Django](https://www.djangoproject.com/) - python-based free and open-source web framework that follows the model-template-view architectural pattern;

- [django-forms-bootstrap](https://pypi.org/project/django-forms-bootstrap/) - used to style django form with Bootstrap styling;

- [django-storages](https://django-storages.readthedocs.io/en/latest/) and [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - both packages used to connect Django to S3;

- [bootstrap-select](https://developer.snapappointments.com/bootstrap-select/examples/#styling) - jQuery plugin was used to style selectmenu;

<a name="tech-database"/>

### Database

- [Postgres](https://www.heroku.com/postgres) - a relational database management systems hosted on Heroku;

- **SQLite** - a lightweight database management system used when running and testing app locally;

<a name="API"/>

### API

- [Highcharts](https://www.highcharts.com/) - charting API used to create interactive charts for the data dashboard;

- [Stripe API](https://stripe.com) - Stripe was used to make secure payments when users upvote features;

<a name="ver-control-system"/>

### Version-control System

- **Git**- git was used as a version control system to add and commit changes made to the project in AWS Cloud9. All committed changes were then pushed to remote repository on GitHub;

- [GitHub](https://github.com/) - GitHub was used as a remote repository to store the committed changes from the local repository;

<a name="hosting"/>

### Hosting

- [Heroku](https://www.heroku.com/) - Heroku was used as the hosting platform to deploy my app;

<a name="tech-other"/>

### Other

- [Gifox](https://gifox.io/) - Tool was used to record the gif presented in the demo section of this README files;

- [Multi Devices Mockup Generator](https://techsini.com/multi-mockup/) - Online tool was used to display the project on various devices;

- [MockFlow WireframePro](https://www.mockflow.com/) - Online tool that was used to create wireframes;

- [DBDiagram](https://dbdiagram.io/home) - A relational database diagram design tool used to create database schema;

- [Placeholder](https://placeholder.com/) - Online tool to create custom placeholder images. It was used to create image placeholder in cases when user did not upload his / her profile image;

- [npm](https://getbootstrap.com/docs/4.0/getting-started/webpack/) - Bootstrap and Bootswatch theme installed as a Node.js module using npm to customize SCSS;

- [Popper](https://popper.js.org/) - **jQuery** and **Popper** are Bootstrap's peer dependencies and had to be added to enable me to customize the SCSS;

- [Angrytools gradient maker](https://angrytools.com/gradient/image/) - was used to create a gradient image that was further processed in Dmesh software;

- [Dmesh software](http://dmesh.thedofl.com/) - was used to triangulate the gradient image in order to create backgound images for the app.

<a name="testing"/>

## Testing

<a name="code-validation"/>

### Code Validation

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

Python code was validated using [PEP8 Online](http://pep8online.com). All errors and warnings were fixed to validate the code agains the PEP8 requirements.

The only warning that was not fixed in some cases was the following:
```
blank line contains whitespace
```

This issue apppeared when I added spaces between some blocks of code to make it more readable, which is allowed as per the following PEP8 rule:
**"Extra blank lines may be used (sparingly) to separate groups of related functions."**

<a name="travis"/>

### Travis Continuous Integration

I have also used Travis CI for Continuous Integration to automate testing of my code and resolve any issues as soon as they arose.

<a name="auto-testing"/>

### Automated Testing

Python code was tested using unittest framework and I was able to achieve **overall coverage of 89%**, with the following breakdown for each app:

- **Home** - 100% coverage;

- **Accounts** - 83% coverage;

- **Forum** - 94% coverage;

- **Tickets** - 85% coverage;

- **Search** - 95% coverage;

- **Dashboard** - 100% coverage.

To achieve 100% for all apps below that level I would need a bit more time and knowledge on testing Django apps. However, I believe I managed to achieve a great result given it was my first time testing a Django app.

<a name="functionality-testing"/>

### Functionality Testing

All the features were tested manually throughout the application development process. I documented all tests in an Excel spreadsheet. The file below outlines all features and tests performed on them:

[Testing documentation](https://github.com/JBroks/unicornattractor_issue_tracker/blob/master/testing/testing-documentation.pdf)

<a name="responsiveness-testing"/>

### Responsiveness Testing

This site was tested across multiple browsers (Google Chrome, Safari, Mozilla Firefox, Opera) and on multiple mobile devices (iPad Mini, Nvidia Shield Tablet K1, Huawei P20) to ensure compatibility and responsiveness.

Chrome developer tools were used to additionally inspect responsiveness for the following devices:

- iPad Pro / iPad / iPad Mini (portrait & landscape);

- iPhone 5/SE (portrait & landscape);

- iPhone 6/7/8 (portrait & landscape);

- iPhone 6/7/8 Plus (portrait & landscape);

- iPhone X (portrait & landscape);

- Samsung Galaxy S5 (portrait & landscape);

- MS Surface Duo (portrait & landscape);

- Android (Pixel 2) (portrait & landscape).

Furthermore, [Responsinator](https://www.responsinator.com/) was used to test responsiveness of the final version of the project.

I also used [Mobile-Firendly Test](https://search.google.com/test/mobile-friendly) to check if my website would pass as mobile friendly design. Page was evaluated as easy to use on mobile devices, thus mobile friendly.

The website is fully responsive and working well on mobile devices.

<a name="additional-testing"/>

### Peer-code-review & Additional Testing

Besides testing the app myself I asked my friends and family members to test its functionality for me. Additionally, the project was published on Code Institute Slack code-peer-review channel where other students and mentors are able to review the code and provide their feedback.

<a name="us-testing"/>

### User Stories Testing

**User Story 1:**

- Solution:  Any user can create their own account by using the registration form. User has to provide first and last name, username, email and password in order to register. After successful registration user can login in using the login form. When logged in user can explore all the existing content as well as add their own content.

**User Story 2:**

- Solution:  User can delete their account by going to the profile page and clicking Delete Account button. Confirmation alert will pop up asking for confirmation.

**User Story 3:**

- Solution: Login form enables user to login to their account. Whenever user wants to log out they can click 'Sign out' located in the navbar menu. When user is not authenticated nobody else can access their account unless they know username and password of that user.

**User Story 4:**

- Solution: User can add any type of ticket by clicking 'Add ticket' option in the navbar menu, 'Add ticket' button on jumbotron or static 'Add ticket' button on 'All tickets' page. User is then redirected to the add ticket form where he or she can select a ticket type and fill out other details.

**User Story 5:**

- Solution: User can upvote and donate for any feature of their choice by clicking 'Upvote' button on the view a single ticket page. However, user can only donate once for any given feature.

**User Story 6:**

- Solution: User can upvote any ticket as long as they are authenticated. If user upvoted the ticket they can remove their upvote at any point by clicking the 'Downvote' button. 'Downvote' button replaces 'Upvote' button when a ticket was upvoted by the user.

**User Story 7:**

- Solution: User can comment any ticket in order to share his / her opinion and interact with other users, as long as they are authenticated.

**User Story 8:**

- Solution: User is able to filter out tickets by type and status by using the filter feature implemented on the all tickets page.

**User Story 9:**

- Solution: User is able to search throught the content of my application by using the search bar. Results will include all tickets, comments, threads, and posts that match the keyword typed into the search bar.

**User Story 10:**

- Solution: User can start any new discussion on the forum by adding a new thread. New thread can be added by clicking 'Add Thread' in the navbar or 'Add Thread' static button available on the forum page.

**User Story 11:**

- Solution: User is able to Like / Dislike any thread / post added by them or other users. When e.g. user clicks on the 'Like' button their vote is submitted to the database and color of thumbs up icon changes to green (red when user clicks 'Dislike' button) so the user knows that they already voted for a given thread / post. When user wants to remove their vote they need to click on the same icon again and then the color will go back to grey and the vote will be removed.

**User Story 12:**

- Solution: User is able to review statistics by going to the statistics page. Dashboard contains statistic for top donated features, top upvoted tickets, tickets by type and status, and total number of tickets / bugs / features.

**User Story 13:**

- Solution: Users are able to get an overview on the content they have added by going to their profile page. Profile page shows the content added by a user organised in tabular form and navigated by Bootstrap pills. User can use links to access and review their content, or view / edit / and delete buttons to take an action.

**User Story 14:**

- Solution: User can access the edit profile form by clicking 'Edit Profile' in the navbar or on their profile page.

**User Story 15:**

- Solution: If user forgets their password they can click 'Forgot your password' link available on the sign in page. Process is desing in a way to provide a clear instructions every step of the way.

<a name="resolved-bugs"/>

### Interesting Bugs - Resolved

Throught the process of development of this app I came accross a few interesting bugs. 

- **SQLite issue** - One of the biggest issues I came accross whan using Travis CI was associated with my SQLite database. I switched to Heroku PostgreSQL too fast and while performing some testing I got an issue with missing migrations. I contacted the Code Institiute Tutoring service for advice. In the end I had to reset my SQLite database and rerun migrations to resolve the issue.

- **X-Frame-Options isssue** - when i was triend to test my app using Responsinator and create a demo gif I got the following error:
    ```
    Refused to display '<URL>' in a frame because it set 'X-Frame-Options' to 'sameorigin'.
    ```
    Code Institute Tutor suggested this [solution](https://stackoverflow.com/questions/33267383/how-to-configure-x-frame-options-in-django-to-allow-iframe-embedding-of-one-view/33267908#33267908) and I also these solutions: [solution 1](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options), [solution 2](https://docs.djangoproject.com/en/3.0/ref/clickjacking/).
    
    Ultimately I managed to fix that issue by adding one line in `settings.py` file:
    ```
    X_FRAME_OPTIONS = 'ALLOW-FROM <selected page url>'
    ```
    When I was done testing and I created my gif file I removed that line from my `settings.py`, as it could cause security issues if left there pernamently.

- **Stripe issue** - Initially I had an issue with Stripe, every time I was trying to uvote a feature my first payment was rejected and only the second one was accepted. In the console I was seeing this error:

    ![alt text](https://github.com/JBroks/unicornattractor_issue_tracker/blob/master/design/other-images/stripe-error.png "Stripe error")
    
    I contacted tutor support at Code Institiute and Tim Nelson helped me to resolve it. The problem was that I placed `settings.STRIPE_PUBLISHABLE` in the `upvote` view context and it should have been placed in the `view_ticket` view context.

- **Filtered results pagination** - When testing features I noticed that pagination does not work for the filtered results. I resolved this bug using same process as for the search result pagination i.e. I used the same approach as per [this](http://shopnilsazal.github.io/django-pagination-with-basic-search/) tutorial.

- **Responinator testing issue** - While testing the app on Responsinator I noticed it was showing a gap between the navbar and page content, so I conducted further checks (i.e. on [Mobile-Friendly Test](https://search.google.com/test/mobile-friendly) and [Am I Responsive](http://ami.responsivedesign.is/#). Since it was working well on other online tools and actual devices I came to conclusion that it was an issue with the Responsinator tool rather than my app.

<a name="unresolved-bugs"/>

### Unresolved Bugs

Improved solution for the pills pagination issue has to be implemented. Currently the following javascript solutions was implemented:

```javascript
/**
 * Function that keeps the selected pill active after page is changed
 **/

$(function() {
  $('a[data-toggle="pill"]').on('click', function(e) {
    window.localStorage.setItem('activePill', $(e.target).attr('href'));
  });
  var activePill = window.localStorage.getItem('activePill');
  if (activePill) {
    $('#pills-tab a[href="' + activePill + '"]').tab('show');
  }
});
```

However, this solution causes a minor bug i.e. if user selects page 2 in one pill, it automatically selects the page 2 for all other tabs. I would probably need to inject a tag in the HTML.

I also noticed a bug during responsiveness testing. The issue with a flexbox occurs only for the reset password templates and only while using the Safari browser. Given more time I will investingate and fix this issue.

<a name="deployment-process"/>

## Deployment Process

<a name="S3"/>

### AWS S3 Bucket

#### Setting Up S3 Bucket

In order to set up S3 bucket I went through the following steps:

1. I went to [AWS](https://aws.amazon.com) and created an account and signed into it.

2. I went to the **S3** section of AWS and clicked on the **Create bucket** button.

3. I opened my new bucket and I went to **Properties** tab and selected **Static website hosting**.
 
4. Then I went to **Permissions > CORS Config** and changed the **CORS Configuration** to the following:
    ```
    <?xml version="1.0" encoding="UTF-8"?>
    <CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <CORSRule>
    <AllowedOrigin>*</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <AllowedMethod>HEAD</AllowedMethod>
    <MaxAgeSeconds>3000</MaxAgeSeconds>
    <AllowedHeader>Authorization</AllowedHeader>
    </CORSRule>
    </CORSConfiguration>
    ```

5. Still in the S3 **Permissions** section, I changed the **Bucket Policy** to the following:
    ```
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "PublicReadGetObject",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::<bucket-name>/*"
            }
        ]
    }
    ```
6. In place of the <bucket-name> in the **Resource** line I put my S3 bucket's name.

7. I went to the **IAM  > Groups**, created a **New Group** and attached my S3 bucket details to it.

8. In the **IAM** section I created a **New Policy** and a **New User** and attached these to the newly created group.

#### Adding S3 to Django

1. In my local workspace I installed `django-storages` and `boto3` using the following commands:
    ```
    $ sudo pip3 install django-storages
    $ sudo pip3 install boto3
    ```

2. In `settings.py` file I added `storages` to **INSTALLED_APPS** and updated it with the following S3 bucket details:
    ```python
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000'
    }
    
    # Bucket config
    AWS_STORAGE_BUCKET_NAME = '<bucket-name>'
    AWS_S3_REGION_NAME = '<region-name>'
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_SECRET_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_DEFAULT_ACL = None
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    ```

#### Adding Media to S3

1. I created a `custom_storages.py` file with classes to route to the relevant location settings for static and media files:

    ```
    from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage


    class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION
    
    
    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION
    ```
    
2. Configure media and static files location and storage in the `settings.py` file:
    ```python
    # Static and media files
    STATICFILES_LOCATION = 'static'
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    MEDIAFILES_LOCATION = 'media'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    ```
3. Finally, to push the static files to my S3 bucket I ran the `python3 manage.py collectstatic` command.

<a name="version-control"/>

### Version Control

The site was developed using AWS Cloud 9. To keep records of different versions of all project files git version control system was used. 

To initialize the local repository the command `$ git init` was used. After adding initial files and committing them `$ git remote add origin 'GitHub repo name'` command was used to add new remote repository. Code was then pushed to the master branch of the remote repository using `$ git push -u origin master`.

In order to track the changes in the local repository the following steps were taken:

- command `$ git add 'filename'` - to update what will be committed;

- command `$ git commit -m '<commit-message>'` - to commit the changes.

Using `$ git push` command all changes from the local repository were pushed to the remote one on GitHub.

<a name="run-code-locally"/>

### Running Code Locally

In order to clone my GitHub repository to your local one you should follow these steps:

1. On GitHub navigate to [my repository](https://github.com/JBroks/unicornattractor_issue_tracker).

2. Under the repository name, click **Clone or download**.

3. In the Clone with HTTPs section, copy the clone URL for the repository.

4. Go to IDE that you are using and open terminal.

5. Change the current working directory to the location where you want the cloned directory to be made.

6. Type git clone and then paste the URL you copied in Step 3:

    `$ git clone https://github.com/JBroks/unicornattractor_issue_tracker.git`

7. Lastly press Enter and your local repository will be created.

8. In order to set your own credentials for the enviroment variables follow on of the two steps presented below in your local workspace:

    - Enter and save your own credentials in the `.bashrc` file; or
    
    - Create an `env.py` file with your own credentials and import this into the `settings.py` file.
    
9. Install the requirements.txt file by running the following command in your CLI terminal:

    `sudo pip3 install -r requirements.txt`

10. Run one of the following commands in your terminal to launch the Django project:

    `python3 manage.py runserver`

11. Window showing running the app address will pop up, click the link and the project should load in the new tab. If it doesn't load copy and paste it into a new browser tab instead.

12. In order to create a super user and migrate the changes from models to database run the following commands:

    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py createsuperuser
    ```

<a name="deployment"/>

### Deployment

This project is hosted using Heroku, deployed directly from the `master` branch. 

To deploy my project I followed these steps:

1. Create App:

    - On Heroku [website]() I logged onto my account and created my app by clicking **New > Create new app**;
    
    - In the **Resources** tab on Heroku I searched for **Heroku Postgres** in the **Add-Ons** section and I selected the free **Hobby level**;
    
    - In `settings.py` file I added url of my Heroku app to `ALLOWED_HOSTS`;
    
2. Install the Heroku CLI and required packages: 

    - To install Heroku CLI I typed `$ sudo snap install --classic heroku` command into the terminal; 
     
    - In order to log in to the Heroku account I typed `$ heroku login` command into the terminal;
    
    - I installed guinicorn using the following command: `$ sudo pip3 install guinicorn`;
    
    - I installed psycopg2 library using the following command: `$ sudo pip3 install psycopg2-binary install`;

3. Declare app dependencies:

    - In order to run the app Heroku needs to install the required dependencies so make sure that **requirements.txt** file was created and committed;
    
    - In order to create **requirements.txt** file run `$ sudo pip3 freeze --local > requirements.txt` command in the terminal;
    
    - I run the git `add  requirements.txt`, `git commit -m '<commit-message>'"` and `git push` commands to push all changes to my GitHub repository.

4. First push to Heroku:

    - To make initial push to Heroku I used the following command: `git push heroku master`;
    
    - Since I was using **AWS S3** (see [AWS S3 Bucket](#S3) section) to store staticfiles I set `DISABLE_COLLECTSTATIC=1` by running the following command: `heroku config:set DISABLE_COLLECTSTATIC=1`;
    
5. Procfile:

    - **Procfile** is a Heroku specific type of file that tells Heroku how to run our project;
    
    - For the **Procfile** run `$ echo web: gunicorn issue_tracker.wsgi:application > Procfile` command in the terminal;

6. PostgreSQL Database:

    - In order to connect to the Heroku database I installed `dj_database_url` package using the following command: `$sudo pip3 install dj_database_url`;
    
    - I have updated my **requirements.txt** file and pushed it to my GitHub repository;
    
    - Update the `DATABASE_URL` details in the `env.py` file (stored locally in my workspace);
    
    - I imported `dj_database_url` package into the `settings.py` file and I added my database configuration in setting.py file to connect to the database using the `dj_database_url` package:
    
    ```python
    if "DATABASE_URL" in os.environ:
        DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
    else:
        print("Database URL not found. Using SQLite instead")
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
    }

    ```
    
7. Run migrations and create superuser:

    - In order to migrate all the models into Heroku PostgreSQL I ran the `python3 manage.py makemigrations`, `python3 manage.py migrate`
    
    - To create a new superuser in the new PostgreSQL database I ran `createsuperuser` command;

8. Setting Up App for Hosting on Heroku:

    - In the **Settings** tab on Heroku I clicked on the **Reveal Config Vars** button to add my variables that I stored locally in the `env.py` file;

    - I copied all of the `env.py` variables over to  Heroku's **Config Vars** section;
    
    - Variables in the `env.py` file included the following:

![alt text](https://github.com/JBroks/unicornattractor_issue_tracker/blob/master/design/other-images/settings-heroku.png "App settings")
   
9. Deployment Automation:

    - In the **Deploy** tab on Heroku, I selected GitHub as my deployment method and I connected my app to my GitHub repository;
    
    - I then enabled **Automatic Deploys** to make sure that every push to my GitHub repo will deploy a new version of my app.

<a name="credits"/>

## Credits

<a name="content"/>

### Content

Description in the 'About Unicorn Attractor' section was sourced from [here](https://www.personio.com/product/applicant-sourcing/).

<a name="media"/>

### Media

Favicon and logo used for the project was created and downloaded from [here](https://www.freelogodesign.org/).

The following images were used for the project:

- Forum image was sourced from [here](https://www.csp.org.uk/sites/default/files/styles/full_width/public/media-image/2019-05/forum_discussion.jpg?itok=mv36Pmi9);

- Tickets image was sourced from [here](https://www.wallpaperflare.com/close-up-photography-of-ticket-coupons-admission-admit-buy-wallpaper-wqegy/download/1920x1080);

- Search image was sourced from [here](https://images8.alphacoders.com/438/438354.jpg);

- Statistics image was sourced from [here](https://www.york.ac.uk/study/postgraduate-taught/courses/pgcert-health-research-and-statistics/).

Gradient images were created using [gradient maker](https://angrytools.com/gradient/image/) and [Dmesh software](http://dmesh.thedofl.com/).

Images for the 'About Unicorn Attractor' section were sourced from [here](https://www.personio.com/product/applicant-sourcing/).

Google Play Store and Apple App Store badges were sourced from [here](https://www.stickpng.com/img/download/5a902dbf7f96951c82922875).

<a name="acknowledgements"/>

### Acknowledgements

While working with Django I relied heavily on [Django documentation](https://docs.djangoproject.com/en/3.0/).

Code Institute tutorials were used to create authentication app and Stripe payment processing.

[This](https://stackoverflow.com/questions/25044370/make-clicked-tab-active-in-bootstrap) Stackoverflow discussion was used to make navbar links active.

[This](https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html) tutorial was used when I was working on pagination.

When working on filter feature I reviewed [this](https://www.youtube.com/watch?v=GtwK0Hj6jU8&list=PLLRM7ROnmA9EGO3TOlWLgrc46EhTgj1Ih&index=7) video tutorial.

Filter chaining [solution](https://stackoverflow.com/questions/42105347/django-combine-filter-on-two-fields) was suggested by Haley from Code Institute.

In order to create navbar that disappears on a scroll [this](https://www.solodev.com/blog/web-design/bootstrap/build-a-fixed-top-navigation-that-disappears-as-users-scroll.stml) tutorial was used.

[This](https://stackoverflow.com/questions/6536373/how-can-i-set-the-size-of-rows-columns-in-textfield-in-django-models) Stackoverflow discussion was reviewed to add attributes to textarea.

[History back method](https://www.google.com/search?client=safari&rls=en&q=history.back()&ie=UTF-8&oe=UTF-8) was used for cancel buttons.

[Timesince method](http://www.learningaboutelectronics.com/Articles/How-to-display-how-long-ago-a-post-was-created-in-Django.php) was used in the project.

[This](https://www.youtube.com/watch?v=6Ovw43Dkp44) tutorial was used to learn how to customize bootstrap with Sass.

In order to calculate total comments per post [this](https://stackoverflow.com/questions/46726672/count-total-comments-of-every-author-in-django) Stackoverflow discussion was reviewed.

To keep active tab on refresh [this](https://stackoverflow.com/questions/50423148/keep-active-tab-on-page-refresh-in-bootstrap-4-using-local-storage) Stackoverflow discussion was used.

When creating pagination for search results I reviewed [this](http://shopnilsazal.github.io/django-pagination-with-basic-search/) tutorial.

To create mini charts for total figures cards I reviewed [this](https://css-tricks.com/how-to-make-charts-with-svg/) article.

Many thanks to my mentor **Maranatha Ilesanmi** for support and advice throughout the project.

<a name="disclaimer"/>

### Disclaimer

*This is for educational use.*
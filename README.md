[![Build Status](https://travis-ci.org/JBroks/unicornattractor_issue_tracker.svg?branch=master)](https://travis-ci.org/JBroks/unicornattractor_issue_tracker)

# Unicorn Attracktor Issue Tracker - issue tracker application

## About
Stream Four Project: Full Stack Frameworks with Django - Milestone Project

![alt text](paste gif link "Gif")

This project is part of the 'Full Stack Frameworks with Django' module of the Code Institute Full Stack Software Development course.

## Scope
To complete this module the task was to create an issue tracking application that allows users to submit their tickets. Users are allowed to submit two types of tickets i.e. bugs and features. In order to prioritize their tickets users are able to upvote them. The more upvotes a ticket has the faster it will be look after by a developer.
However, the difference is that bugs can be upvoted for free, while user has to donate minimum €5 to upvote a feature. Users are also able to comment on tickets.
Additional features were developed, these include: data dashboard, forum, like / dislike mechanism for forum, search bar.

## Overview

Project consists of the following sections:

1. Homepage - 

2. Sign in form - Page containing the form that enables user to log into their account to use the app.

3. Sign up form - Page containing the form that enables user to sign up for the Unicorn Attractor Issue Tracking app.
 
4. All tickets page - Page containing paginated tickets and filters that enable user to filter tickets by type and status.

5. Single ticket view page - Page containing a detail information about a given ticket, a comment form and paginated comments.

6. Add / edit ticket page - Page containing add / edit ticket form.

7. Forum page - Page containing paginated forum threads.

8. Thread view page - Page containing a single thread and all associated posts.

9. Add / edit thread page - Page containing add / edit thread form.

10. Data dashboard page - Page containing summary statistics and charts presenting analysis of all tickets submited by app users.

11. Search results page - Page containing any application content that matches the search term.

12. Profile page - Page containing user information, such as username, last seen (date and time), and all content that a given user added, commented, upvoted, liked or disliked.

13. Edit profile page - Page containing edit profile form that enables a user to upload a profile photo and update any personal information.

14. Reset password pages - Pages that display instructions on password reset and password reset form.

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

### Target Audience

### User Stories

The following user stories were used to design this project:

**User Story 1:**

**User Story 2:**

**User Story 3:**

### Mockups & Wireframes

The following [wireframe](paste link) sketches were created to design the project layout options for large, medium and mobile displays.

<a name="database"/>

## Database

### Database Type

### Database Design

Picture below presents the database schema outlining structure of each collection and relationship between each collection.

![alt text](paste link "database-schema")

Relationships between collections are as follows:

- ...

- ...

- ...

<a name="features"/>

## Features

### Existing Features

The project consists of various features presented below.

#### Page loading

- **Spinner** - jQuery method `show()` and `hide()` was used to create spinner showing while page is loading;

- **Overlay** - overlay that fades out the background while page is loading;

#### Buttons

#### Forms

#### Structure

- **Navbar** - the navbar stays collapsed on medium and small devices. To create Bootstrap mobile collapsed button `class="collapse navbar-collapse"` was applied. The navbar contains brand logo and links to associated sections i.e. Home, Explore, Create, Account / Profile;

- **Footer** - contains disclaimer GitHub link and copyrights information;

#### Alerts

- **Toast messages** - **Bootstrap** toasts were used to style flash messages and present them as toast messages to the user;

- **Delete confirmation alerts** - alerts created using **Bootstrap** framework modals that asks user to confirm deletion.

#### Other

- **Pagination** - 

- **Accordion** - Bootstrap accordion feature that stores user personal information, activity, delete profile and update profile buttons on user profile page (mobile displays only);

- **Pills** - 

- **Bootstrap cards** - feature used to present comments / posts added by users and charts & statistics on data dashboard;

- **Search bar** - search bar that enables users to search any ticket, comment, thread, and post.

### Features left to implement

List of features to be implemented in the future:

<a name="technologies-used"/>

## Technologies used

### Programming languages

- **HTML** - the project used HTML to define structure and layout of the web page;

- **CSS** - the project used CSS stylesheets to specify style of the web document elements;

- **JavaScript** - the project used JavaScript to ...........

- **Python** - the project back-end functions are written using Python. Django and Python is used to build views functions;

### Libraries

- [jQuery](https://code.jquery.com/jquery-3.4.1.min.js) - .....;

- [Bootswatch](https://bootswatch.com/) - The project used Bootswatch "LUX" theme for setting styling for all pages;

- [Font Awesome](https://fontawesome.com/v4.7.0/) - Various Font Awesome icons were used for the project;

### Frameworks & Extensions

- [Bootstrap]() - ....;

- [Django]() - ....;

### Other

- [Highcharts](https://www.highcharts.com/) - .....;

- [Gifox](https://gifox.io/) - Tool was used to record the gif presented in the demo section of this README files;

- [Am I Responsive](http://ami.responsivedesign.is/#) - Online tool was used to display the project on various devices;

- [MockFlow WireframePro](https://www.mockflow.com/) - Online tool that was used to create wireframes;

- [DBDiagram](https://dbdiagram.io/home) - A relational database diagram design tool used to create database schema.

- [Placeholder](https://placeholder.com/) - Online tool to create custom placeholder images. It was used to create image placeholder in cases when user did not upload his / her profile image.

<a name="testing"/>

## Testing

### Code validation

#### CSS

....

#### HTML

....

#### JavaScript

......

#### Python

.....

### Features testing

### Responsiveness testing

#### Bugs:

### Peer-code-review

#### Bugs

### User stories testing

**User Story 1:**

- Solution:  .......

**User Story 2:**

- Solution:  .......

<a name="deployment"/>

## Deployment

### GitHub

### Heroku

<a name="credits"/>

## Credits

### Content

### Media

### Acknowledgements

### Disclaimer

*This is for educational use.*
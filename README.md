# BDCrypto Portfolios Website

[Access the BDCrypto Portfolios Website here](https://bdcrypto-portfolio4.herokuapp.com/)(Ctrl + Click to open on a new tab)

## Table of Contents
1. [**UX**](#ux)
    - [**Purpose of the project**](#purpose-of-the-project)
    - [**User stories**](#user-stories)
    - [**Features**](#features)
    - [**Future features**](#future-features)

2. [**Typography and color scheme**](#typography-and-color-scheme)

3. [**Design**](#design)
    - [**Wireframes**](#wireframes)
    - [**ERD Diagrams**](#erd-diagrams)

4. [**Technologies Used**](#technologies-used)
    - [**Code validation**](#code-validation)
    - [**Test cases (user story based with screenshots)**](#test-cases)
    - [**Fixed bugs**](#fixed-bugs)
    - [**Supported screens and browsers**](#supported-screens-and-browsers)

5. [**Deployment**](#deployment)
    - [**Via Gitpod**](#via-gitpod)
    - [**Via Github Pages**](#via-github-pages)
6. [**Credits**](#credits)

---

## UX

## Purpose of the project

Welcome fellow visitor,

This is the BDCrypto portfolios website. It's an application that helps to manage portfolios with crypto assets and track their performance. The website has a simple yet effective interface and provides real use cases to cryptocurrency investors.

This website is made of the following sections:

1. Navigation bar with the title and menu.
2. Presentation with hero and login button.
3. Resgistration and login page.
4. List of portfolios that can be created by the user.
5. List of assets for every portfolio.
6. Possibility to create, edit and delete portfolios.
7. Possibility to add and remove assets to the portfolios.

The business goals for this application is to provide users an application easy to use and to track and manage their cryptocurrency holdings.

The target users are crypto enthusiasts of all ages looking for an application to manage their portfolios and track their performance.

## User stories

### EPIC | Website

- As a **Website User**, I can intuitively navigate around the site so that I can find the content I'm looking for.
- As a **Website User**, I can understand the purpose of the website so that I decide if it meets my needs.

### EPIC | User authentication

- As a **Website User** I can register an account so that I can create a portfolio to add/delete crypto assets.
- As a **Website User** I can Sign in and Sign out to my account so that I keep my account secure.

### EPIC | Portfolio CRUD

- As a **Website User**, I can create a Portfolio of assets so that I can manage and track my crypto holdings.

### EPIC | Assets CRUD

- As a **Website User** I can Add assets to my Portfolio so that I can have it on my holdings.

## Features

## Future features

## Typography and color scheme

## Design

### Wireframes

This user interface for the website was first planned from scratch on Balsamic Wireframes with the license provided by the Code Institute. [Click here](./docs/readme/wireframes.pdf) to see the wireframes of the raw project.

Please note the actual website has changed slightly from these wireframes.

### ERD Diagrams

All the data needed to store on a functioning portfolio tracker was considered in order to create the database. Three relational databases were created: the first one is the default Django User database, which would store the usernames and passwords of all users which would allow them to login to the site, create portfolios and add tokens. The second one is the ´Portfolio´, created with a primary key of PortfolioID and a foreign key relationship to the Users database; it also contains the portfolio's name and creation date, as can be checked [here](https://github.com/Bruno-Diego/bdcrypto-portfolio4/blob/f6a572e44bbc878c21581867d2adbdc7c49130bc/home/models.py#L6). The third and last one is the Asset database, found [here](https://github.com/Bruno-Diego/bdcrypto-portfolio4/blob/f6a572e44bbc878c21581867d2adbdc7c49130bc/home/models.py#L23), which would be responsible for holding the data about a single asset within a single portfolio. The model contains a primary key of AssetID and a foreign key relationship with Portfolio which would allow the individual asset to be connect to a particular portfolio.

The relationship between the Portfolio and the Assets database is a zero-to-many as one portfolio could have zero or many assets within.

[Click here](./docs/readme/erddiagram.png) to see the ERD diagram of the raw project.

## Technologies Used

  - [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
    - Used as the basic building block for the project and to structure the content.
  - [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
    - Used to style all the web content across the project. 
  - [JAVASCRIPT](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
    - Used mostly to add some interactivity to the web elements.
  - [Python](https://www.python.org/)
    - Used when creating the backend functionality in Django.
  - [GitHub](https://github.com/)
    - Used to store code for the project after being pushed.
  - GitHub [Project Boards](https://github.com/users/Bruno-Diego/projects)
    - Used to keep track of all the User Stories and Tasks necessary in order to build
  - [Gitpod](https://www.gitpod.io/)
    - Used as the development environment.
  - [Git](https://git-scm.com/)
    - Used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
  - [Materialize](https://materializecss.com/)
    - Used to as the front-end framework.
  - [Favicon.io](https://favicon.io/)
    - Used to create favicon for my website.
  - [Grammarly](https://www.grammarly.com/)
    - Used to fix the grammar errors across the project.
  - [Django](https://www.djangoproject.com/)
    - Used as Python-based free and open-source web framework that follows the model–template–views architectural pattern to develop the basic back-end of the project.
  - [Grammarly](https://www.grammarly.com/)
    - Used to fix the grammar errors across the project.
  - [Grammarly](https://www.grammarly.com/)
    - Used to fix the grammar errors across the project.



 
## Code validation

## Test cases

## Fixed bugs

## Supported screens and browsers

## Deployment

## Via Gitpod

## Via Heroku

## Credits
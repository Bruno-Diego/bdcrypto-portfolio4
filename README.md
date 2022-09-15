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

## User stories

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

## Technologies Used

## Code validation

## Test cases

## Fixed bugs

## Supported screens and browsers

## Deployment

## Via Gitpod

## Via Heroku

## Credits
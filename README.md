# Team Member Management Application

This repository contains a simple team-member management application built using Django. The application allows users to
view, edit, add, and delete team members. It consists of three main pages: List page, Add page, and Edit page.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)

## Features

### List Page

- Displays a list of all team members.
- Subtitle reflects the number of team members.
- Indicates if a team member is an admin.
- Clicking a team member navigates to the Edit page.
- Clicking the "+" at the top navigates to the Add page.

### Add Page

- Allows users to add a new team member.
- Input fields for first & last name, phone number, email, and role.
- Role defaults to regular.
- Clicking save adds the team member to the list and navigates to the List page.

### Edit Page

- Allows users to edit the details of a team member.
- Form includes fields for first & last name, phone number, email, and role.
- Clicking save updates the team member information and navigates to the List page.
- Clicking delete by admin only removes the team member and navigates to the List page.

## Getting Started

### Prerequisites

- Python 3.x
- Django (install via `pip install Django`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/team-member-management.git
   cd team-member-management

## Install dependencies:

- pip install -r requirements.txt
- install project dependencies

## Apply database migrations:

- python manage.py migrate
- run database migrations for the project

## Run the development server:

- python manage.py runserver
- run the server for the app in development

## Time Spent
-I spent approximately 15 hours working on this project.

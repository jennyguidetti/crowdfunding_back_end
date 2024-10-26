# Crowdfunding Back End
Jenny Guidetti

## Planning:
### Concept/Name
#### ParamediXPlus

A crowdfunding website where paramedics and ambulance services can organise work placement opportunities for clinical and skill development. 

### Intended Audience
- Qualified paramedics
- Ambulance Organisations

### User Stories
- As a qualified paramedic working for the local ambulance service, I would like to see how interstate ambulance services operate differently in regards to clinical, operational and day to day protocols
- As a well established ambulance organisation, we would like to collaborate with other ambulance services in order to improve patient outcomes and foster strong relationships

### Front End Pages/Functionality
- Homepage
    - Top 8 list of available opportunities in ambulance services
    - Ability to register for user account
    - Ability to login to user account
- Project page
    - Page of available ambulance service placements
    - Description of each individual service (name, goal, current pledges)
    - Button to pledge to each service
- User page
    - Option to update user details
    - Displays all ambulance services that have been pledged to
    - Option to update pledges
- Pledge detail page
    - Ability to pledge amount of hours to organisations

### API Spec

| HTTP Method | URL | Purpose | Request Body | Success Response Code | Authentication/Authorisation |
| ----------- | --- | ------- | ------------ | --------------------- | ---------------------------- |
| GET | /users/ | Returns all users | N/A | 200 | N/A |
| POST | /users/ | Create a new user | User object | 201 | N/A |
| GET | /users/:id/ | Return a user by ID | N/A | 200 | Must be logged in. Must be same user. |
| PUT | /users/:id/ | Update a user by ID | User object | 200 | Must be logged in. Must be same user. |
| DELETE | /users/:id/ | Delete a user by ID | N/A | 200 | Must be logged in. Must be same user. |
| GET | /projects/ | Return all projects | N/A | 200 | N/A |                              |
| POST | /projects/ | Create a new project | Project object | 201 | Must be logged in. |
| GET | /projects/:id/ | Return a project by ID | N/A | 200 | N/A |
| PUT | /projects/:id/ | Update a project by ID | Project object | 200 | Must be logged in. Must be owner of project. |
| DELETE | /projects/:id/ | Delete a project by ID | N/A | 200 | Must be logged in. Must be owner of project |
| GET | /pledges/ | Return all pledges | N/A | 200 | N/A |
| POST | /pledges/ | Create a new pledge | Pledge object | 201 | Must be logged in. |
| GET | /pledges/:id/ | Return a pledge by ID | N/A | 200 | Must be logged in. Must be owner of pledge |
| PUT | /pledges/:id/ | Update a pledge by ID | Pledge object | 200 | Must be logged in. Must be owner of pledge |
| DELETE | /pledges/:id/ | Delete a pledge by ID | N/A | 200 | Must be logged in. Must be owner of pledge. |
| POST | /api_auth_token/ | Create auth token for user | User object | 200 | N/A

### DB Schema
![DB Schema](../crowdfunding_back_end/img/db_schema.png)

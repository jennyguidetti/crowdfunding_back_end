# Crowdfunding Back End
Jenny Guidetti

## Planning:
### Concept/Name
#### ParamediXPlus
Link to the deployed project https://paramedixplus-d64ffb40bbf8.herokuapp.com/projects/

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
![DB Schema screenshot](../crowdfunding_back_end/img/db_schema.png)

### How to register a new user
1. Make POST request at /users/ endpoint
2. Ensure 'Body' contains mandatory fields provided in JSON format: username, password, email, employer, clinical level (optional: first name, last name)
3. Send request to receive 201 response and user details

![register new user insomnia screenshot](../crowdfunding_back_end/img/register_user.png)

### How to create a new project
1. Make POST request at /api-token-auth/ endpoint
2. Ensure 'Body' contains mandatory fields provided in JSON format: username, password
3. Send request to receive 200 response and authorisation token

![get authentication token insomnia screenshot](../crowdfunding_back_end/img/how_to_auth.png)

4. Make POST request at /projects/ endpoint
5. Select 'Auth' and then 'Bearer Token'
6. Ensure it is enabled, then use authentication token received from step 3 as 'Token' and add prefix 'Token' (If left blank or incorrectly entered then 401 error will occur)

![auth details for POST projects insomnia screenshot](../crowdfunding_back_end/img/how_to_add_project_auth.png)

7. Ensure 'Body" contains mandatory fields in JSON format: organisation name, organisation description, goal, image, is open, date created
8. Send request to receive 201 response and project details

![POST projects body insomnia screenshot](../crowdfunding_back_end/img/how_to_add_project_details.png)

### Screenshots
1. Get users
![GET users insomnia screenshot](../crowdfunding_back_end/img/get_users.png)

2. Create new user
![POST users insomnia screenshot](../crowdfunding_back_end/img/post_users.png)

3. Get user by ID
![GET users/id insomnia screenshot](../crowdfunding_back_end/img/get_users1.png)

4. Update user by ID
![PUT users/id insomnia screenshot](../crowdfunding_back_end/img/put_users1.png)

5. Delete user by ID
![DELETE users/id insomnia screenshot](../crowdfunding_back_end/img/delete_users1.png)

6. Get projects
![GET projects insomnia screenshot](../crowdfunding_back_end/img/get_projects.png)

7. Create new project
![POST projects insomnia screenshot](../crowdfunding_back_end/img/post_projects.png)

8. Get project by ID
![GET projects/id insomnia screenshot](../crowdfunding_back_end/img/get_projects1.png)

9. Update project by ID
![PUT projects/id insomnia screenshot](../crowdfunding_back_end/img/put_projects1.png)

10. Delete project by ID
![DELETE projects/id insomnia screenshot](../crowdfunding_back_end/img/delete_projects1.png)

11. Get pledges
![GET pledges insomnia screenshot](../crowdfunding_back_end/img/get_pledges.png)

12. Create new pledge
![POST pledges insomnia screenshot](../crowdfunding_back_end/img/post_pledges.png)

13. Get pledge by ID
![GET pledges/id insomnia screenshot](../crowdfunding_back_end/img/get_pledges1.png)

14. Update pledge by ID
![PUT pledges/id insomnia screenshot](../crowdfunding_back_end/img/put_pledges1.png)

15. Delete pledge by ID
![DELETE pledges/id insomnia screenshot](../crowdfunding_back_end/img/delete_pledges1.png)

16. Get authentication token for user
![POST authentication insomnia screenshot](../crowdfunding_back_end/img/auth-token.png)


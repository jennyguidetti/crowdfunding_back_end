# Crowdfunding Back End
Jenny Guidetti

## Planning:
### Concept/Name
A crowdfunding website where paramedics and ambulance services can organise work placement opportunities for clinical and skill development. 

### Intended Audience
The intended audience includes paramedics looking to gain experience working in other ambulance services. It also includes ambulance services willing to offer placements in exchange for insight into other services and foster strong relationships. 
* Qualified Paramedics
* Ambulance Organisations

### User Stories
* As a qualified paramedic working for x ambulance service, I would like to see how y ambulance service operates differently in regards to clinical, operational and day to day protocols
* As a well established Ambulance Organisation, we would like to collaborate with other ambulance services in order to improve patient outcomes and foster strong relationships

### Front End Pages/Functionality
- Homepage
    - Top 8 list of available opportunities in ambulance services
    - Ability to register for user account
    - Login 
- Project page
    - Pages of available projects
    - Option to pledge to projects
- User page
    - Displays all projects that have been pledged to
- Project detail page
- Project all page
- Pledge detail page
- Pledge all page?
- {{ A second page available on the front end }}
    - {{ A list of dot-points showing functionality is available on this page }}
    - {{ Another list of dot-points showing functionality }}
    - {{ etc }}

### API Spec
Define your endpoints:

| HTTP Method | URL | Purpose | Request Body | Success Response Code | Authentication/Authorisation |
| ----------- | --- | ------- | ------------ | --------------------- | ---------------------------- |
| GET | /users/ | Get all users | N/A | 200 | N/A |
| POST | /users/ | Create a new user | User object | 201 | ? |
| GET | /users/1/ | Show user with ID of "1" | N/A | 200 | Must be logged in. Must be same user. |
| PUT | /users/1/ | Update user with ID of "1" | User object | 200 | Must be logged in. Must be same user. |
| DELETE | /users/1/ | Delete user with ID of "1" | N/A | 200 | Must be logged in. Must be same user. |
| GET | /projects/ | Return all projects | N/A | 200 | N/A |                              |
| POST | /projects/ | Create a new project | Project object | 201 | Must be logged in |
| GET | /projects/1/ | Return the project with ID of "1" | N/A | 200 | N/A |
| PUT | /projects/1/ | Update the project with ID of "1" | Project object | 200 | Must be logged in. Must be project owner. |
| DELETE | /projects/1/ | Delete the project with ID of "1" | N/A | 200 | Must be logged in. Must be owner of project |
| GET | /pledges/ | Get all pledges | N/A | 200 | Must be logged in. Must be owner of pledges |
| POST | /pledges/ | Create a new pledge | Pledge object | 201 | Must be logged in. Must not be owner of the project. |
| GET | /pledges/1/ | Get the pledge with ID of "1" | N/A | 200 | N/A |
| PUT | /pledges/1/ | Update pledge with ID of "1" | Pledge object | 200 | Must be logged in. Must not be owner of the project |
| DELETE | /pledges/1/ | Delete the pledge with ID of "1" | N/A | 200 | Must be logged in. Must be owner of pledge. |
| POST | /api_auth_token/ |
| POST | /users/login/ |

### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )
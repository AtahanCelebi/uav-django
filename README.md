# Uav-Django Project - UAV API Documentation
## User Registration, Login, and Logout API
This is a set of APIs for user registration, login, and logout functionality. It's built using the Django Rest Framework and allows users to create an account, log in, and log out.

### Endpoints
#### User Registration
```
URL: /api/user/register/
```
Method: POST

Permissions: AllowAny

Request Body:

```json
{
    "email": "user@example.com",
    "password": "password123",
    "first_name": "John",
    "last_name": "Doe"
}
```
Response Body:

```json
Copy code
{
    "id": 1,
    "email": "user@example.com",
    "first_name": "John",
    "last_name": "Doe"
}
```
#### User Login
```
URL: /api/user/login/
```
Method: POST

Permissions: AllowAny

Request Body:

```json
Copy code
{
    "email": "user@example.com",
    "password": "password123"
}
```
Response Body:

```json
Copy code
{
    "message": "Login successful."
}
```
#### User Logout
```
URL: /api/user/logout/
```

Method: POST

Permissions: IsAuthenticated

Response Body:

```json
Copy code
{
    "message": "Logout successful."
}
```
## Authentication
The user login and logout endpoints require authentication. To authenticate a user, send an email and password in the request body to the login endpoint. If the credentials are correct, a token will be returned. Send this token in the Authorization header of subsequent requests to the logout endpoint to log out the user.

## Serializers
The following serializers are used in the endpoints:

## UserRegistrationSerializer
Serializes and deserializes User objects.

## Fields:

email: EmailField
password: CharField
first_name: CharField
last_name: CharField
LoginSerializer
Serializes and deserializes email and password fields.

Fields:
| email:   |  EmailField |
| ------------- | ------------- |
| password  | CharField  |

## IHA KAYIT APP

This API allows you to create, retrieve, update, and delete IHA (UAV) objects.

### Endpoints
##### Registration
The IHARegistrationView endpoint allows you to register a new IHA object.
```
POST /ihas/register/
```
##### Request
The request body should contain the following fields:

|Field  | 	Type  | 	Required  | 	Description | 
| ------------- | -------------  | ------------- | ------------- |
| brand  | 	string  | Yes  | 	The brand of the IHA  |
| model  | string  | Yes  | 	The model of the IHA  |
| weight  | number  | Yes  | The weight of the IHA  |
| category  | string  | Yes  | 	The category of the IHA  |

#### Response
On success, the response body will contain the registered IHA object in JSON format.

#### Retrieve
The IHAListView endpoint allows you to retrieve a list of all IHA objects.
```
GET /ihas/list/
```
#### Response
On success, the response body will contain a list of all registered IHA objects in JSON format.

#### Update
The IHAUpdateView endpoint allows you to update an existing IHA object.
```
PUT /ihas/<id>/update/
```
#### Request
The request body should contain the same fields as the registration endpoint.

#### Response
On success, the response body will contain the updated IHA object in JSON format.

#### Delete
The IHADeleteView endpoint allows you to delete an existing IHA object.
```
DELETE /ihas/<id>/delete/
```
#### Response
On success, the response body will contain a message indicating that the IHA object has been deleted.

### Filtering
The IHAFilterView endpoint allows you to filter the list of IHA objects based on the brand, model, weight, category, and/or search terms.
```
GET /ihas/filter/
```
#### Request
The request can include query parameters for the filter fields and search terms:

|Field  | 	Type  | 	Description  | 
| ------------- | -------------  | ------------- | 
| brand  | 	string  | Filters by brand  | 	
| model  | string  | 	Filters by model  | 
| weight  | number  | Filters by weight  |
| category  | string  | Filters by category  | 	
| search_fields  | string  | Searches across brand, model, and category fields | 	

#### Response
On success, the response body will contain a list of filtered IHA objects in JSON format.

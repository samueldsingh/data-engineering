
## 1. What is webservices?

- Web Service uses a collection of open-source protocols to exchange data between applications whereas API acts as an interface between two 
applications to facilitate interaction with each other.
- The key difference is web service supports only HTTP while API supports HTTP/HTTPS protocol.
- A web application is a network-based resource responsible for completing a single task.
- All Web services are APIs but all APIs are not web services.

## 2. What is an API?
- An Application Programming Interface is a collection of communication protocols and subroutines used by various programs to communicate between them. 
- the API is responsible here to send your request to the database and responds with the output
- API works as:
  - The client initiates the requests via the APIs URI (Uniform Resource Identifier)
  - The API makes a call to the server after receiving the request
  - Then the server sends the response back to the API with the information
  - Finally, the API transfers the data to the client
- Example: Zomato uses Google Maps API to track delivery boy location.
- APIs are considered safe in terms of attacks as it includes authorization credentials and an API gateway to limit access so as to minimize security threats.

- [API - Geeks For Geeks](https://www.geeksforgeeks.org/what-is-an-api/)

## 3. What are REST APIs?

REST stands for Representational State Transfer, and follows the constraints of REST architecture allowing interaction with RESTful web 
services. It defines a set of functions (GET, PUT, POST, DELETE) that clients use to access server data. The functions used are:

- GET (retrieve a record)
- PUT (update a record)
- POST (create a record)
- DELETE (delete the record)

Its main feature is that REST API is statelessness, i.e., the servers do not save clients’ data between requests. 

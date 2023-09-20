
## 1. What is webservices?

- A web service is offered by an electronic device to another electronic device, as they communicate with each other via the Internet, without any platform dependency issues.
- It is a standardized method for propagating messages between client and server applications.
- Any software, application, or cloud technology that uses standardized web protocols (HTTP or HTTPS) to connect, interoperate, and exchange data messages – commonly XML (Extensible Markup Language) – across the internet is considered a web service.
- All Web services are APIs but all APIs are not web services.


## 2. What is an API?
- An API, or Application Programming Interface, is a set of rules that define how applications can communicate with each other.
- An API is a set of definitions and protocols for building and integrating application software. It’s sometimes referred to as a contract between an information provider and an information user—establishing the content required from the consumer (the call) and the content required by the producer (the response).
- API works as:
  - The client initiates the requests via the APIs URI (Uniform Resource Identifier). A request URL consists of an HTTP method, a base URL, and a resource URI. 
  - The API makes a call to the server after receiving the request
  - Then the server sends the response back to the API with the information
  - Finally, the API transfers the data to the client
- Example: Zomato uses Google Maps API to track delivery boy location.
- Example: The API design for a weather service could specify that the user supply a zip code and that the producer reply with a 2-part answer, the first being the high temperature, and the second being the low.  
- APIs are considered safe in terms of attacks as it includes authorization credentials and an API gateway to limit access so as to minimize security threats.
- After a client issues a **request url**, HTTP defines a set of request methods to indicate the desired action to be performed for a given resource:
  - `GET` - This request reads information from a record in the database.
  - `PUT` - This request changes a record's information in the database.
  - `POST` - This request creates a new record in the database
  - `DELETE` - This request removes a record from the database.
  - `PATCH` - To modify a part of a resource. You only need to pass in the data that you want to update.
  - `HEAD` - The HEAD method asks for a response identical to a GET request, but without the response body.
  - `CONNECT` - The CONNECT method establishes a tunnel to the server identified by the target resource.
  - `OPTIONS` - The OPTIONS method describes the communication options for the target resource.
  - `TRACE` - The TRACE method performs a message loop-back test along the path to the target resource.
- The payload is an essential part of a REST API as it contains the actual data being transferred between the client and the server. It is important to ensure that the payload is properly formatted and structured according to the API's specifications to ensure proper communication and handling of data.
- An advantage of an API is that you don’t have to know the specifics of caching—how your resource is retrieved or where it comes from.

- JSON payload format example:
```
{
    "cid": 1,
    "cname": "Ramesh",
    "email": "ramesh@gmail.com"
}
```

- [API - Geeks For Geeks](https://www.geeksforgeeks.org/what-is-an-api/)

## 4. Difference between web services and API?

- Every web service is an API "since it exposes an application's data and/or functionality” but not every API is a web service.
- APIs are just the terminals that enable client-server relationships, while web services are an architectural style for integrating Web-based applications using the XML, SOAP, and WSDL open standards over an Internet Protocol backbone.
- Web services require SOAP and XML to transfer data over a network, while APIs can use any protocols or design patterns.
- APIs allow applications to communicate, while web services allow machines to communicate.
- Web Services requires a network connection while APIs may or may not require a network for their operability.
- Web services require SOAP and XML, which are no longer the most popular standard.
- APIs are more efficient, with RESTful web services offering a more light-weight architecture web services are heavy.
- Web services only support HTTP as a backbone, while APIs are more flexible.
- [API vs Web Services](https://www.abstractapi.com/guides/api-vs-web-services#:~:text=or%20design%20patterns.-,APIs%20allow%20applications%20to%20communicate%2C%20while%20web%20services%20allow%20machines,longer%20the%20most%20popular%20standard.)

## 3. What are REST APIs?

A REST API (also known as RESTful API) is an application programming interface (API or web API) that conforms to the constraints of REST architectural style and allows for interaction with RESTful web services. REST stands for representational state transfer.

- REST is a set of architectural constraints, not a protocol or a standard. API developers can implement REST in a variety of ways.
- When a client request is made via a RESTful API, it transfers a representation of the state of the resource to the requester or endpoint.
- This information, or representation, is delivered in either JSON (Javascript Object Notation), HTML, XLT, Python, PHP, or plain text format via HTTP.

In order for an API to be considered RESTful, it has to conform to these criteria:
- A client-server architecture made up of clients, servers, and resources, with requests managed through HTTP.
- Stateless client-server communication, meaning no client information is stored between get requests and each request is separate and unconnected.
- Cacheable data that streamlines client-server interactions.
- A uniform interface between components so that information is transferred in a standard form. This requires that:
  - resources requested are identifiable and separate from the representations sent to the client.
  - resources can be manipulated by the client via the representation they receive because the representation contains enough information to do so.
  - self-descriptive messages returned to the client have enough information to describe how the client should process it.
  - hypertext/hypermedia is available, meaning that after accessing a resource the client should be able to use hyperlinks to find all other currently available actions they can take.
- A layered system that organizes each type of server (those responsible for security, load-balancing, etc.) involved the retrieval of requested information into hierarchies, invisible to the client.
- Code-on-demand (optional): the ability to send executable code from the server to the client when requested, extending client functionality. 

[REST API](https://www.redhat.com/en/topics/api/what-is-a-rest-api)

## 4. What is an API call. Explain in detail?

An API call, or Application Programming Interface call, is a fundamental concept in software development that allows different software applications or components to communicate and interact with each other. Let's dive into a detailed explanation of API calls:

1. **Application Programming Interface (API):** An API is like a bridge or contract that defines how one software component or system can interact with another. It specifies a set of rules, protocols, and functions that developers can use to request specific actions or access data from another application, service, or system.

2. **Client and Server:** In the context of API calls, there are typically two roles:
   - **Client:** The client is the software application or component that initiates the API call. It needs some service, data, or functionality provided by the server.
   - **Server:** The server is the software application or component that receives and processes the API request from the client. It performs the requested action or retrieves the requested data and sends a response back to the client.

3. **HTTP/HTTPS:** Many API calls are made over the HTTP (Hypertext Transfer Protocol) or its secure counterpart, HTTPS. These protocols define how data is transmitted over the internet. When you make an API call using HTTP/HTTPS, you send an HTTP request from the client to the server, and the server responds with an HTTP response.

4. **HTTP Request Methods:** HTTP requests typically use different HTTP methods to specify the type of action to be performed. The most common HTTP methods used in API calls are:
   - **GET:** Used to retrieve data from the server.
   - **POST:** Used to send data to the server to create a new resource or perform an action.
   - **PUT:** Used to update an existing resource on the server.
   - **DELETE:** Used to request the removal of a resource on the server.

5. **Request Headers:** API calls often include headers in the HTTP request to provide additional information or metadata about the request. Headers can contain things like authentication tokens, content types, and other relevant information.

6. **Request Body:** In some API calls, particularly those using the POST and PUT methods, data is sent in the request body. This data can be in various formats, such as JSON, XML, or form data, depending on the API's specifications.

7. **Endpoint:** An API call typically includes an endpoint, which is a specific URL or URI (Uniform Resource Identifier) that identifies the resource or action the client wants to access on the server. The endpoint, combined with the HTTP method, defines the nature of the API call.

8. **Response:** After processing the API request, the server sends back an HTTP response to the client. This response includes:
   - **Status Code:** A three-digit numerical code that indicates the outcome of the request (e.g., 200 for success, 404 for not found, 500 for server error).
   - **Response Body:** Data returned by the server, which can be in various formats like JSON, XML, HTML, or plain text. This is often the actual data or the result of the requested action.

9. **Error Handling:** API calls can result in errors, such as authentication failures, invalid requests, or server issues. Proper error handling is crucial to ensure that the client can react appropriately when things go wrong.

10. **Authentication and Security:** To protect sensitive data and resources, APIs often require authentication, where the client provides credentials (e.g., API keys, tokens) to prove its identity. Additionally, APIs may use encryption (HTTPS) to secure data transmission.

11. **Rate Limiting:** Some APIs impose rate limits on the number of API calls a client can make within a specified time period to prevent abuse and ensure fair usage.

In summary, an API call is a communication process between a client and a server that follows a predefined set of rules and protocols. It involves sending an HTTP request from the client to the server, specifying the desired action or data retrieval, and receiving an HTTP response containing the result. APIs are a critical component of modern software development, enabling the integration of diverse services and systems to create complex and powerful applications.

## 5. Explain GET vs POST request

HTTP (Hypertext Transfer Protocol) defines several request methods that clients (such as web browsers) can use to communicate with web servers. Two of the most commonly used methods are GET and POST. These methods serve different purposes and have distinct characteristics:


1. **Purpose:** 

  - `GET` Request: The GET request method is primarily used to request data from a web server. It is used when the client wants to retrieve information from the server without sending any data in the request body.

  - `POST` Request: The POST request method is used when the client wants to submit data to the server. It is often used for actions that modify server-side data, create new resources, or submit forms containing sensitive information.

2. **Data in URL:**

  - `GET` Request: In a GET request, the data is typically included in the URL as query parameters. This means that the data is visible in the URL, making it suitable for simple queries or when you want to share a link that contains specific parameters.

  - `POST` Request: In a POST request, the data is included in the request body, not in the URL. This means that the data is not visible in the URL, making it suitable for sending larger amounts of data or sensitive information.

3. **Caching:** 

  - `GET`: GET requests are generally cacheable, which means that the response can be stored by the browser or intermediate proxy servers for future use. This can help reduce server load and improve performance for frequently accessed resources.

  - `POST`: POST requests are typically not cacheable, meaning that the response should not be stored for future use by the client or intermediate proxies.

4. **Idempotent:** 

  - `GET`: GET requests are considered idempotent, meaning that making the same GET request multiple times should have the same result each time, and it should not change the server's state. This property makes GET requests safe for scenarios where repetition is acceptable.

  - `POST`: POST requests are not idempotent, which means that making the same POST request multiple times may result in different outcomes, and it can change the server's state. Therefore, they should be used with caution when repeating the same request could have unintended consequences.

5. **Examples:** 

  - `GET`: Browsing a web page, requesting search results, or viewing an image are common use cases for GET requests.
  - `POST`: Submitting a contact form, uploading a file, making a purchase, or submitting login credentials are common use cases for POST requests.

In summary, the choice between GET and POST request methods depends on the intended use and the nature of the data being transferred:

- Use GET for retrieving data from the server, especially when the request is idempotent and the data can be included in the URL.

- Use POST for submitting data to the server, especially when the request modifies server-side data, involves sensitive information, or requires a larger data payload in the request body.

## 6. Explain POST vs PUT

HTTP (Hypertext Transfer Protocol) defines several request methods that clients (such as web browsers) can use to communicate with web servers. Two of these methods, POST and PUT, are often used to send data to the server, but they have distinct purposes and behaviors:

1. **Purpose:** 

  - POST: The POST request method is primarily used to submit data to the server for processing. It is commonly used when creating a new resource on the server or when sending data that will be processed and stored on the server.

  - PUT: The PUT request method is used to update or replace an existing resource on the server. It is commonly used when the client wants to send data to the server to replace the current state of a resource entirely.


2. **Data in Request Body:** 

  - POST: In a POST request, the data is included in the request body, not in the URL. This allows for sending larger amounts of data and more complex data structures compared to GET requests.

  - PUT: Similar to POST, the data in a PUT request is included in the request body. This data should represent the updated state of the resource.

3. **Idempotence:** 

  - POST: POST requests are not idempotent, meaning that making the same POST request multiple times can result in different outcomes. For example, submitting a POST request to create a new resource multiple times will create multiple resources on the server.

  - PUT: PUT requests are idempotent, meaning that making the same PUT request multiple times should have the same result as making it once. Repeatedly sending the same data using PUT should not create multiple copies of the resource.

4. **Resource Creation:** 

  - POST: 
  - PUT (Resource Update): PUT requests are typically used to update an existing resource. If the resource does not exist at the specified URL, some server implementations may create a new resource, but this behavior is not strictly defined by the HTTP specification.


5. **Examples:** Submitting a form on a website, creating a new user account, posting a comment, or uploading a file are common use cases for POST requests.

  - POST: POST requests are often used to create new resources on the server. The server typically generates a unique identifier for the newly created resource and includes it in the response.

  - PUT: Updating a user's profile information, replacing a file on a server with an updated version, or editing an existing document are common use cases for PUT requests.

In summary, the main difference between POST and PUT requests lies in their intended use:

- Use POST when you want to submit data to the server for processing, especially when creating new resources or performing actions that are not idempotent.

- Use PUT when you want to update or replace an existing resource on the server, and you want the request to be idempotent, meaning it can be safely repeated without unintended consequences.

## 7. Explain PUT vs PATCH

HTTP (Hypertext Transfer Protocol) defines several request methods that clients (such as web browsers) can use to communicate with web servers. Two of these methods, PUT and PATCH, are used for updating resources on the server, but they have different purposes and behaviors:

**PUT Request:**

1. **Purpose:** 

  - PUT: The PUT request method is used to update or replace an existing resource on the server with a complete new representation of that resource. It is typically used when the client wants to provide a full, updated version of the resource, which will replace the existing resource entirely.

  - PATCH: The PATCH request method is used to partially update an existing resource on the server. It is designed for making partial modifications to a resource, rather than replacing it entirely.

2. **Data in Request Body:** 

  - PUT: In a PUT request, the data representing the updated resource is included in the request body. This data should represent the complete state of the resource, including any properties that were not modified.

  - PATCH: In a PATCH request, the data representing the changes or modifications to the resource is included in the request body. The data should only include the specific fields or properties that need to be updated.

3. **Idempotence:** 

  - PUT: PUT requests are idempotent, meaning that making the same PUT request multiple times should have the same result as making it once. Repeatedly sending the same data using PUT should not create multiple copies of the resource.

  - PATCH: PATCH requests can be idempotent or non-idempotent, depending on how they are implemented. It is up to the server and the specific PATCH request to determine whether repeating the same request will have the same effect each time.

4. **Resource Replacement:** 

  - PUT: PUT requests are typically used for resource replacement. The server replaces the existing resource at the specified URL with the new representation provided in the request.

  - PATCH (Partial Update): PATCH requests are used when you want to make partial updates to a resource. The server applies the changes provided in the request to the existing resource, without requiring the client to send the complete representation of the resource.

5. **Examples:** 

  - PUT: Using PUT to update a user's profile information with a complete new set of data, replacing an entire document on a server with an updated version, or updating a product's details with all new information are common use cases for PUT requests.

  - PATCH: Using PATCH to update a user's profile with changes to specific fields (e.g., updating the user's email address or phone number), modifying a document by adding or changing specific sections, or updating specific attributes of a product are common use cases for PATCH requests.

In summary, the key difference between PUT and PATCH requests lies in their intended use and the scope of updates:

- Use PUT when you want to replace an entire resource on the server with a complete new representation of that resource.

- Use PATCH when you want to make partial modifications or updates to an existing resource, sending only the changes needed, rather than replacing the entire resource.

## 8. Explain POST vs PATCH

POST and PATCH are both HTTP methods used for different purposes in web applications, particularly when dealing with resources and data manipulation. Here's an explanation of the differences between POST and PATCH:

**POST Request:**

1. **Purpose:** 

  - POST: POST is primarily used to submit data to the server to create a new resource or perform a non-idempotent action. It is often used for creating new records or resources on the server.

  - PATCH: PATCH is used to make partial updates to an existing resource on the server. It is designed for modifying specific attributes or properties of a resource without replacing the entire resource.

2. **Data in Request Body:** 

  - POST: In a POST request, the data to be processed or saved is included in the request body. This data typically represents the entire resource being created.

  - PATCH: In a PATCH request, the data in the request body represents the changes or updates to be applied to the resource. It typically includes only the fields or properties that need to be updated.

3. **Idempotence:** 

  - POST: POST requests are not idempotent, meaning that making the same POST request multiple times can result in different outcomes. Each request typically creates a new resource or performs a non-idempotent action.

  - PATCH: PATCH requests can be either idempotent or non-idempotent, depending on how they are implemented. It is possible to design PATCH requests in an idempotent way, where repeating the same request will have the same effect each time, but this is not guaranteed.

4. **Resource Creation:** 

  - POST: POST is commonly used for creating new resources on the server. The server typically generates a unique identifier for the newly created resource, and this identifier is often included in the response.

  - PATCH (Partial Update): PATCH is used when you want to apply partial modifications to an existing resource. It allows you to send only the changes needed, without requiring the client to send the complete representation of the resource. 

5. **Examples:** 

  - POST: Submitting a form to create a new user account, adding a new item to a shopping cart, or posting a comment on a blog are common use cases for POST requests.

  - PATCH: Using PATCH to update specific attributes of a user profile (e.g., changing the email address or phone number), modifying a document by adding or changing specific sections, or updating certain attributes of a product are common use cases for PATCH requests.


In summary:

- Use POST when you want to create a new resource or perform a non-idempotent action on the server. POST typically involves sending the complete data for the new resource.

- Use PATCH when you want to make partial modifications to an existing resource on the server, sending only the changes needed to update specific attributes or properties of the resource.


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

Backend

Backend development refers to server-side development that powers digital applications and interfaces. Backend developers focus on building server infrastructure, developing APIs, optimizing databases, and ensuring smooth data flow between frontend interfaces and backend servers.

While frontend development focuses on the visual user and the interface of an application, backend development focuses on the logical components, which are as follows:

    Databases: Backend developers design, build, and optimize databases to store application data. Popular database development options include SQL, NoSQL, and object-oriented databases.
    Servers: Backend developers configure servers and server environments to deploy applications and handle requests. Common server environments include Apache Spark, Nginx, and Microsoft IIS.
    APIs: Application Programming Interfaces, or APIs, allow frontend development interfaces and mobile apps to communicate with backend servers. Backend developers build and document APIs to expose application data and functionality.
    Security: Backend developers implement security controls and measures to protect server infrastructure and application data. This includes tasks like managing user authentication, restricting API access, and preventing malicious attacks.
    Optimization: Backend developers continuously monitor server performance and traffic to optimize infrastructure efficiency and scalability. They work to minimize response times, maximize throughput, and reduce costs.
    Coding Languages: Backend developers use programming languages optimized for server-side development like Java, PHP, Python, and C#. These languages interface with server environments and databases.

Backend development has several benefits, including:

    1. Data Management: Backend development is responsible for managing the data of the website or application, which includes storing and retrieving data from databases, managing user authentication and authorization, and ensuring data security.
    2. Scalability: A well-designed backend architecture can support the website or application's growth and scalability by allowing for the addition of new features and functionalities without compromising performance.
    3. Performance: Backend developers optimize the website or application's performance by implementing efficient algorithms, minimizing database queries, and reducing server response time.
    4. Customization: Backend development allows for customization of the website or application to meet specific business needs, including creating unique features, integrating with other systems, and enabling automation.
    5. Security: Backend developers implement security measures to protect the website or application from cyber-attacks and unauthorized access, such as encryption, firewalls, and secure APIs.

Resources:

- https://intellipaat.com/blog/what-is-backend-development/
- https://www.quora.com/What-are-the-benefits-of-backend-development

Web Servers

A web server is a computer that hosts web pages, making them accessible online. When a user loads a site, the web server retrieves the relevant files and sends them to the browser so the user can interact with them.

Web and application servers follow a client-server model. In this structure, one program – the client – requests a resource or service from another program – the server.

Web servers use Hypertext Transfer Protocol (HTTP) when responding to user requests via the World Wide Web. HTTP is a protocol used to exchange information between computers.

Through the HTTP request process, servers can deliver the site’s HTML document to the user’s web browser, like Google Chrome.

Here’s an overview of the whole process to give you a better understanding:

- When someone wants to load a website, the browser looks for the web server hosting the site’s files.
- To achieve this, the web browser translates the site’s domain name into an IP address via the Domain Name System (DNS). If the site is frequently visited, the web browser searches through its file cache.
- After finding the corresponding web server, the browser sends an HTTP request to retrieve site content.
- The web server receives and processes the HTTP request through its HTTP server. Once the HTTP server accepts the request, it searches through the database to obtain the relevant data.
- Finally, the server returns the files to the web browser and delivers them to users.
- When the HTTP server fails to find or process the requested files, it sends an HTTP error status code to the browser.

The most common error message is a 404 error, which means the requested page is missing. Meanwhile, a 403 error may appear if there are permission issues.

Furthermore, if a web server fails to receive a timely response from another server acting as a proxy or gateway, a 504 error occurs.

How do web servers work?

A page on the internet can be viewed when the browser requests it from the web server and the web server responds with that page. The simple process consists of 4 steps:

1. Obtaining the IP Address from the domain name:

   - By searching in its cache.
   - By requesting one or more DNS (Domain Name System) Servers.

2. Browser requests the full URL.

3. The web server responds to the request:

   - The web server sends the desired pages, and in case the pages do not exist or an error occurs, it sends the appropriate error message.
   - Examples of error messages include Error 404, which is sent when the page does not exist, and Error 401, which is sent when access is denied due to incorrect credentials.

4. The browser displays the web page or the error message.

Performance measures of web servers include:

- RPS (Requests per second): It determines the maximum number of requests a server can handle from various clients.
- Latency: It is the response time that a server takes to process each client’s request.
- Throughput: It is the amount of data transferred in a given amount of time.
- Concurrency: It is a parameter used to check the performance of a web server under various specifications.

Popular web servers include:

1. Apache HTTP Server: It is the most popular web server available and is widely used. It is developed and maintained by Apache Software Foundation. It is free and open-source.

2. Microsoft Internet Information Service (IIS): It is the second most popular web server and its market share is increasing rapidly. It is developed and maintained by Microsoft and works with all Windows operating systems.

In summary, web servers can be used by individuals or web hosting provider companies. Individuals can locally host websites on their own systems, while hosting provider companies allow websites to be viewed by anyone across the globe. There are various types of web servers available, each with its own features and capabilities.

Some web server types include:

1. Apache HTTP Server
2. Microsoft Internet Information Services
3. Lighttpd
4. Nginx Web Server
5. Sun Java System Web Server (SJSAS)

Each of these web servers has its own strengths and is suitable for different use cases.

Resources:

- https://www.geeksforgeeks.org/web-servers-work/
- https://www.hostinger.com/tutorials/what-is-a-web-server
- https://medium.com/@sanchit0496/what-is-a-web-server-different-types-of-web-servers-c0bd1a1b4b43

Proxy Server

A proxy server is a system or router that provides a gateway between users and the internet, preventing cyber attackers from entering a private network. It acts as an intermediary between end-users and the web pages they visit online. When a computer connects to the internet, it uses an IP address, similar to a home's street address, directing incoming and outgoing data. A proxy server, with its own IP address, works by receiving requests from a computer, routing them to the web server, and forwarding the data to the computer's browser (e.g., Chrome, Safari, Firefox, or Microsoft Edge).

Proxy Server Types:

1. Forward Proxy:

   - Sits in front of clients and is used to provide data to groups of users within an internal network.
   - Best suited for internal networks requiring a single point of entry, offering IP address security and administrative control.
   - May limit an organization's ability to cater to individual end-users.

2. Transparent Proxy:

   - Provides users with an experience identical to using their home computer, while also being capable of forced connections.
   - Well-suited for companies desiring proxy usage without employee awareness, ensuring a seamless user experience.
   - More susceptible to security threats, such as SYN-flood denial-of-service attacks.

3. Anonymous Proxy:

   - Focuses on making internet activity untraceable, hiding the user's identity and computer information.
   - Ideal for users seeking full anonymity while accessing the internet.
   - Some view the use of anonymous proxies as underhanded, leading to potential pushback or discrimination.

4. High Anonymity Proxy:

   - Takes anonymity a step further by erasing user information before connecting to the target site.
   - Best suited for users requiring absolute anonymity, such as employees not wanting their activity traced back to the organization.
   - Some free high anonymity proxies may attempt to access personal information or data.

5. Distorting Proxy:

   - Identifies itself as a proxy to websites but conceals its own identity by changing its IP address.
   - Suitable for users wanting to hide their location while accessing the internet, providing both user and proxy identity security.
   - Some websites automatically block distorting proxies, potentially limiting access.

6. Data Center Proxy:

   - Not affiliated with an internet service provider (ISP) and provided by another corporation through a data center.
   - Offers quick response times and an inexpensive solution, making it suitable for gathering intelligence swiftly and inexpensively.
   - Does not provide the highest level of anonymity, potentially risking user information or identity.

7. Residential Proxy:

   - Gives users an IP address associated with a specific physical device, channeling all requests through that device.
   - Well-suited for users needing to verify ads on their websites and block unwanted or suspicious ads.
   - More trustworthy than other proxy options but often comes at a higher cost.

8. Public Proxy:

   - Accessible to anyone free of charge, granting users access to its IP address for anonymous site visits.
   - Best suited for users prioritizing cost over security and speed.
   - Increased risk of information access by others on the internet.

9. Shared Proxy:
   - Used by multiple users simultaneously, providing access to an IP address shared by others.
   - Allows browsing from a chosen location while offering a cost-effective solution.
   - May not provide a fast connection.

Benefits and Drawbacks of Proxy Servers:

1. Enhanced Security:

   - Acts as a firewall, preventing hackers from easily accessing your IP address and infiltrating your computer or network.

2. Private Browsing:

   - Helps avoid unwanted ads and IP-specific data collection, ensuring protected and untraceable site browsing.

3. Access to Location-Specific Content:

   - Designate a proxy server with an address associated with another country to access content restricted to that location.

4. Restrict Inappropriate or Distracting Site Access:
   - Block websites conflicting with organizational principles and eliminate distractions from important tasks.

Resources:

- https://www.fortinet.com/resources/cyberglossary/proxy-server
- https://whatismyipaddress.com/using-proxies
- https://www.youtube.com/watch?v=Lz4AdRpG6qo

OSI Model

The OSI ("Open Systems Interconnection") model represents an easy and intuitive way to standardize the different parts required to communicate across networks.

The model makes it clear what is required to communicate on a network by splitting the requirements into multiple layers.

Its structure is based on 7 layers:

7. Application
8. Presentation
9. Session
10. Transport
11. Network
12. Data link
13. Physical

The top 3 layers are typically implemented in software within the operating system, and the bottom 3 layers are typically implemented in hardware within devices on the network, such as switches, routers, and firewalls. Layer 4, the Transport layer, connects the software with the hardware layers.

OSI Model Layers

- Application Layer:
  It contains the functionality of the application and is what users use to interact with services across a network. Examples of applications include HTTP and FTP.

- Presentation Layer:
  It is responsible for adapting, transforming, and translating data to ensure that the application and underlying layers can understand each other.

- Session Layer:
  It handles connections between the application and the layers below, including establishing, maintaining, and terminating connections.

- Transport Layer:
  It allows applications to be represented on the network. The most famous protocols known on the Transport Layer are TCP and UDP.

- Network Layer:
  It is responsible for routing packets between networks via routers. The IP (Internet Protocol) is used in this layer. It handles all aspects related to IP addresses.

- Data link Layer:
  It links networks and consists of protocols designed to send packets through physical connections. In other words, the Data link Layer is responsible for moving data from the physical layer to the logical layer (the network layer). It handles all aspects related to MAC addresses.

- Physical Layer:
  It acts as a bridge between the digital information processed by higher layers and the physical transmission medium.

The Relationship between the OSI and Backend Development:
The OSI model itself is not directly tied to backend development. However, it provides a foundation for understanding how data flows through a network, which can be relevant for backend developers working on networked applications.

Resources:

- https://www.w3schools.com/cybersecurity/cybersecurity_networking.php
- https://www.imperva.com/learn/application-security/osi-model/

networking

IP Addressing
All computers on the Internet network communicate with each other using underground or underwater cables or wirelessly. For any internet-related activity, such as downloading files or loading web pages, a computer must have an address called an IP Address or Internet Protocol Address.
Internet Protocol is a set of rules that enables the internet to function.
IP addresses utilize protocols to send and receive data and files to connected devices. There are several steps involved behind the scenes.

Types of IP Address
IPv4: Internet Protocol version 4 consists of four numbers separated by dots. Each number can range from 0 to 255 in decimal format.

    Classes of IPv4 Address: To manage the large number of IPv4 addresses, they are organized and divided into five classes in numeric order:
        Class A: 1-126
        Class B: 128-191
        Class C: 192-223
        Class D: 224-239 (Reserved for multitasking)
        Class E: 240-254 (Reserved for Research and development)

    IPv6: It is a 128-bit IP address that can assign unique addresses to an immense number of devices, more than enough for future generations.

Ports
A port or port number is a unique number assigned to identify a connection endpoint and direct data to a specific service. Ports are handled at the software level within an operating system.
Ports are used in the Transport Layer and serve as a logical construct to identify a specific process or network service.
The most common transport protocols that use port numbers are the Transmission Control Protocol (TCP) and the User Datagram Protocol (UDP).
There are many common port numbers, for example:
80: HTTP
443: HTTP Secure (HTTPS)
20, 21: File Transfer Protocol (FTP)
25: Simple Mail Transfer Protocol (SMTP)

TCP/IP
TCP/IP is the communication protocol for computers on the Internet.
TCP/IP stands for Transmission Control Protocol / Internet Protocol.
TCP/IP defines how electronic devices, like computers, should be connected to the Internet and how data should be transmitted between them.
Browsers use TCP/IP to access Internet servers, and servers use TCP/IP to send HTML back to the browser.
Email programs use TCP/IP to connect to the Internet for sending and receiving emails.
An Internet address is part of the standard TCP/IP protocol.
Within the TCP/IP standard, there are several protocols for handling data communication:
TCP: Transmission Control Protocol for communication between applications
UDP: User Datagram Protocol for simple communication between applications
IP: Internet Protocol for communication between computers
ICMP: Internet Control Message Protocol for errors and statistics
DHCP: Dynamic Host Configuration Protocol for dynamic addressing

Relationship between TCP/IP and IP
TCP/IP is a combination of TCP and IP.
TCP handles communication between application software (e.g., browser) and network software.
IP handles communication with other computers.
TCP breaks down data into IP packets before sending and reassembles them upon arrival.
IP ensures packets are sent to the correct destination.

The Relationship between TCP/IP and Backend Development
While TCP/IP is not directly tied to backend development concepts like server-side programming or data storage, knowledge of TCP/IP is crucial for backend developers to design, implement, and maintain networked applications and services effectively.

Resources:

- https://www.geeksforgeeks.org/what-is-an-ip-address/
- https://en.wikipedia.org/wiki/Port_(computer_networking)
- https://w3schools.sinsixx.com/tcpip/default.asp.htm
- https://w3schools.sinsixx.com/tcpip/tcpip_intro.asp.htm

http

HTTP stands for Hyper Text Transfer Protocol. It is a protocol for fetching resources such as HTML documents. It is the foundation of any data exchange on the Web and it is a client-server protocol. Clients and servers communicate by exchanging individual messages (as opposed to a stream of data). The messages sent by the client, usually a web browser, are called requests, and the messages sent by the server as an answer are called responses. It is an application layer protocol that is sent over TCP, or over a TLS-encrypted TCP connection.

HTTP Request / Response

1. A client (a browser) sends an HTTP request to the web.
2. A web server receives the request.
3. The server runs an application to process the request.
4. The server returns an HTTP response (output) to the browser.
5. The client (the browser) receives the response.

The HTTP Request Circle

The browser requests an HTML page. The server returns an HTML file.
The browser requests a style sheet. The server returns a CSS file.
etc...

The Relationship between HTTP and Backend Development

HTTP is an essential component of backend development as it enables the seamless transfer of data and communication between clients and servers. It provides a standardized protocol for building web applications, APIs, and other backend systems.

Resources:

- https://www.w3schools.com/whatis/whatis_http.asp
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview

REST API

REST API, short for Representational State Transfer Application Programming Interface, is a set of architectural constraints and principles used for designing networked applications. It is an architectural style, not a protocol, that is based on the principles of simplicity, scalability, and uniformity. REST was introduced by Roy Fielding in his doctoral dissertation in 2000 and has since become the de facto standard for designing web-based APIs.

Key Principles of REST

1. Statelessness: Each request from a client to a server must contain all the information needed to understand and process the request. The server should not store any client context between requests, improving scalability and reliability.

2. Client-Server Architecture: REST separates the client and server, allowing them to evolve independently. This separation enhances the overall system's scalability and maintainability.

3. Resource-Based: Resources, such as data objects or services, are identified by unique URIs (Uniform Resource Identifiers). Clients interact with these resources using a limited set of well-defined methods, such as GET, POST, PUT, and DELETE.

4. Representation: Resources can have multiple representations, such as JSON, XML, or HTML. Clients interact with these representations to access or modify the resource's state.

5. Stateless Communication: Each request from a client to a server must contain all necessary information, including authentication. This approach simplifies the server's task and improves reliability.

Benefits of REST API

1. Simplicity: RESTful APIs are easy to understand and use because they rely on standard HTTP methods and status codes. This simplicity reduces the learning curve for developers.

2. Scalability: By adhering to stateless communication and separating client and server concerns, REST APIs are inherently scalable. This makes them suitable for large-scale applications and microservices architectures.

3. Flexibility: REST allows for multiple data formats, making it adaptable to various client needs. This flexibility enables clients to request data in their preferred format.

4. Platform Independence: REST APIs can be accessed from different platforms and devices, promoting interoperability and compatibility.

Common Use Cases

1. Web Services: RESTful APIs power web services like social media platforms, e-commerce websites, and news aggregators, allowing them to retrieve and exchange data.

2. Mobile Applications: Mobile apps often communicate with server-side components through REST APIs to fetch data, perform authentication, and execute other functions.

3. IoT (Internet of Things): RESTful APIs enable IoT devices to send and receive data, facilitating remote control and monitoring.

4. Integration: REST APIs are used for integrating different software systems and services, enabling them to work together seamlessly.

Best Practices

1. Use Appropriate HTTP Methods: Employ HTTP methods like GET, POST, PUT, and DELETE according to their intended purposes to ensure a clear and intuitive API design.

2. Versioning: Include version information in the API's URI to maintain backward compatibility while allowing for updates and improvements.

3. Authentication and Authorization: Implement robust security mechanisms to protect sensitive data and restrict access to authorized users.

4. Documentation: Provide comprehensive API documentation to assist developers in understanding and using your API effectively.

5. Error Handling: Use meaningful error codes and descriptions to help clients troubleshoot issues.

Nginx

Nginx is an open-source web server and reverse proxy server software known for its high performance. It efficiently handles web traffic, making it a popular choice for serving websites and applications. Nginx's main function is to accept incoming HTTP requests from clients, such as web browsers, and distribute them to the appropriate backend servers hosting web applications or serving static content.

Nginx's architecture is based on an event-driven, asynchronous model. It utilizes a single-threaded, non-blocking approach to handle multiple client connections simultaneously. Instead of spawning new processes or threads for each request, Nginx uses an event loop to efficiently manage and process requests.

Some benefits of using Nginx include:

- High Performance: Nginx is known for its speed and efficiency, making it ideal for high-traffic websites and applications.
- Load Balancing: Nginx can distribute incoming traffic across multiple backend servers, ensuring even resource utilization and high availability.
- Reverse Proxy: It can act as a reverse proxy, providing an extra layer of security and allowing for advanced request handling, such as SSL termination and caching.
- SSL/TLS Termination: Nginx can handle SSL/TLS encryption and decryption, offloading this resource-intensive task from backend servers.
- Caching: Nginx supports caching of static and dynamic content, reducing the load on backend servers and improving content delivery.

In addition, Nginx Unit is a modern offering from the Nginx team that addresses common challenges in contemporary development processes. It brings benefits such as standardized configuration, a declarative configuration model, and reconfiguration without restarts. Nginx Unit simplifies the management of production deployments and serves as an alternative for hosting applications in various languages.

Configuring Nginx for backend development involves creating server blocks, defining location blocks, and configuring proxying for backend applications. The specific steps may vary depending on the use case, such as setting up Nginx to serve a Node.js application. For load balancing, the process typically involves defining an upstream element, listing backend nodes, and mapping URIs to the upstream cluster.

Resources:

- https://www.nginx.com/resources/glossary/nginx/
- https://docs.nginx.com/nginx-service-mesh/about/architecture/
- https://octopus.com/blog/why-use-nginx-unit
- https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/How-to-setup-an-Nginx-load-balancer-example

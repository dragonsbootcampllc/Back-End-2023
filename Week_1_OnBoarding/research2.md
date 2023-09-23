# Research

- ### Introduction
  ##### In this section we will talk about back and its components and the benefits of it
  - At first Back-End :
    What is it and how it involves in our world life ?
    The simple answer is every website , system , mobile application has a back end
    Now what is back end ?
    Back end is a layer of the architecture of any working software which handling the data that shows to
    the user while he is using the system I.E when you are using Facebook and you commented or reacted
    on post when you refresh or visit this post again you info ( react and comment ) is shown to you
    and to every person using Facebook another simple example when you sign up in any website your
    data stored so when you sign in again the website system will recognize you. It also handling the
    action on servers and requests accepting and response sending it also handling the routing of your
    website in brief the back end makes your front end works Front end without back end is nothing
    because the the response of interaction with front end back end is making it (i do not mean
    animations !!) and back end without front end is also nothing because the user will not find a
    friendly user interface to interact with. I mentioned database which is one of the components of
    the back end also the servers and of course the app itself. Till now we Knew the back end and its
    components and the benefits of it in the next section we will talk about on of these components
    which is web servers.
- ### Web Servers
  in this section we will talk about web server and its types and how it works
  - A web server is a software or hardware that keeps all the data about your website the pages , styles , java script files , ... etc. so for example when you type the URL of your website the page which you requested is stored on the server and the response will return to you as an http response ( we will talk about http later ) also keeps the database to store in and get information from. Now we have may types of web servers i will mention some Apache HTTP Server , Internet Information Services , Nginx , ...etc.
    We will take Nginx and Apache HTTP server to give an example of the difference between web servers in the benefits and drawbacks
  - Apache HTTP Server
    - Benefits
      - Long-established and widely used, making it well-documented and supported.
      - High configurability and extensibility through modules.
      - Platform-independent and available on various operating systems.
      - Excellent support for dynamic content generation through technologies like PHP and Python.
    - Drawbacks
      - Can be resource-intensive, especially when handling a large number of concurrent connections.
      - Complex configuration files might be challenging for beginners.
  - Nginx
    - Benefits
      - Lightweight and efficient, capable of handling a high number of concurrent connections with low resource usage.
      - Designed for proxying and load balancing, making it suitable for reverse proxy setups.
      - Excellent support for serving static content.
      - Configuration syntax is more straightforward and easier to manage than Apache's.
    - Drawbacks
      - Limited support for dynamic content out of the box, often requiring additional modules or configurations.
      - Not as feature-rich as Apache when it comes to certain advanced functions.
- ### Proxy servers
  It is a Server application that works in middle of the client and the server It means when the client uses a proxy server the client is not acting with the server directly it is acting with the server through the proxy server in this section we will talk about it in details and its different types and how to use it
  - Proxy server is working a middle layer between client and resource server and it could be a working computer in details when you send a request to visit a website and the request IP you send is forbidden in this website Proxy server get your request and send it to the server with an acceptable IP and get the request from the server and send it again to the client.There are different types of proxy server like
    forward proxy : Forward proxies are used to transmit data to groups of user within an internal network
    Public proxy : Public proxies are available to anyone, and it works by providing its users its IP address to hide their identity.
    Shared proxy : This proxy enables multiple users to engage with this proxy in a given time by providing the users with a shared IP address.
    TOR proxy : This proxy directs data across various networks globally present to obscure the user’s address.
    of course there is more Types of proxy servers.
    Ok now why we use proxy servers in other word what is the benefits and drawbacks of proxy servers.
    Benefits --> (Anonymity , Speed , Content Filtering , Security)
    Drawbacks --> (Limited Functionality , Privacy Concerns , Single-Point Failure)
    After all I mentioned how to use a proxy server on your pc in network settings you go to proxy settings and if you want to set it manually you have to know proxy server name or IP address and port to connect to the proxy server and save it by this you are using this proxy server
  - Resource used `https://en.wikipedia.org/wiki/Proxy_server`
- ### OSI model
  OSI model (Open System Interconnection) it is made by IEEE it handles the connection between different systems in 7 layer each layer do a specific job we will explain the layers and because our intro was about back end we will know how OSI related to it
  - The layers of the OSI model
    Software layer --> Contains (Application layer (Include the application you uses and the request you do on it) , Presentation layer (Translate the data to binary and encrypt it) , session layer (Authentication , Authorization , session management))
    Transport layer --> Using transport protocol like TCP , UPD to transfer file over the network also has error detection and flow control and also make segmentation to the data to send it in the sender side and reassembly in the receiver side
    Hardware layer --> Contains (Network layer (Convert segment to packet by adding sender and receiver IPs so it controls the transmission of data from one host to the other located in different networks) , Data Link Layer(Converts packet to frame by adding MAC address of sender and receiver and it is responsible to node-to-node delivery ) , Physical layer (converts the bits to a physical signals to electric signal (in wires) or radio signals (in WIFI ) or optical signal(in fiber optics) ) ).
    In brief when you send a message from your pc you are in the application layer after that the message will go to presentation layer to be encrypted and translated to 0 1 and then go to session layer to check the Authentication and Authorization to send and manage the session and the connection and then go to transport layer to decide which transport protocol to use and handle error and separate the data to segments (segmentation) and then every segment goes to network layer to add IP of the sender and receiver and then you have a packet and then go to data link layer to convert it to frame by adding MAC addresses to transmit in different media like routers and radio waves and wires then go to physical layer that converts the frame to signal to go when they find the receiver goes from down to up and in transportation layer will make Reassemble for the data received and go to application layer to be shown on the receiver application layer.It helps the back end because it is the foundation of data transportation between servers and clients.
  - Resources `https://www.geeksforgeeks.org/open-systems-interconnection-model-osi/`
- ### Networking
    Now we will talk about some concepts we all hear about networking like IP , Ports ,TCP/IP
        -IP --> Is Internet Protocol 
        -IP addressing : is a system used to uniquely identify and locate devices on a computer network that uses the Internet Protocol for communication. It is a fundamental part of the Internet and most other networks, including local area networks (LANs) and wide area networks (WANs)
        - Ports : Ports in the context of computer networking and the Internet refer to a standardized method for applications and services to communicate over a network. Ports act as endpoints for network connections, allowing multiple applications and services to run simultaneously on a single device, such as a computer or server. Ports numbers are in range from 0 to 65,535 divided to 
        Well-Known Ports from 0 to 1023 i.e port 80 is typically associated with HTTP (web) traffic, while port 25 is used for SMTP (email) communication.
        Registered and Dynamic Ports are from 1024 to 65,535 These ports are often allocated dynamically by the operating system when an application or service initiates network communication.
        - TCP/IP : TPC (Transmission Control Protocol)  is a suite of networking protocols that form the foundation of the modern internet and most computer networksIt provides a set of rules and conventions for how data should be transmitted, routed, and received over networks.And obviously is contains TCP and IP protocols. It is related to back end because it plays a role in the networked applications in database communication and server communication to get pages and data in other word back end process like getting pages and data is made via this suite 
- ### HTTP
    HTTP (Hypertext Transfer Protocol) is an application layer protocol used for transmitting and receiving data over the World Wide Web it has some requests and status codes we will figure out in the next lines 
        - It works as the following when you request an html file -for example- you send an http request the this is get request the server will send you a http response with this file in brief it works as a request-response protocol that enables the communication between a client and a web server.
        Types of HTTP protocol (GET (Retrieve data from the server.), POST(submit data to be processed by the server.) , PUT(Update or replace a resource on the server.) , DELETE(Request removal of a resource on the server.) , PATCH(Partially update a resource on the server.) )
        Status codes are many so I will mention the most common (100 Continue , 200 OK , 302 Found (or 303 See Other) , 401 Unauthorized , 403 Forbidden , 404 Not Found , 503 Service Unavailable , 504 Gateway Timeout)
        It also involves to back end s it serves as the foundation for communication between clients and backend servers. Backend development involves creating and managing server-side applications and services that respond to HTTP requests from clients.
- ### REST APIs
	Representational State Transfer Application Programming Interface, is a set of rules and conventions for building and interacting with web services and web-based resources.REST is an architectural style that uses standard HTTP methods, URIs (Uniform Resource Identifiers), and various other principles to enable communication between clients (such as web browsers or mobile apps) and servers.It provide set of rules and conventions for clients to communicate with servers over the HTTP Using HTTP methods of course.Its advantages are (Simplicity and Ease of Use , Compatibility with HTTP , Statelessness , Scalability). Some of its end points (User-related Endpoints , Post-related Endpoints , Comment-related Endpoints , Category or Tag-related Endpoints).Finally how to use it or in details how to implement it follow this process 
	- Define the Purpose and Scope
	- Identify Resources
	- Define CRUD (Create, Read, Update, Delete ) Operations
	-Design Resource Representations
	-Use HTTP Status Codes that we mentioned in the previous section

- ### Nginx
	pronounced "engine-x" is a high-performance, open-source web server and reverse proxy server software. Developed by Igor Sysoev in 2004. It works as a web server ( we has explained how web servers works in web servers section ) , as a reverse proxy server , a load balancer and and with HTTP caching (save the info locally so when you send a request to the same website and it didn't changed from the last request it comes to you from caching).Some of its benefits (High Performance , Low Resource Usage , SSL/TLS Support(For security) , Flexibility , Ease of Configuration , Compatibility , Scalability , Security). Finally how to configure it to use it in backend development follow this process
	on powerShell or CMD
	- Download Nginx for Windows
	`https://nginx.org/en/download.html`
	- Extract Nginx
	- Configuration
	- Start Nginx
	in the directory of nginx type `nginx.exe` in powerShell or CMD
	- Test Configuration
	write `nginx.exe -t`
	- Access Your Backend
	With Nginx running, you can access your backend server through Nginx by opening a web browser and navigating to http://localhost or the server name you specified in your configuration
	- Stop Nginx
	Run this in powerShell or CMD `nginx.exe -s stop`
	- Monitoring and Logs:

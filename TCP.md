# **The Transmission Control Protocol (TCP)**
 >### 1. *What is a TCP?*
 **_The Transmission Control Protocol (TCP):_** 
 is one of the main protocols of the Internet protocol suite. It originated in the initial network implementation in which it complemented the Internet Protocol (IP). Therefore, the entire suite is commonly referred to as TCP/IP. TCP provides reliable, ordered, and error-checked delivery of a stream of octets (bytes) between applications running on hosts communicating via an IP network. Major internet applications such as the World Wide Web, email, remote administration, and file transfer rely on TCP, which is part of the Transport Layer of the TCP/IP suite. SSL/TLS often runs on top of TCP.

 ---
 ---
 >### 2. *What is IP?*
__The Internet Protocol (IP)__ is the method for sending data from one device to another across the internet. Every device has an IP address that uniquely identifies it and enables it to communicate with and exchange data with other devices connected to the internet.  Today, it’s considered the standard for fast and secure communication directly between mobile devices.



<img src="https://blog.apnic.net/wp-content/uploads/2019/07/Olaf_Fig-1.png" alt="Alt Text" width="250" height="250" style="margin-left: 270px; ">



IP is responsible for defining how applications and devices exchange packets of data with each other. It is the principal communications protocol responsible for the formats and rules for exchanging data and messages between computers on a single network or several internet-connected networks. It does this through the Internet Protocol Suite (TCP/IP), a group of communications protocols that are split into four abstraction layers.

IP is the main protocol within the internet layer of the TCP/IP. Its main purpose is to deliver data packets between the source application or device and the destination using methods and structures that place tags, such as address information, within data packets.

 ---
 ---
 >### 3.**_TCP vs. IP: What is the Difference?_**
TCP and IP are separate protocols that work together to ensure data is delivered to its intended destination within a network. IP obtains and defines the address—the IP address—of the application or device the data must be sent to. TCP is then responsible for transporting and routing data through the network architecture and ensuring it gets delivered to the destination application or device that IP has defined. Both technologies working together allow communication between devices over long distances, making it possible to transfer data where it needs to go in the most efficient way possible.

In other words, the IP address is akin to a phone number assigned to a smartphone. TCP is the computer networking version of the technology used to make the smartphone ring and enable its user to talk to the person who called them. 

Now that we’ve looked at TCP and ICP separately, what is TCP/IP? The two protocols are frequently used together and rely on each other for data to have a destination and safely reach it, which is why the process is regularly referred to as TCP/IP. With the right security protocols in place, the combination of the TCP/IP allows users to follow a safe and secure process when they need to move data between two or more devices.

 ---
 ---
  > ### 3. *TCP  work is a general idea*
  TCP is a connection-oriented protocol, which means a connection is established and maintained until the applications at each end have finished exchanging messages.

**TCP performs the following actions:**

1. determines how to break application data into packets that networks can deliver;
2. sends packets to, and accepts packets from, the network layer;
3. manages flow control;
4. handles retransmission of dropped or garbled packets, as it's meant to provide  error-free data transmission;
5. acknowledges all packets that arrive.


<img src="https://pimages.toolbox.com/wp-content/uploads/2022/04/05123619/10-2.png" alt="Alt Text" width="200" height="300"  style="margin-left: 270px; ">


---
---

>### 4. How work TCP ?
It works in several steps:
1. <span style="color:#1565c0;">**Connection Establishment:**</span>  
Before data transfer can begin, a connection must be established between the sender and receiver. This is achieved through a process called the three-way handshake:
  * <span style="color:#9fa8da;">**_Step 1 (SYN):_**</span>   The sender (client) initiates the connection by sending a SYN (synchronize) packet to the receiver (server), indicating its intention to establish a connection.
  
* <span style="color:#9fa8da;">**_Step 2 (SYN-ACK):_**</span>  The receiver responds with a SYN-ACK packet, acknowledging the client's request and indicating its readiness to establish a connection.
* <span style="color:#9fa8da;">**_Step 3 (ACK):_**</span> The client sends an ACK packet back to the server, confirming the connection establishment. At this point, data transfer can commence.

<img src="https://i.imgur.com/CdjvCNr.png
" alt="Image" style="margin-left: 250px; "  />

2. <span style="color:#1565c0;">**Data Transfer:**</span> 
Once the connection is established, data can be exchanged between the sender and receiver. TCP divides the data into smaller units called segments and assigns a unique sequence number to each segment. The sender sends these segments, and the receiver acknowledges their receipt.
TCP implements flow control mechanisms using a sliding window approach. The sender keeps track of the receiver's available buffer space and adjusts the rate of transmission accordingly. This prevents overwhelming the receiver and helps manage congestion.

3. <span style="color:#1565c0;">**Reliable Data Delivery:**</span> TCP ensures reliable data delivery through several mechanisms:
* <span style="color:#9fa8da;">**_Acknowledgments (ACKs):_**</span>  The receiver sends acknowledgment packets (ACKs) to the sender to confirm the receipt of data segments. If the sender doesn't receive an ACK for a segment within a certain time (known as the retransmission timeout), it assumes the segment was lost and retransmits it.

* <span style="color:#9fa8da;">**_Sequence Numbers:_**</span>  The sender assigns sequence numbers to segments to ensure proper ordering. The receiver uses these sequence numbers to reassemble segments in the correct order.

* <span style="color:#9fa8da;">**_Selective Acknowledgment (SACK):_**</span>  In some cases, the receiver can use SACK to acknowledge the receipt of specific segments, allowing the sender to retransmit only the missing or lost segments.

* <span style="color:#9fa8da;">**_Buffering and Flow Control:_**</span>  TCP uses sliding windows to manage the flow of data and prevent congestion. The sender adjusts the window size based on acknowledgments and the receiver's available buffer space.

<img src="https://tetcos.com/help/v13.2/images/Experiments-Manual/Reliable-data-transfer-with-TCP/media/image1.jpg" alt="Alt Text" width="250" height="250" style="margin-left: 270px; ">


4. <span style="color:#1565c0;">**Connection Termination:**</span>
When data transfer is complete, the connection needs to be gracefully terminated. This is achieved through a four-way handshake:
* <span style="color:#9fa8da;">**_Step 1 (FIN):_**</span> One party initiates the termination process by sending a FIN (finish) packet.

* <span style="color:#9fa8da;">**_Step 2 (ACK):_**</span> The other party acknowledges the FIN packet with an ACK packet.

* <span style="color:#9fa8da;">**_Step 3 (FIN)_**</span>  The other party also sends a FIN packet to initiate its termination.

* <span style="color:#9fa8da;">**_Step 4 (ACK):_**</span>  The initiating party acknowledges the second FIN packet with an ACK packet. The connection is now fully closed.

<img src="https://media.geeksforgeeks.org/wp-content/uploads/CN.png" alt="Alt Text" width="250" height="250" style="margin-left: 270px; ">


---
---
 > ### 5. *TCP vs. UDP:*
 **_1. UDP:_**

UDP stands for User Datagram Protocol. It is a core communication protocol of the Internet Protocol Suite (TCP/IP) and is used for connectionless, lightweight, and low-overhead data transmission between devices on a network. UDP is an alternative to the more reliable but heavier Transmission Control Protocol (TCP).<span style="color:#9fa8da;"> Unlike TCP, UDP does not establish a formal connection before sending data and does not provide the same level of error correction and reliability.</span>

* **the difference between TCP and UDP :**
This process of error detection, in which TCP retransmits and reorders packets after they arrive, can introduce latency in a TCP stream. Highly time-sensitive applications, such as voice over IP (VoIP), streaming video and gaming, generally rely on a transport process such as User Datagram Protocol (UDP), because it reduces latency and jitter by not reordering packets or retransmitting missing data.
UDP is classified as a datagram protocol, or connectionless protocol, because it has no way of detecting whether both applications have finished their back-and-forth communication. Instead of correcting invalid data packets, as TCP does, UDP discards those packets and defers to the application layer for more detailed error detection.
The header of a UDP datagram contains far less information than a TCP segment header. The UDP header also goes through much less processing at the transport layer in the interest of reduced latency.

---
---

 > ### 6. *TCP application in real life:*
 **_Some TCP application in real life:_**

1. <span style="color:#9fa8da;">**_Web Browsing (HTTP):_**</span> 
TCP is essential for web browsing, as it ensures that web pages and their elements (images, text, videos) are reliably and efficiently delivered from web servers to users' browsers. The HyperText Transfer Protocol (HTTP) relies on TCP to establish connections and transmit web content.

2. <span style="color:#9fa8da;">**_Email Communication (SMTP, POP3, IMAP):_**</span>
TCP enables email communication by providing a reliable transport mechanism for sending and receiving emails. Protocols like Simple Mail Transfer Protocol (SMTP) for sending emails and Post Office Protocol (POP3) and Internet Message Access Protocol (IMAP) for retrieving emails rely on TCP.

3. <span style="color:#9fa8da;">**_File Transfer (FTP):_**</span>
TCP is used for secure and reliable file transfer between computers using the File Transfer Protocol (FTP). FTP ensures that files are transferred intact and can handle large files efficiently.

4. <span style="color:#9fa8da;">**_Remote Access (SSH, Telnet):_**</span>
TCP is utilized for remote access to systems through protocols like Secure Shell (SSH) and Telnet. These protocols allow users to connect to and manage remote computers securely and efficiently.

5. <span style="color:#9fa8da;">**_Database Access:_**</span>
TCP is used for accessing databases remotely, allowing applications to query and retrieve data from databases securely and reliably.

---
---
 > ### 7. *Services offered by the TCP:*
 **_Services offered by the TCP are as follows:_**
 1. Process to Process or end to end Communication using Port numbers.

 2. Transmits the data as a stream of bytes from source to destination
It groups the data that comes from the application into packets called Segments. It also adds a header to each data segment and sends it to the network layer.
3. It offers Full Duplex communications .
4. Reliable Service: TCP uses an acknowledgment mechanism which makes it reliable.
5. It offers Flow control, Error control, and Congestion control too.
---
---
> ### 8. *Advantages :*
1. Flow Control

2. Error Control
3. Congestion Control
4. Process to Process Communication
5. Inorder delivery of data segments
---
---
> ### 9. *Disadvantages :*
1. The data segments don’t get transmitted immediately 

2. More overhead(20-60Bytes)
3. It has a large TCP Header
---
---
> ### 10. **_Resources_**:
1. [Wikipedia](https://en.wikipedia.org/wiki/Transmission_Control_Protocol)

2. [Geeksforgeeks](https://www.geeksforgeeks.org/examples-of-tcp-and-udp-in-real-life/)
3. [Techtarget](https://www.techtarget.com/searchnetworking/definition/TCP)

4. [Fortinet](https://www.fortinet.com/resources/cyberglossary/tcp-ip)

5. [uff](http://www2.ic.uff.br/~michael/kr1999/3-transport/3_040-principles_rdt.htm)
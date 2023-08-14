## Hello, today I want to explain TCP to you

In this post, I will cover the following topics :

1. [**History of TCP**](#1-history-of-tcp)
2. [**What is TCP?**](#2-what-is-tcp)
3. [**What is an IP address?**](#3-what-is-an-ip-address)
4. [**TCP vs IP: What's the Difference?**](#4-tcp-vs-ip-whats-the-difference)
5. [**How does Transmission Control Protocol (TCP) / IP work?**](#5-how-does-transmission-control-protocol-tcp--ip-work)
6. [**The Four Layers of the TCP/IP Model**](#6-the-four-layers-of-the-tcpip-model)
7. [**Advantages and Disadvantages of TCP**](#7-advantages-and-disadvantages-of-tcp)
8. [**Tell you what is UDP**](#8-tell-you-what-is-udp)
9. [**What are the advantages and disadvantages of UDP?**](#9-what-are-the-advantages-and-disadvantages-of-udp)
10. [**What is the difference between UDP and TCP?**](#10-what-is-the-difference-between-udp-and-tcp)


Let's dive into each of these topics.

## 1. History of TCP

The world's most popular networking protocol, the **TCP/IP** protocol suite, was designed in the 1970s by two DARPA scientists - *Vint Cerf* and *Bob Kahn*, two people who are often called the **fathers of the Internet**.
While developing **TCP**, Cerf and Kahn used the concepts of *CYCLADES*, a French packet-switched network, designed and directed by *Louis Buzyn* in 1973. It was developed to explore alternatives to **ARPANET** design and to support network research in general. *CYCLADES* was the first network to make hosts responsible for reliable delivery of data, rather than the network itself, using unreliable datagrams and end-to-end protocol mechanisms.

**TCP/IP** has become the standard **Internet communications protocol** that allows digital computers to communicate over long distances. The Internet is a packet-switched network, in which information is broken into small packets, sent individually down many different paths at the same time, and then reassembled at the receiving end. **TCP** is the component that collects and reassembles data packets, while **IP** is responsible for ensuring that packets are sent to the correct destination. **TCP/IP** was developed in the 1970s and was adopted as the protocol standard for **ARPANET** (the predecessor to the Internet) in 1983.
The **TCP/IP** model consists of four layers, as described in **RFC 1122**. From lowest to highest, these are - *Link Layer*, *Internet Layer*, *Transport Layer*, and *Application Layer*. It should be noted that this model was not intended to be a strict reference model that new protocols must conform to in order to be accepted as a standard.

Almost all operating systems in use today, including all systems aimed at the consumer, include an implementation of **TCP/IP**.

There is a lot of history, but I will suffice with that information.

## 2. What is TCP?

**Transmission Control Protocol (TCP)** is a communications standard that enables application software and hardware to exchange messages over a network. It is designed to send packets over the Internet and ensure the successful delivery of data and messages across networks.

**TCP** is one of the basic standards that define the rules of the Internet and is included within the standards set by the *Internet Engineering Task Force (IETF)*. It is one of the most widely used protocols in digital network communications and ensures end-to-end data delivery.

**TCP** organizes data so that it can be transferred between the server and the client. It ensures the integrity of data delivered over the network. Before data is transmitted, **TCP** establishes a connection between the source and its destination, ensuring that it continues until the connection is initiated. It then splits large amounts of data into smaller packets, ensuring data integrity throughout the process.

As a result, higher-level protocols that need to transmit data use **TCP**. Examples include peer-to-peer sharing methods such as *File Transfer Protocol (FTP)*, *Secure Shell (SSH)*, and *Telnet*. It is also used to send and receive email through the *Internet Message Access Protocol (IMAP)*, *Post Office Protocol (POP)*, and *Simple Mail Transfer Protocol (SMTP)*, and to access the Web through *Hypertext Transfer Protocol (HTTP)*.

## 3. What is an IP address?

The **Internet Protocol (IP)** is the method for sending data from one device to another across the internet. Every device has an IP address that uniquely identifies it and enables it to communicate with and exchange data with other devices connected to the internet. Today, it’s considered the standard for fast and secure communication directly between mobile devices.

**IP** is responsible for defining how applications and devices exchange packets of data with each other. It is the principal communications protocol responsible for the formats and rules for exchanging data and messages between computers on a single network or several internet-connected networks. It does this through the *Internet Protocol Suite (TCP/IP)*, a group of communications protocols that are split into four abstraction layers.

**IP** is the main protocol within the internet layer of the **TCP/IP**. Its main purpose is to deliver data packets between the source application or device and the destination using methods and structures that place tags, such as address information, within data packets.

## 4. TCP vs IP: What's the Difference?

**TCP** and **IP** are separate protocols that work together to ensure data is delivered to its intended destination within a network. **IP** obtains and defines the address—the **IP address**—of the application or device the data must be sent to. **TCP** is then responsible for transporting and routing data through the network architecture and ensuring it gets delivered to the destination application or device that **IP** has defined. Both technologies working together allow communication between devices over long distances, making it possible to transfer data where it needs to go in the most efficient way possible.

In other words, the **IP address** is akin to a phone number assigned to a smartphone. **TCP** is the computer networking version of the technology used to make the smartphone ring and enable its user to talk to the person who called them.

Now that we’ve looked at **TCP** and **ICP** separately, what is **TCP/IP**? The two protocols are frequently used together and rely on each other for data to have a destination and safely reach it, which is why the process is regularly referred to as **TCP/IP**. With the right security protocols in place, the combination of the **TCP/IP** allows users to follow a safe and secure process when they need to move data between two or more devices.

## 5. How does Transmission Control Protocol (TCP) / IP work?

The **TCP/IP model** is the default method of data communication on the Internet. It breaks messages into packets to avoid having to resend the entire message in case it encounters a problem during transmission. Packets are automatically reassembled once they reach their destination. Every packet can take a different route between the source and the destination computer, depending on whether the original route used becomes congested or unavailable.

**TCP/IP** divides communication tasks into layers that keep the process standardized, without hardware and software providers doing the management themselves. The data packets must pass through four layers before they are received by the destination device, then **TCP/IP** goes through the layers in reverse order to put the message back into its original format.

It determines how the original message should be broken into packets, numbers and reassembles the packets, and sends them on to other devices on the network, such as routers, security gateways, and switches, then on to their destination. **TCP** also sends and receives packets from the network layer, handles the transmission of any dropped packets, manages flow control, and ensures all packets reach their destination.

A good example of how this works in practice is when an email is sent using **SMTP** from an email server. To start the process, the **TCP** layer in the server divides the message into packets, numbers them, and forwards them to the **IP** layer, which then transports each packet to the destination email server. When packets arrive, they are handed back to the **TCP** layer to be reassembled into the original message format and handed back to the email server, which delivers the message to a user’s email inbox.

## 6. The four layers of the TCP/IP model?

1. **Datalink layer**
2. **Internet layer**
3. **Transport layer**
4. **Application layer**

1) **Datalink layer**, **link layer**, **network access layer**, **network interface layer**, or **physical layer**:
The datalink layer defines how data should be sent, handles the physical act of sending and receiving data, and is responsible for transmitting data between applications or devices on a network. It is the combination of the physical and data link layers of the Open Systems Interconnection (**OSI**) model, which standardizes communications functions on computing and telecommunications systems.

2) **Internet layer**: The internet layer is responsible for sending packets from a network and controlling their movement across a network to ensure they reach their destination. It provides the functions and procedures for transferring data sequences between applications and devices across networks.

3) **Transport layer**: The transport layer is responsible for providing a solid and reliable data connection between the original application or device and its intended destination. This is the level where data is divided into packets and numbered to create a sequence. The transport layer then determines how much data must be sent, where it should be sent to, and at what rate. It ensures that data packets are sent without errors and in sequence and obtains the acknowledgment that the destination device has received the data packets.

4) **Application layer**:
The application layer refers to programs that need **TCP/IP** to help them communicate with each other. This is the level that users typically interact with, such as email systems and messaging platforms. It combines the session, presentation, and application layers of the **OSI** model.

## 7. Advantages and disadvantages of TCP?

**Advantages of TCP**

- **TCP** is connection-oriented.
- It establishes a connection between sender and receiver over the network before sending a message.
- It uses a congestion control policy to avoid congestions.
- Supports data retransmission. If the packets get lost failing to reach their destination, they will be sent back to the sender from the receiver. The sender can retransmit the packets.
- Performs in-order delivery by rearranging all packets at the receiving end.
- Error detection, such as corrupted and missing packets is easier. It is done through a three-step mechanism – checksum, retransmission, and acknowledgment.

**Disadvantages of TCP**

- It does not support broadcast or multicast transmission.
- **TCP** offers several features that we may not want. These features may result in a waste of bandwidth, time, or effort.

## 8. Tell you what is UDP:

**UDP** (**User Datagram Protocol**) is a connectionless Internet protocol. Error-checking and error recovery services are not required. There is no need for opening a connection, maintaining a connection, or terminating a connection. This is because data is continuously sent to the recipient, whether or not they receive it.

**UDP** is mainly used for real-time communications and time-sensitive applications, such as playing videos, gaming, or Domain Name System (**DNS**) lookups. It provides faster data transfer speeds as it does not spend time establishing a firm connection with the destination before sending the data.

**UDP** divides messages into packets, called datagrams. These packets are forwarded by the devices in th

## 9. What are the advantages and disadvantages of UDP?

**Advantages of UDP**

- **UDP** is an alternative to **TCP**.
- It is useful for applications in which we don’t need to put sequences of packets together.
- Helps in reducing transmissions time.
- It is widely used for time-sensitive or real-time communications, such as broadcast or multi-task network transmission.

**Disadvantages of UDP**

- It is a less reliable and connectionless protocol.
- Not ideal for sending an email, viewing a webpage, or downloading a file.
- It does not provide Congestion Control.
- Does not provide packet sequencing or error connection support.
- Data packets are likely to get lost during transmission.

## 10. What is the difference between UDP and TCP?

In **TCP**, when the data is transferred, the receiving end sends a signal that it is ready to receive the data. In this way, nothing is lost along the way. It takes more time but results in more consistent transmissions.

But with **UDP**, the data is forwarded before establishing a firm connection with the receiving end. It can cause the data packets to get lost when data is transferred across the internet. Due to this, hackers also get an opportunity to execute a distributed denial-of-service (**DDoS**) attack.



| Aspect                                       | TCP                                      | UDP                                      |
|----------------------------------------------|------------------------------------------|------------------------------------------|
| Protocol Expansion                          | Transmission Control Protocol (TCP)         | User Datagram Protocol (UDP)             |
| Connection Type                            | Connection-oriented                         | Connectionless                           |
| Connection Establishment                | Requires connection establishment before data transmission | No connection establishment required  |
| Data Units                                 | Packets                                    | Datagrams or Packets                     |
| Data Sequence                             | Data follows a specific sequence            | No guaranteed sequencing                  |
| Data Delivery Guarantee                 | Guarantees data delivery                   | No guaranteed data delivery               |
| Error Checking                            | Extensive error-checking                    | Basic error-checking using checksums    |
| Retransmission of Lost Packets   | Retransmission of lost packets                | No retransmission support                |
| Weight                                      | Heavy-weight                                | Lightweight                              |
| Header Size                                 | 20 bytes                                   | 8 bytes                                  |
| Acknowledgment Segment           | Acknowledgment segment present               | No acknowledgment segment                |
| Handshake                                  | Three-way handshake to establish connection | No handshake                             |
| Speed                                         | Slower than UDP                            | Faster and more efficient                |

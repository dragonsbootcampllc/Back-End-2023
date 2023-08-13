# **OSI model​​**

OSI stands for **Open Systems Interconnection**. It has been developed by ISO – ‘**International Organization for Standardization**‘, in the year 1984. It is a 7-layer architecture with each layer having specific functionality to perform. All these 7 layers work collaboratively to transmit the data from one person to another across the globe.

## Layers of OSI Model

- **Physical Layer**
- **Data Link Layer (DLL)**
- **Network Layer**
- **Transport Layer**
- **Session Layer**
- **Presentation Layer**
- **Application Layer**

## **Layer 1- Physical Layer**

- The lowest layer of the OSI reference model.
- It is responsible for the actual physical connection between the devices and information in the form of **bits.**
- It is responsible for **transmitting individual bits** from one node to the next.
- When receiving data, this layer will get the signal received and convert it into 0s and 1s and send them to the Data Link layer.
- **Bit rate control:** The Physical layer also defines the transmission rate i.e. the number of bits sent per second.
- **Physical topologies:** Physical layer specifies how the different, devices/nodes are arranged in a network i.e. bus, star, or mesh topology.
- **Transmission mode:** Physical layer also defines how the data flows between the two connected devices. The various transmission modes possible are Simplex, half-duplex and full-duplex.
- Hub, Repeater, Modem, and Cables are Physical Layer **devices**.

## **Layer 2- Data Link Layer (DLL)**

- Responsible for the node-to-node delivery of the **message**.
- Encapsulate sender and receiver's MAC address.
- The packet received from Network Layer it divides to frames depends on the frame size of NIC.
- **Error control:** The data link layer provides the mechanism of error control in which it detects and retransmits damaged or lost frames.
- **Flow Control:** The data rate must be constant on both sides else the data may get corrupted thus, flow control coordinates the amount of data that can be sent.

- ### It consists of two sublayers

---

> #### **1. Logical Link Control (LLC):**

- Provides services to the upper-layers.
- Flow-control and multiplexing for the logical link.
- **Note** => Multiplexing allows data streams to share a single communication channel without interference.

> #### **2. Media Access Control (MAC)**

- Control how devices access the medium.
- Host addressing (MAC address).
- Encapsulate and de-encapsulate the frames.
- Back-off Functions => The mechanism used to handle collisions.

### Note

- DLL is handled by the NIC
- Switch & Bridge are Data Link Layer devices.

## **Layer 3- Network Layer**

- Transmission of data from one host to the other in different networks.
- Packet routing i.e. selection of the shortest path to transmit the packet, from the number of routes available.
- The sender & receiver’s IP addresses are placed in the header by the network layer.
- The **PBU** of this layer is the **Packet**.
- Network layer is implemented by networking devices such as routers.

## **Layer 4- Transport Layer**

- Provides services to the Application layer and Network layer.
- The data in the transport layer is referred to as **Segments**.
- Provides the acknowledgment of the successful data transmission and re-transmits the data if an error is found.
- **At the sender’s side:** The transport layer receives the formatted data from the upper layers, performs **Segmentation**, and also implements **Flow & Error control** to ensure proper data transmission. It also adds Source and Destination port numbers in its header and forwards the segmented data to the Network Layer.
- **At the receiver’s side:** Transport Layer reads the port number from its header and forwards the Data which it has received to the respective application. It also performs sequencing and reassembling of the segmented data.

### Services Provided by Transport Layer

1. **Connection-Oriented Service:** In this type of transmission, the receiving device sends an acknowledgment, back to the source after a packet or group of packets is received. This type of transmission is reliable and secure.
2. **Connectionless service:** It is a one-phase process and includes Data Transfer. In this type of transmission, the receiver does not acknowledge receipt of a packet. This approach allows for much faster communication between devices. Connection-oriented service is more reliable than connectionless Service.

- The **PBU** of this layer is the **Segments**.
- Transport layer is operated by the Operating System.
- **Protocol Use :** TCP, UDP.

## **Layer 5- Session Layer**

- Responsible for the establishment of connection, maintenance of sessions, and authentication, and also ensures security.
- **Synchronization:** By adding check-points.
- **Dialog Controller:** The session layer allows two systems to start communication with each other in half-duplex or full-duplex.

## **Layer 6- Presentation Layer**

- The presentation layer is also called the **Translation layer**.
- The data from the application layer is extracted here and manipulated to get to required format to transmit over network.
- **Translation:** For example, ASCII to EBCDIC.
- **Encryption/ Decryption:** Data encryption translates the data into another form or code.
- **Compression:** Reduces the number of bits that need to be transmitted on the network.
- **Protocol Use:** JPEG, GIF.

## **Layer 7- Application Layer**

- At the very top of the OSI Reference Model stack of layers and implemented by the network applications.
- It serves as a window for the application services to access the network and for displaying the received information to the user.
- Example: Application – Browsers.
- **Protocol Use :** SMTP.
- Also called **Desktop Layer**.
- Mail Services : Provide email service
- Network Virtual Terminal: It allows a user to log on to a remote host.

## Final Notes

- The first 3 layers are **Lower Layers or Hardware Layers.**
- The last 3 layers are **Upper Layers or** **Software Layers.**

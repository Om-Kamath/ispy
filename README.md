# iSpy 🕵🏻

A cryptographically encrypted p2p messaging app built for the cyber cypher tech hackathon conducted by Taqneeq in Jan, 2022.

<p>The online world is so easy to use that we often forget how fragile and dangerous it is. There are many problems which spies may face while communicating digitally. Some of the problems are: Lack of privacy, Data leakage and Increased complexity which can be intimidating at times.</p>

<p>iSpy uses cryptographic encryption for enhanced security. It establishes a peer-to-peer connection which increases privacy along with a very simple execution which is compatible on most of the devices.</p>

<h2>How does it work?</h2>
<p>The host will start the application and generate a token. This token should be shared with the person who wants to establish a connection. After entering the correct token, the connection will be established with the receiver. The messages which are sent are first cryptographically encrypted and can be decrypted only using the key which both end-users have. Any person trying to intercept the communication will be unable to read any of the messages as the decryption takes place at the receiver side only.</p>


<h2>Tools used</h2>
<p>iSpy is a simple tool which runs on the command line. It is built using Python. Socket is used to establish the connection between the nodes and fernet is a module from the cryptography package which is used for encryption of the messages.</p>


<h2>Additional features that can be implemented in the future</h2>
<ul>
<li>A GUI would appeal to the masses.</li>
<li>Self-destruct messages would prove to be beneficial in case the spies get abducted.</l>
<li>The integration of ultra-wideband technology would help in faster communication when the spies are in close proximity without any fear of suspicion. This technology is currently being used by Apple in most of their products like iPhones and the newly launched Airtags.</li>
</ul>

<a href="https://youtu.be/bYNaww-03Wk?t=8201">Hackathon Demo</a>

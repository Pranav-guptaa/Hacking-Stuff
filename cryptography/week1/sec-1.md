# INTRODUCTION
# Section -1 
```

Cryptography is everywhere

uses:
	secure communication i.e. web traffic and wireless traffic

	encrypting files on disk

	content protection

	user authentication

Secure Communication:
	achieved by using the protocols called SSL and TLS 

	Goal is to prevent the attacker from eavesdropping and tampering the data shared over internet

Secure Sockets layer/TLS:
	Has two main parts:
		handshake protocol: establishes a secret key using public-key cryptography

		record layer: transmit data using secret key(ensures confidentiality and intergrity)

Symmetric encryption:
	alice and bob share a secret key K only known to them.

	E,D : two cipher algorithms
	E : encryption algorithm 
	D : decryption algorithm

	E takes a message(m) and the key(k) and produces a ciphertext(c)
	D takes a ciphertext and the key and produces back the message

	E,D algorithms are publicly known and only k is kept secret 


Use cases:
	Single use key(one time key):
		key is only used to enrcrypt one message i.e. every message is encrypted using a different
		symmetric key.

	Multi use key(many time key):
		key is used to encrypt multiple messages i.e. same key for many messages

		needs more machinery than for one-time key
	
Things to remeber:
	cryptography is a tremendous tool and basis for many security mechanisms


What is cryptography?
	Consists of two parts: secret key establishment and secure communication 

	Digital signatures and anonymous communication 
	Anonymous digital cash: a digital currency that can be replicated into many coins. i.e. how to
	prevent a user from double spending a coin i.e. using a single coin multiple times and this is 
	considered as a fraud but we have no idea who has done that fraud as their identity is hidden.


```

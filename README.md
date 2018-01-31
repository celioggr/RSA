# RSA
> A simple RSA implementation (GenKey, Cipher &amp;&amp; Decipher)

The following work is a very simple implementation of the RSA algorithm (yet functional use it at your own risk) with the purpose of better understanding the functionalities and applications
associated with it. It was developed only for academic scope and should only be used on it.   


### KeyGen

Will generate a RSA key. You can specify number of bits, otherwise 1024 bit key will be set to default. 
This function returns a tuple (n,p,q,e,d) according to the following primitives.

![RSA](https://i.imgur.com/uaknNgQ.png)


> Kp = {e,n} - Your Public Key


> Ks = {d,n} - Your Private key

### Cipher

Will take a plaintext and cipher it into a single block that will be then sent to the destinary or to the decipher function in order to get back the original message.
At the main function, a random message is generated (you can change this message at your will).
The cipher process turns M (plaintext) into an integer m, such that  **0 ≤ m < n** by using an agreed-upon reversible protocol known as a padding scheme (here represented as 'str'). Then computes the ciphertext C, using a public key e, corresponding to:


![RSA](https://i.imgur.com/sp461c0.png)


### Decipher

It is possible to recover m from c by using the private key exponent d. Given m, the original message M  can be recovered by reversing the padding scheme.


![RSA](https://i.imgur.com/9WZSOvI.png)

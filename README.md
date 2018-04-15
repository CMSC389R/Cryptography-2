# Cryptography-2

## Part 1

You have come across a digital notary who is using MD5 hashing to sign messages. The notary can either generate a signature for you by prepending your message with a random secret, or test a signature against a new message. Each time you request a new signature, he will generate a new secret for your data, but will keep the same secret for every signature test.

Your task is to show the notary that this signature scheme is vulnerable to a hash length extension attack. You have heard that the length of the secret he uses is only 6 bytes (48 bits) long, so you won't need to try and determine this length yourself. Use the stub.py code to help you craft a valid signature on a custom payload. The notary lives on 159.89.236.106:5678. Thus, you may connect to the challenge over nc using: $ nc 159.89.236.106 5678. Make sure to include the hash from which you based your crafted hash, your crafted hash, and the payload sent to the notary.

This part of the assignment proved to be difficult for me, but reading the information described [here](https://blog.skullsecurity.org/2012/everything-you-need-to-know-about-hash-length-extension-attacks) helped me extensively. I began simpy be connecting to the notary using ```nc 159.89.236.106 5678``` and figuring out how it operated, and this allowed me to start the first task of calculating the forged hash. By simply selecting option 1) to sign some data and sending my message ```Hacker4Life``` to the notary I get this hash ```2bd4bd04b19905c57b38a471502439f0```.

# Cryptography-2

## Part 1

My code for this part can be found [here]()!

You have come across a digital notary who is using MD5 hashing to sign messages. The notary can either generate a signature for you by prepending your message with a random secret, or test a signature against a new message. Each time you request a new signature, he will generate a new secret for your data, but will keep the same secret for every signature test.

Your task is to show the notary that this signature scheme is vulnerable to a hash length extension attack. You have heard that the length of the secret he uses is only 6 bytes (48 bits) long, so you won't need to try and determine this length yourself. Use the stub.py code to help you craft a valid signature on a custom payload. The notary lives on 159.89.236.106:5678. Thus, you may connect to the challenge over nc using: $ nc 159.89.236.106 5678. Make sure to include the hash from which you based your crafted hash, your crafted hash, and the payload sent to the notary.

This part of the assignment proved to be difficult for me, but reading the information [here](https://blog.skullsecurity.org/2012/everything-you-need-to-know-about-hash-length-extension-attacks) helped me extensively. I began simply be connecting to the notary using ```nc 159.89.236.106 5678``` and figuring out how it operated, and this allowed me to start the first task of calculating the forged hash. By simply selecting option 1) to sign some data and sending my message ```Hacker4Life``` to the notary I got this hash ```2bd4bd04b19905c57b38a471502439f0```. 

The second task in order to complete this part of the assignment was crafting the payload, which required greater thought than forging the hash. In order to successfuly calculating the padding I took into account that the length of the secret is 6 bytes, and that the length would be stored in 8 bytes, so I add 14 to the length of the message, mod that number by 64 and subtract it from 64 to make sure that the padding is corect: ```pad = 64 - ((len(message)+14) %64)```. I then craft the payload by converting my ```message + malicious``` to hex:
```
encrypt = message + malicious

payload = ""
for c in encrypt:
	payload =  payload + '\\x%02X' % ord(c)
```
Finally I send in my ```test``` and ```payload``` to the notary and am presented with this flag:

```CMSC389R-{merkle_damgard_unguarded}```

[!alt text]()

## Part 2

For this part of the assignment we were to send an encrypted email using a PGP public key provided to ```pgpassignment@gmail.com.```
I tried both using the GPG command line tool and using a web based GPG encryption. First I generated a PGP key using ```gpg --gen-key```, I then imported and encrypted my message, ```I really enjoyed the CTF!```, I used a piece of software called GPG Keychain, shown below to import my secret key and the public key provided and send my encrypted message to ```pgpassignment@gmail.com```. 

[!alt text]()

[!alt text]()

I then recieved a message which contained this flag: 
```CMSC389R-{thanks_f0r_com1ng_t0_UMDCTF}```




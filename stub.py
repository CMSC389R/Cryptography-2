# do `curl http://starship.python.net/~gherman/programs/md5py/md5py.py > md5.py`
# if you do not have it from the git repo
import md5
import socket
import struct

#####################################
### STEP 1: Calculate forged hash ###
#####################################

host = "159.89.236.106"
port = 5678
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


message = 'Hacker4Life'    # original message here

s.recv(1024)
s.send("1\n")
s.recv(1024)
s.send(message+"\n")
data = s.recv(1024)
print(data)

split = data.split("\n")

splitAgain = split[2].split(": ")
legit = splitAgain[1]
malicious = 'ScriptKiddie'

data = s.recv(1024)
print(data)
s.send("2\n")
data = s.recv(1024)
print(data)


# initialize hash object with state of a vulnerable hash
fake_hash = md5.new('A' * 64)
fake_hash.A, fake_hash.B, fake_hash.C, fake_hash.D = md5._bytelist2long(legit.decode('hex'))

  # put your malicious message here

# update legit hash with malicious message
fake_hash.update(malicious)

# test is the correct hash for md5(secret + message + padding + malicious)
test = fake_hash.hexdigest()



#############################
### STEP 2: Craft payload ###
#############################

# TODO: calculate proper padding based on secret + message
# secret is 6 bytes long (48 bits)
# each block in MD5 is 512 bits long
# secret + message is followed by bit 1 then bit 0's (i.e. \x80\x00\x00...)
# after the 0's is a bye with message length in bits, little endian style
# (i.e. 20 char msg = 160 bits = 0xa0 = '\xa0\x00\x00\x00\x00\x00\x00\x00\x00')
# craft padding to align the block as MD5 would do it
# (i.e. len(secret + message + padding) = 64 bytes = 512 bits

pad = 64 - ((len(message)+14) %64)
bits = 8 * (len(message)+6)

message += '\x80' + '\000' * (pad - 1)
message += struct.pack('<q', bits)


encrypt = message + malicious

payload = ""
for c in encrypt:
	payload =  payload + '\\x%02X' % ord(c)



# send `test` and `payload` to server (manually or with sockets)
# REMEMBER: every time you sign new data, you will regenerate a new secret!

s.send(test+"\n")
data = s.recv(1024)
print(data)
s.send(payload+"\n")

data = s.recv(1024)
data = s.recv(1024)

print(data)

s.close()

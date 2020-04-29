import secrets

#Generate a secure string with secret modules :
print(f"Secure string byte: -{secrets.token_bytes(32)}")

#hex string 
print(f"Secure sting : {secrets.token_hex(32)}")

#specific number of string 
print(f"8 Secure sting : {secrets.token_hex(32)[0:8]}") 
print(f"10 Secure sting : {secrets.token_hex(32)[0:10]}")
print(f"15 Secure sting : {secrets.token_hex(32)[0:15]}")
import secrets 

#Secure token for 
#OTP
#registration confirmation token
#session keys
#Password changing user token 

#You can create token as many bytes you want 
#32 bytes (256 bits) of randomness is sufficient to secure and hard to guess 

#32 bytes
print(f"URL : https://adobil.com/user/ashik001/reset={secrets.token_urlsafe(32)}")


#64 bytes
print(f"URL : https://adobil.com/user/ashik001/reset={secrets.token_urlsafe(64)}")

#96 bytes
print(f"URL : https://adobil.com/user/ashik001/reset={secrets.token_urlsafe(96)}")

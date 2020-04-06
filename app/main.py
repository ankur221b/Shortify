import sys 
import hashlib

base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def to_base62(num, b = 62):
    
    if b <= 0 or b > 62:
        return 0
    
    rem = num % b
    res = base[rem];
    q = num // b
    while q:
        
        rem = q % b
        q = q // b
        res = base[int(rem)] + res

    return res

def to_base10(num, b = 62):

    limit = len(num)
    res = 0
    for i in range(limit):
        res = b * res + base.find(num[i])
    return res

def shorten(long_URL):
	md5_value = hashlib.md5(long_URL.encode())
	hex_value = str(md5_value.hexdigest())
	dec_value = int(hex_value,16)
	base62_value = to_base62(dec_value)
	short_URL = base62_value[:7]

	return short_URL
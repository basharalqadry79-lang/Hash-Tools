import hashlib
import colorama
from hashlib import *
colorama.init(autoreset=True)
style = '\033[31m' + r'''
  _    _           _       _______          _     
 | |  | |         | |     |__   __|        | |    
 | |__| | __ _ ___| |__      | | ___   ___ | |___ 
 |  __  |/ _` / __| '_ \     | |/ _ \ / _ \| / __|  @Bashar Pythhub 2026
 | |  | | (_| \__ \ | | |    | | (_) | (_) | \__ \  -Hashing Tools 
 |_|  |_|\__,_|___/_| |_|    |_|\___/ \___/|_|___/            
                                       
''' + '\033[0m'
print(style)
print("===============================================")
print("\033[33m1]-Hash Checker\n2]-Hash length\n3]-Hash type")
print("\033[33m4]-MD5 Encrypt\n5]-MD5 Decrypt \033[37m")
print("===============================================")

choose = input ("Please choose option : ")
if choose == '1':
	print("This Option For Hash Chacker")
	hash1 = input("Enter hash [1] :")
	hash2 = input("Enter hash [2] :")
	if hash1 == hash2 :
	        print("the hash is clean")
	else:
         	print("the hash is virus ")
if choose == '2':
	print("This option For length hash")
	length = input("Enter your Hash : ")
	print("Length Hash is : ", len(length))
	
if choose == '3' :
	print("This Option For Know Hash Type")
	hash = input("Enter the hash : ")
	length = len(hash)
	if length == 32 :
		print("The Hash is [MD5]")
	if length == 40 :
		print("The Hash is [SHA1]")
	if length == 64 :
		print("The Hash is [SHA256]")
if choose == '4' :
	print("This Option For Text to MD5 :")
	word = input("Enter Your Text : ")
	md5 = hashlib.md5(word.encode())
	print(md5.hexdigest())
if  choose == '5' :
	print("This Option For Decryption :")
	hash = input("Enter Your Hash : ")
	file = input("Write file name : ")
	with open(file , mode='r') as f :
		for line in f :
			line = line.strip()
			if md5(line.encode()).hexdigest() == hash :
				print("[-] Password Found :" +line)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
         
         

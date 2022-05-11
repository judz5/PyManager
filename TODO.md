## Gen plan
  - Terminal interface
  - use master key for encryption/decryption
  - allow searching of website and use that to find pw
  - Auto copy to clipboard

## How

  - Master pw is inputted by user at config start
  - a device secret password is auto gen
  - both are put in file
  - master pw + device pw = master key
  - use master key to encrypt/decrypt entries
  - * is encrypt
  - email(*), username(*), password(*), sitename, url

### Add

  - ask for master pw
  - validate the master pw (Combine with system key = master key)
  - validate by hashing and comparing or sum
  - input fields: sitename, url, email(*), username(*), password(*)
  - encrypt what need to be encrypted with masterkey

### GET

  - input site name
  - display all that match search, hide pw by default
  - if user uses flag to show pw show pw
  - ask for master PW
  - verifiy master PW
  - make master key
  - decrypt the pw with master key and copy to clipboard



SALT SHOULD BE STORED WITH HASH

EX: ThisIsSalt:12089ffjq921023jfa


on config start, make user input masterpw (confirm 2x)
hash and store in sql or file (salt)

ask user for masterPW at start
hash and compare to stored masterpw hash 

if right then allow access

then take that masterpw they inputed, adds salt
puts through PBKDF2 To make the key

encyption : 

take key and plaintext (add IV to plaintext)

use key to encrypt plaintext+IV(1fkljslj:password) through AES 

save to sql as (IV:PasswordHash)



Decrpyt : 

use key generate method to get key

get the cipher and IV from sql 

pass key and cipher and iv through AES decryption (boom)




on config user sets a master password, we then salt this master password and save the salt 

next time the user enters they enter the master password and we again salt it with the saved salt, and use as our key
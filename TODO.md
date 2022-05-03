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


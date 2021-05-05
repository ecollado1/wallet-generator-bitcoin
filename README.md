# wallet-generator-bitcoin
Open Source Python Scripts Bitcoin Wallet Generator (WIF, P2WPKH, P2WSH, Encrypted Key Private BIP0038)

### PREREQUISITES FOR RUN 

You'll need git, a Python3 (or later). We'll assume Ubuntu 18.04 LTS (Bionic Beaver) for the package installs, which comes with Python 3 out of the box.
  
* __import and install the following libraries__: 
  * __pip install graphenebase__
  * __pip install pyqrcode__
  * __pip install ecdsa__
  * __pip install hashlib__
  * __pip install binascii__
  * __pip install base58__
  * __pip install base64__
  * __pip install ecdsa __
  * __pip install codecs__

### RUN

* __To run the program simply type the following in your terminal__:

   #### python3 WalletGeneratorBitcoin.py


* __will have an output something like this.. and also the qr code images__:

* __ECDSA Public Key__:  0436679dfa9be4503e6179cc76d4f86e7c195ec7e378eae8d6d64041af607f993414947b62b27a3bacd40440bf6532759c67aee6b1314be7fac387f3e7e787f6a9
* __SHA256(ECDSA Public Key)__:  f49f09d1129a4aa1de25799a788924115d80fcee241815540ade5b83e7636976
* __RIDEMP160(SHA256(ECDSA Public Key))__:  d9560c01a59cb933a539657c3fa968710d538c7f
* __Prepend Network Byte to RIDEMP160(SHA256(ECDSA Public Key))__:  00d9560c01a59cb933a539657c3fa968710d538c7f
	* __|___>SHA256 # 1 __:  6b93a96a70115e062027581abb7cba142330447e74036bf84b6216fba4c5ee8f
	* __|___>SHA256 # 2__:  94938aa309acfc761a2c25f248ff509f9d19dc90498e6b83730dcab868d19503
* __Checksum(first 4 bytes)__:  94938aa3
* __Append Checksum to RIDEMP160(SHA256(ECDSA Public Key))__:  00d9560c01a59cb933a539657c3fa968710d538c7f94938aa3

* __Colocar Password Llave Privada__: Hola Mundo

* __DIRECCION PUBLICA 1__:  1LpAiGhR698gu9vM1utKbvVnTjHk8pxe8r

LLAVE PRIVADA HEX:  b9d60cd49ac63b8c36a73f6a553f5c1a439ca445c7ebb68f7d8c62d64172f7cf
LLAVE PRIVADA WIF Encrypted Key (BIP0038) CON CONTRASEÑÁ:   6PRReBanKBh1tJ6fSoRYtTBenCRz9zFFXtsaWwSH7NMs1Ut9YyruJ7y9DC
LLAVE PRIVADA WIF:   5KE8WtTxMybymNJgG2D15yk1eyBYZi16NaerB1CdHLmtzvKVGKi
LLAVE PRIVADA WIF COMPRESS:  L3SxAv9yMaqPYq32HJKyNySqtayYKMyQiFY439tK98HAWEMZyA1P

VERIFICANDO DIRECCION SI ES VALIDA
Hash# 1  :  6b93a96a70115e062027581abb7cba142330447e74036bf84b6216fba4c5ee8f
Hash# 2  :  94938aa309acfc761a2c25f248ff509f9d19dc90498e6b83730dcab868d19503
[VERDADERO] checksum es valido!

COMPARANDO SI LAS LLAVES SON GENERADAS CORRECTAMENTE
CON LA LIBRERIA BITCOINADDRESS

DIRECCION PUBLICA 1:  1LpAiGhR698gu9vM1utKbvVnTjHk8pxe8r
DIRECCION PUBLICA Compress:  18rXYohfcJHqZ1VeVjhSMybHuuEXwA3Zt6
DIRECCION PUBLICA 3:  3LqjyGU6iDX65AVsTNnfeG9vJtmNCT1V4k
DDIRECCION PUBLICA bc1 P2WPKH:  bc1q2cnvxkklrjyrjqm3hjgqmfzy9w8whmkgq2yzwj
DIRECCION PUBLICA bc1 P2WSH:  bc1qf072navk0gmkz2qhr6j0f2j5x9xwjeehfuvrf5ghgvew8slrelys58p3qm

LLAVE PRIVADA HEX:  b9d60cd49ac63b8c36a73f6a553f5c1a439ca445c7ebb68f7d8c62d64172f7cf
LLAVE PRIVADA WIF:  5KE8WtTxMybymNJgG2D15yk1eyBYZi16NaerB1CdHLmtzvKVGKi
LLAVE PRIVADA WIFC:  L3SxAv9yMaqPYq32HJKyNySqtayYKMyQiFY439tK98HAWEMZyA1P



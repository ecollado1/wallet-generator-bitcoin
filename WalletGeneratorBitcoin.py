#!/usr/bin/env python3

### program python generate address public and key private for wallet bitcoin
### Edwin Collado.
### 04/may/2021

import hashlib
import binascii
import base58
import base64
import ecdsa 
import codecs

##para generar el codigo QR y manejos de las imagenes logos
from PIL import Image
from PIL import ImageDraw
import json
import pyqrcode


##para encriptar con password la llave primaria
from graphenebase import PrivateKey
from graphenebase.bip38 import encrypt


def generarcodigoqr(cadena,nombre_archivo,texto_cadena):

	import os

	codigoqr = pyqrcode.create(cadena)
	codigoqr.eps(nombre_archivo, scale=8)

	img = Image.open(nombre_archivo)
	img = img.convert("RGBA")

	logo = Image.open('bitcoin.jpg')
	logo.thumbnail((100, 100))
	logo_pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)

	img.paste(logo, logo_pos)

	draw = ImageDraw.Draw(img)
	draw.text((33,5),nombre_archivo , (0,0,0))
	draw.text((33,16),texto_cadena, (0,0,0))

	img.paste(logo, logo_pos)
	img.save("tmp.png")

	im = Image.open("tmp.png")
	fig = im.convert('RGB')
	fig.save(nombre_archivo, lossless = True)

	os.remove("tmp.png")

ecdsaPrivateKey = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)

###GENERAR LLAVE PUBLICA
ecdsaPublicKey = '04' +  ecdsaPrivateKey.get_verifying_key().to_string().hex()
print("ECDSA Public Key: ", ecdsaPublicKey)
hash256FromECDSAPublicKey = hashlib.sha256(binascii.unhexlify(ecdsaPublicKey)).hexdigest()
print("SHA256(ECDSA Public Key): ", hash256FromECDSAPublicKey)
ridemp160FromHash256 = hashlib.new('ripemd160', binascii.unhexlify(hash256FromECDSAPublicKey))
print("RIDEMP160(SHA256(ECDSA Public Key)): ", ridemp160FromHash256.hexdigest())
prependNetworkByte = '00' + ridemp160FromHash256.hexdigest()
print("Prepend Network Byte to RIDEMP160(SHA256(ECDSA Public Key)): ", prependNetworkByte)
hash = prependNetworkByte
for x in range(1,3):
    hash = hashlib.sha256(binascii.unhexlify(hash)).hexdigest()
    print("\t|___>SHA256 #", x, " : ", hash)
cheksum = hash[:8]
print("Checksum(first 4 bytes): ", cheksum)
appendChecksum = prependNetworkByte + cheksum
print("Append Checksum to RIDEMP160(SHA256(ECDSA Public Key)): ", appendChecksum)
bitcoinAddress = base58.b58encode(binascii.unhexlify(appendChecksum))

###CONVERTIR EL PRIVATE KEY WALLET IMPORT FORMAT WIF
private_key_hex = '80' + ecdsaPrivateKey.to_string().hex()
first_sha256 = hashlib.sha256(binascii.unhexlify(private_key_hex)).hexdigest()
second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()
final_key = private_key_hex+second_sha256[:8]
WIF = base58.b58encode(binascii.unhexlify(final_key))

###CONVERTIR EL PRIVATE KEY WALLET IMPORT FORMAT WIFC
private_key_hexc = '80' + ecdsaPrivateKey.to_string().hex()+'01'
first_sha256 = hashlib.sha256(binascii.unhexlify(private_key_hexc)).hexdigest()
second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()
final_key = private_key_hexc+second_sha256[:8]
WIFC = base58.b58encode(binascii.unhexlify(final_key))


##http://docs.pygraphenelib.com/en/latest/bip38.html
##https://github.com/xeroc/python-graphenelib
###COLOCAR A LA LLAVE PRIVADA WIF UNA CONTRASENA O PASSWORD BIP0038
print()
password = input("Colocar Password Llave Privada: ")
print()
WIFPASS = format(encrypt(PrivateKey(WIF.decode('utf-8')),password), "encwif")

print("--------------------------------------------------------------")
print("DIRECCION PUBLICA 1: ", bitcoinAddress.decode('utf8'))
print()
print("LLAVE PRIVADA HEX: ", ecdsaPrivateKey.to_string().hex())
print("LLAVE PRIVADA WIF Encrypted Key (BIP0038) CON CONTRASEÑÁ:  ", WIFPASS)
print("LLAVE PRIVADA WIF:  ", WIF.decode('utf-8'))
print("LLAVE PRIVADA WIF COMPRESS: ", WIFC.decode('utf-8'))

print("--------------------------------------------------------------")

generarcodigoqr(WIF,"PrivateAddress.eps",WIF)
generarcodigoqr(WIFPASS,"PrivateAddressPassword.eps",WIFPASS)
generarcodigoqr(bitcoinAddress.decode('utf-8'),"PublicAddress.eps",bitcoinAddress.decode('utf-8'))

print()
print("------------VERIFICANDO DIRECCION SI ES VALIDA----------------")
base58Decoder = base58.b58decode(bitcoinAddress.decode('utf-8')).hex()
prefixAndHash = base58Decoder[:len(base58Decoder)-8]
checksum = base58Decoder[len(base58Decoder)-8:]
hash = prefixAndHash
for x in range(1,3):
    hash = hashlib.sha256(binascii.unhexlify(hash)).hexdigest()
    print("Hash#", x, " : ", hash)
print("--------------------------------------")
if(checksum == hash[:8]):
    print("[VERDADERO] checksum es valido!")
else:
    print("[FALSO] checksum no es valido!")
print("--------------------------------------")


print()
print('-----------------------------------------------------------------------------')
print('-----COMPARANDO SI LAS LLAVES SON GENERADAS CORRECTAMENTE--------------------')
print('-------------- CON LA LIBRERIA BITCOINADDRESS--------------------------------')
from bitcoinaddress import Wallet
wallet = Wallet(WIF.decode('utf-8'))
print()
print("DIRECCION PUBLICA 1: ",wallet.address.__dict__['mainnet'].__dict__['pubaddr1'])
print("DIRECCION PUBLICA Compress: ",wallet.address.__dict__['mainnet'].__dict__['pubaddr1c'])
print("DIRECCION PUBLICA 3: ",wallet.address.__dict__['mainnet'].__dict__['pubaddr3'])
print("DDIRECCION PUBLICA bc1 P2WPKH: ",wallet.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'])
print("DIRECCION PUBLICA bc1 P2WSH: ",wallet.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'])
print()
print("LLAVE PRIVADA HEX: ",wallet.key.__dict__['hex'])
print("LLAVE PRIVADA WIF: ",wallet.key.__dict__['mainnet'].__dict__['wif'])
print("LLAVE PRIVADA WIFC: ",wallet.key.__dict__['mainnet'].__dict__['wifc'])

generarcodigoqr(wallet.address.__dict__['mainnet'].__dict__['pubaddr1'],"PublicAddress1.eps",wallet.address.__dict__['mainnet'].__dict__['pubaddr1'])
generarcodigoqr(wallet.address.__dict__['mainnet'].__dict__['pubaddr1c'],"PublicAddressC.eps",wallet.address.__dict__['mainnet'].__dict__['pubaddr1c'])
generarcodigoqr(wallet.address.__dict__['mainnet'].__dict__['pubaddr3'],"PublicAddress3.eps",wallet.address.__dict__['mainnet'].__dict__['pubaddr3'])
generarcodigoqr(wallet.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'],"PublicAddressBC1-P2WSH.eps",wallet.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'])
generarcodigoqr(wallet.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'],"PublicAddressBC1-P2WPKH.eps",wallet.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'])

generarcodigoqr(wallet.key.__dict__['hex'],"hex.eps",wallet.key.__dict__['hex'])
generarcodigoqr(wallet.key.__dict__['mainnet'].__dict__['wif'],"wif.eps",wallet.key.__dict__['mainnet'].__dict__['wif'])
generarcodigoqr(wallet.key.__dict__['mainnet'].__dict__['wifc'],"wifc.eps",wallet.key.__dict__['mainnet'].__dict__['wifc'])

print()

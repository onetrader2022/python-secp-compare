from fastecdsa.curve import secp256k1
from fastecdsa.point import Point
from fastecdsa import keys, curve
import random

N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
def c2ux(point):

 p_hex = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F'
 p = int(p_hex, 16)
 compressed_key_hex = point
 x_hex = compressed_key_hex[2:66]
 x = int(x_hex, 16)
 prefix = compressed_key_hex[0:2]

 y_square = (pow(x, 3, p)  + 7) % p
 y_square_square_root = pow(y_square, (p+1) * pow(4, p - 2, p) % p , p)
 if (prefix == "02" and y_square_square_root & 1) or (prefix == "03" and not y_square_square_root & 1):
     y = (-y_square_square_root) % p
 else:
     y = y_square_square_root

 return x_hex

def c2uy(point):

 p_hex = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F'
 p = int(p_hex, 16)
 compressed_key_hex = point
 x_hex = compressed_key_hex[2:66]
 x = int(x_hex, 16)
 prefix = compressed_key_hex[0:2]

 y_square = (pow(x, 3, p)  + 7) % p
 y_square_square_root = pow(y_square, (p+1) * pow(4, p - 2, p) % p , p)
 if (prefix == "02" and y_square_square_root & 1) or (prefix == "03" and not y_square_square_root & 1):
     y = (-y_square_square_root) % p
 else:
     y = y_square_square_root

 computed_y_hex = format(y, '064x')


 return computed_y_hex


def cpub(x,y):
 prefix = '02' if y % 2 == 0 else '03'
 c = prefix+ hex(x)[2:].zfill(64)
 return c


with open("B.txt","r") as m:
  add = m.read().split()
  add1= str(set(add))

with open("A.txt") as f:
  for line in f:
    line=line.strip()

    xs = int(c2ux(line),16)
    ys = int(c2uy(line),16)
    S = Point(xs, ys, curve=secp256k1)

    xsorg = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
    ysorg = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
    Sorg = Point(xsorg, ysorg, curve=secp256k1)
    while True:
      S = S-Sorg
      xs=S.x
      ys=S.y
      pub04=cpub(xs,ys)
      if pub04 in add1:
        print (pub04,file=open("Result1.txt", "a"))
        break


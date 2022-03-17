#--------------------------------------------------------
n = 0x72bae3105c52d6ca470aa6d21b1a8a9f2208951ca6cd71d1b484e38095e0558b32d9db2f926771dc4a93b6deebaf64d2978f0f4efc8f49db5571959e214c900a4bed54fa235ee72cec66c85bca819ea3fb1b4e3dd70e940d9067eb3d0a6a4abf6c152d7d1a19d0833532048ec84754c95eb8055b7e3817e65aea897e3e2a29764af08589a6271721c863df2386ceb9eea4f208ed8f45f0628d5ec3afcc416ab3dda4071a9fca2166e87f14a9475b1711a0b4ccdefab041a7e2a7b418155aed4a1bbc343a0c1a8d9af479ff7e62765bfb5f1762aa66c4b06ce44b5681977e027428b32811c8c539f0c631178ed60a863176cdd1fd73ee9cbe14eaa5e7010443cd
#--------------------------------------------------------

from Crypto.Util.number import long_to_bytes
from gmpy2 import gcd

factorial = 1
for i in range(1, 100000):
    factorial *= i
 
p = gcd(pow(2, factorial, n) - 1, n)
q = n//p

print(p, q)

# p = 99755582215898641407852705728849845011216465185285211890507480631690828127706976150193361900607547572612649004926900810814622928574610545242732025536653312012118816651110903126840980322976744546241025457578454651121668690556783678825279039346489911822502647155696586387159134782652895389723477462451243655239
# q = 145188107204395996941237224511021728827449781357154531339825069878361330960402058326626961666006203200118414609080899168979077514608109257635499315648089844975963420428126473405468291778331429276352521506412236447510500004803301358005971579603665229996826267172950505836678077264366200199161972745420872759627
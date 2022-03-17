n = 0x72bae3105c52d6ca470aa6d21b1a8a9f2208951ca6cd71d1b484e38095e0558b32d9db2f926771dc4a93b6deebaf64d2978f0f4efc8f49db5571959e214c900a4bed54fa235ee72cec66c85bca819ea3fb1b4e3dd70e940d9067eb3d0a6a4abf6c152d7d1a19d0833532048ec84754c95eb8055b7e3817e65aea897e3e2a29764af08589a6271721c863df2386ceb9eea4f208ed8f45f0628d5ec3afcc416ab3dda4071a9fca2166e87f14a9475b1711a0b4ccdefab041a7e2a7b418155aed4a1bbc343a0c1a8d9af479ff7e62765bfb5f1762aa66c4b06ce44b5681977e027428b32811c8c539f0c631178ed60a863176cdd1fd73ee9cbe14eaa5e7010443cd
c = 0x4790c71b682f70a3e8aeaeb62b7b5c7381b27ab013d806631efd826da0bfc4ea7f343ad33ea0abdd14762acf5fcdf02b3e44646b8df7b09345ec2c43614a15e4e38bda58bf0b08f643e521d04f4d1eb06a4521351533b4140df785f12fa085db1e14dba803f00a25208167b359045d4491a49463f2423894dc69d92fc814229bf3d439b0d552732363af89605fc5bc035612b68c49d01c5ec185028d3d036332f6d5d7bccc1e65c7fe13aefb3c8a4ebeb8006092cb714b9040ec3147c0ec784cb6e6cae2456999afdc8fcacd3f3d2502d29b59be9f47e5ff192512ff6a37cf12837f3da1a1905de2d5a4ae7eea353c1b0c15c764bb10a45a21cdb84c3bf948ef
g = 3

from gmpy2 import *
from Crypto.Util.number import *


p = 99755582215898641407852705728849845011216465185285211890507480631690828127706976150193361900607547572612649004926900810814622928574610545242732025536653312012118816651110903126840980322976744546241025457578454651121668690556783678825279039346489911822502647155696586387159134782652895389723477462451243655239
q = 145188107204395996941237224511021728827449781357154531339825069878361330960402058326626961666006203200118414609080899168979077514608109257635499315648089844975963420428126473405468291778331429276352521506412236447510500004803301358005971579603665229996826267172950505836678077264366200199161972745420872759627

q_phi_factor = [2, 35227, 44617, 66343, 67559, 67651, 67759, 67801, 68239, 71633, 73421, 74159, 74821, 77347, 78977, 79813, 82129, 82301, 82787, 84047, 87181, 87959, 88117, 88241, 89137, 89203, 90583, 91873, 92623, 93557, 93601, 94253, 94649, 95369, 97813, 97849, 98017, 99431, 100459, 101377, 101929, 103217, 103549, 106591, 106979, 111697, 112061, 112253, 112397, 114013, 116107, 116881, 117617, 118739, 119159, 119503, 120847, 121843, 121909, 124471, 126127, 126241, 130729]
p_phi_factor = [2, 20611, 30971, 32987, 33107, 33151, 33289, 33457, 33679, 34123, 34897, 35023, 35671, 36151, 37049, 37139, 39313, 39541, 40087, 40237, 40787, 41257, 41333, 41351, 41999, 42083, 42239, 43177, 43627, 44789, 45179, 46381, 46619, 46861, 47111, 48883, 49157, 50359, 50527, 50773, 50777, 50857, 50951, 51307, 51361, 51383, 51593, 52889, 52967, 53047, 54037, 54673, 56479, 56569, 57301, 58963, 59651, 61027, 61441, 61507, 62347, 62929, 62969, 63587, 64171, 64621, 65497]
phi_factor = [4, 20611, 30971, 32987, 33107, 33151, 33289, 33457, 33679, 34123, 34897, 35023, 35227, 35671, 36151, 37049, 37139, 39313, 39541, 40087, 40237, 40787, 41257, 41333, 41351, 41999, 42083, 42239, 43177, 43627, 44617, 44789, 45179, 46381, 46619, 46861, 47111, 48883, 49157, 50359, 50527, 50773, 50777, 50857, 50951, 51307, 51361, 51383, 51593, 52889, 52967, 53047, 54037, 54673, 56479, 56569, 57301, 58963, 59651, 61027, 61441, 61507, 62347, 62929, 62969, 63587, 64171, 64621, 65497, 66343, 67559, 67651, 67759, 67801, 68239, 71633, 73421, 74159, 74821, 77347, 78977, 79813, 82129, 82301, 82787, 84047, 87181, 87959, 88117, 88241, 89137, 89203, 90583, 91873, 92623, 93557, 93601, 94253, 94649, 95369, 97813, 97849, 98017, 99431, 100459, 101377, 101929, 103217, 103549, 106591, 106979, 111697, 112061, 112253, 112397, 114013, 116107, 116881, 117617, 118739, 119159, 119503, 120847, 121843, 121909, 124471, 126127, 126241, 130729]

def orders_subgroup(c, g, p, factor):
    lst = []
    for x in factor:
        C, G = pow(c, (p - 1)//x, p), pow(g, (p - 1)//x, p)
        for i in range(x):
            if pow(G, i, p) == C:
                lst.append(i)
                break
    return lst

def order(g, n, n_phi_Euler_factor, n_phi_Euler):
    for q in n_phi_Euler_factor[::-1]:
        Ord = n_phi_Euler//q
        if pow(g, Ord, n) == 1:
            return Ord
    return n_phi_Euler

ord_g = order(g, n, phi_factor, (p - 1) * (q - 1))
rm_p = orders_subgroup(c, g, p, p_phi_factor)
rm_q = orders_subgroup(c, g, q, q_phi_factor) 

print(ord_g)
print(rm_p)
print(rm_q)

# ord_g = 3620831041249707681837526614894534070355285598225483947704567590841907012699590416231948016710515187458091091333255758171595595641033083736309400409643928552525615771016574204069905126628091574921138579736452244193978524346401965227602432958121312546484970793941595446729171796239738120972142110982378127424943566648943536407620764596225821813291776832376735113844664973843090883837692356157669303472000289784070105578708851239130329196576851269845975332237349620983071050002827602934735173409535571381136533487551597603554084684495113710973324043031393001050506093082012789172941748667129519131950799991435097455247
# rm_p = [0, 1193, 28278, 449, 30649, 6107, 1953, 21417, 33221, 22543, 16897, 30422, 16738, 8172, 22165, 8002, 33430, 7697, 9296, 7347, 33935, 39184, 23472, 1021, 33227, 23065, 30542, 7298, 5730, 1306, 27904, 9555, 15917, 15406, 15638, 30716, 37933, 599, 13899, 12219, 6372, 30551, 24256, 47377, 7871, 41570, 29051, 41068, 42298, 22657, 41081, 28247, 55477, 35190, 17888, 53950, 56355, 22988, 37969, 16905, 38629, 30739, 56640, 31227, 9154, 60834, 23959]
# rm_q = [0, 1521, 23650, 12431, 18674, 36790, 7645, 60811, 45928, 58318, 64676, 4201, 12452, 7577, 47830, 33608, 65544, 35581, 28185, 65083, 82557, 55719, 79820, 44539, 61391, 26232, 63681, 83630, 62585, 10051, 77893, 52166, 29109, 28097, 83163, 54465, 85217, 65728, 62858, 65506, 48052, 77843, 8516, 35562, 78469, 4390, 28876, 92302, 97802, 112883, 76279, 21858, 43706, 106022, 26734, 64146, 89424, 19235, 94567, 113741, 12190, 20074, 86533] 
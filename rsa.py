import itertools

def findModReverse(e, r):
    # 这里直接用模逆元定义的概念，for循环找出b
    # 也可以用扩展欧几里得算法或者欧拉定理计算出来
    for b in itertools.count(1):
        if (e * b) % r == 1:
            return b
            
def getNewKey(p, q, e=11):
    # e的定义是比r小和r互质的的正整数
    # 【注意】: 这里取3是方便计算演示，一般使用65537
    N = p * q
    r = (p - 1) * (q - 1)
    d = findModReverse(e, r)
    return N, e, d
    
def rsa(N, key, message):
    # 加密和解密本质上都是求指数和模的过程，所以可用参数不同的同一个函数
    # 这也是为什么公私钥可以互换，但是不建议（原因是公钥出于种种原因一般都很短）
    me = message ** key
    return me % N
    
   
# 取两个质数
p = 7
q = 13

# 获取公私钥
(N, e, d) = getNewKey(p, q)

print('公钥为：（%d, %d)' % (N, e))
print('私钥为：（%d, %d)' % (N, d))

message = 16

# 加密
c = rsa(N, e, message)

# 解密
m = rsa(N, d, c)

print('原始消息：%d' % message)
print('加密后的值：%d' % c)
print('解密后的值：%d' % m)


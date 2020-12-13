import random

lis = 'jakljpodifsphqhwdjpdahfpda;hfygpp843iweogfrywpqud;fw'

passlen = 6
passwd = "".join(random.sample(lis, passlen))
print(passwd)
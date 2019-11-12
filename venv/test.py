#小明是家手机点老板，店里有如下手机
a=[{'name':'iphone XR','signal':'4G','stock':50,'price':9999},{'name':'iphone 8','signal':'4G','stock':40,'price':4499},{'name':'小米A','signal':'5G','stock':67,'price':5499},{'name':'小米B','signal':'4G','stock':87,'price':2499},{'name':'华为A','signal':'5G','stock':77,'price':6499},{'name':'华为B','signal':'4G','stock':97,'price':4499}]
#天猫为鼓励商家，凡是超过5000补贴一百 低于5000补贴50，国家为了鼓励国产手机，4G每部补贴20，5G补贴50，由于小明宣传到位，所有手机售空，请计算小明最后收益


def mon_1(item):
    i = 0
    for mobile in item:
        if mobile['price'] > 5000:
            i+=100+mobile['price']
        elif mobile['price'] < 5000:
            i=i+50+mobile['price']
    return i
def mon_2(item):
    m = 0
    for mobile in item:
        if mobile['name'] in ('小米A','华为A','华为B'):
            if mobile['signal'] == '4G':
                m+=20
            elif mobile['signal'] == '5G':
                m+=50
        else:
            pass
    return m

print (mon_1(a)+mon_2(a))





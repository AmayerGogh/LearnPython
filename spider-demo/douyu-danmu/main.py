import time, sys
from danmu import DanMuClient
'''
文档
http://danmu.readthedocs.io/zh_CN/latest/
'''

def pp(msg):
    print(msg.encode(sys.stdin.encoding, 'ignore').
        decode(sys.stdin.encoding))

dmc = DanMuClient('https://www.douyu.com/276685')
if not dmc.isValid(): print('Url not valid')

@dmc.danmu
def danmu_fn(msg):
    # nick =msg['NickName']
    # content =msg['Content']
    # if nick.len
    pp('[%s] %s' % (msg['NickName'].ljust(15,'一'), msg['Content']))
    

# @dmc.gift
# def gift_fn(msg):
#     pp('[%s] sent a gift!' % msg['NickName'])

# @dmc.other
# def other_fn(msg):
#     pp('Other message received')

dmc.start(blockThread = True)
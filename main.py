from event_src.audit.parse_log2eventMap.log2event import log2event
import threading


def filter_prov():
    return

def start():
    # 创建sentlog2buffer线程用来收集，解析日志数据，传输到buffer中
    # filter_thread用来接受 传来的节点与边，进行溯源图简约
    # 要注意buffer要具有多线程访问不冲突的特征
    sentlog2buffer_thread = threading.Thread(target=log2event)
    filter_thread = threading.Thread(target=filter_prov)
    sentlog2buffer_thread.start()
    filter_thread.start()


if __name__=="__main__":
    start()


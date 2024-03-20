import copy
import subprocess

from event_src.audit.event_process.transform2prov import transform2prov
from event_src.audit.parse_log2eventMap.event_parse import event_parse
from event_src.audit.parse_log2eventMap.record_parse import parse_record2common_parttern

def log2event():
    command = ['/home/zzl/Desktop/log_parse/auparse']
    process = subprocess.Popen(command, stdout=subprocess.PIPE ,encoding="utf-8", bufsize=512)
    print(process.pid)
    try:
        cur_event_id=None
        cur_event_record=[]
        # 持续读取子进程的输出数据
        while True:
            line = process.stdout.readline()
            if line == '' and process.poll() is not None:
                break
            if line:
                # 解析一个事件到 Record对象中
                cur_record=parse_record2common_parttern(line)
                # 解析record数据,
                if cur_event_id==None:  #first record
                    cur_event_id=cur_record.event_id
                    cur_event_record.append(cur_record)
                    continue
                if cur_event_id==cur_record.event_id:
                    cur_event_record.append(cur_record)
                    continue
                if cur_event_id!=cur_record.event_id:
                    cur_event_id=cur_record.event_id
                    event_need2parse=copy.copy(cur_event_record)
                    cur_event_record.clear()
                    cur_event_record.append(cur_record)
                    transform2prov(event_parse(event_need2parse))


    except:
        print(cur_event_id,"事件解析，log2event,事件解析出错\n")
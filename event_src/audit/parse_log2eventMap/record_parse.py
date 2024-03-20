import re


class Record:
    def __init__(self,type,time,event_id,data):
        self.type=type
        self.time=time
        self.event_id=event_id
        self.data=data

    def get_record_inf(self):
        return "AuditRecord [id=" + self.event_id + ", time=" + self.time + ", type=" + self.type + ", data=" + self.data + "]"


#将所有记录解析为 type,time,event_id,data的形式
def parse_record2common_parttern(record):
    try:
        assert (record.startswith("type")),'收集的log格式不对'
        common_record = re.match(r'type=(.*?) msg=audit\((.*?):(.*?)\):(.*)', record)
        for i in range(1,5):
            print(common_record.group(i))
        print(','.join([common_record.group(i) for i in range(1,5)]))
        get_rec=Record(common_record.group(1),common_record.group(2),common_record.group(3),common_record.group(4))
        return get_rec
    except:
        return None
#TODO
def parse_syscall(record):
    pass


def parse_cwd(record):
    pass


def parse_path(record):
    pass


def parse_audit_Record(record:Record):
    #  return  datamap={K:V , ... }
    map={}
    record_type=record.type
    if record_type=='SYSCALL':
        return parse_syscall(record)
    if record_type == 'cwd':
        return parse_cwd(record)    
    if record_type=='PATH':
        return parse_path(record)
    if record_type=='PROCTITLE':
        title=record.data
        return {'proctitle':title}

    return map




record=r'type=SYSCALL msg=audit(1710815446.295:49391): arch=c000003e syscall=257 success=yes exit=3 a0=ffffff9c a1=606c1bafd4ab a2=90800 a3=0 items=1 ppid=109773 pid=109774 auid=1000 uid=1000 gid=1000 euid=1000 suid=1000 fsuid=1000 egid=1000 sgid=1000 fsgid=1000 tty=pts5 ses=79 comm="zsh" exe="/usr/bin/zsh" subj=unconfined key="=dir_audit"'
parse_record2common_parttern(record)

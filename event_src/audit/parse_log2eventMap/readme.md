# 文档说明

> 这个模块主要用来将audispd的event数据，经过解析后，转化为键值对集合（每一个map对应一个事件）的形式。

函数说明

1. log2event  是入口函数，在这里通过子进程获取record日志，通过调用其他函数，完成将log-->event_map的转变
   将解析好的map送给event——process模块，
2. record_parse   `log-->Record`
   通过parse_record2common_parttern（）将record数据转化为Record类的形式
   parse_audit_Record(),将不同类型的Record解析问为键值对
   parse_type_record,将type类的记录转化为 K:V
3. event_parse    `event-->eventmap`
   通过将事件的信息解析到一个map中，可能涉及到不同type的Record解析

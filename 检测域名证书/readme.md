## 域名证书过期校验

> 1.运行脚本请先检查脚本中配置的ak sk对应的用户是否有dns的权限.
> 
> 2.本脚本只有调用华为云域名管理的功能.
>
> 3.巡检之后的结果存放在脚本运行目录的resault.xlsx
> 
> 4.注意kailinjt.com在内部解析和华为云解析记录可能不一致导致结果不一致。

## 2025年1月19日

> 优化代码运行方式，检测497主机条记录从6分钟左右优化到24秒。

## 运行

```python
python check_certs_expire.py
```


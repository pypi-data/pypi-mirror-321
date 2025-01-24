# Python Rcon for squad

这是一个针对于战术小队创建的rcon包。对于其他游戏可能不支持。
This is a rcon package built for squad. It might not support other games.

## 使用方法 How to use
```python
from pyrcon4squad import Rcon

with Rcon("localhost", 12345, "yourpassword") as rcon:
    print(rcon.command("listplayers"))
```
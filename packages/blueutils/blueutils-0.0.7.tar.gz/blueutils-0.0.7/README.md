# blueutils

这是一个python 的 工具集

## 安装
```
$ pip install blueutils
```

## 比特浏览器接口
比特浏览器官方虽然提供了api文档，但是没法直接拿来用，所以我对官方api文档进行封装了下，使用起来更简单了，使用方法如下：


```python
from blueutils.bitbrowser_api import BitBrowser

b = BitBrowser(id="你的浏览器id")    
b.open()
context = b.get_browser_context()
print(context)
b.close()
```

## 配置管理器
针对程序配置，提供一个ini配置文件，方便动态配置程序，使用方法如下：

from blueutils.config_manager import ConfigManager

config_manager = ConfigManager('config.ini')
config_manager.set('log', 'level', 'DEBUG')  # 设置默认值
config_manager.save() 
DOCKER_HOST = config_manager.get('log', 'level')  # 获取配置信息

## 飞书通知
可发送消息到飞书，方便监控程序运行状态，使用方法如下：
需要提前在飞书申请好通知密钥（完全免费），步骤为：
创建群组>>设置>>群机器人>>添加机器人>>自定义机器人>>添加>>保存Webhook 地址>>勾选签名校验>>保存签名>>完成
REPORT_URL 设置为Webhook 地址
REPORT_KEY 设置为签名

from blueutils.feishu_robot import FeishuRobot

feishu = FeishuRobot(webhook=REPORT_URL, secret=REPORT_KEY)
feishu.send_text(text="飞书通知")






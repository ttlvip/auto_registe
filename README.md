# emby 用户自助注册

一个注册页面, 可以方便的分享自己的emby给朋友. 省去帮朋友注册的麻烦.

运行前需要编写环境变量, 请完全将[]以及里面的内容替换成你自己的:

```bash
DOMAIN=[你的emby地址, 默认172.17.0.1]
PORT=[你的emby端口号, 默认8096]
API_KEY=[emby api]
COPY_USER_ID=[注册时默认复制哪个用户的配置, 建议创建一个有限权限用户]
IS_SSL=[是否启用SSL ,如果你的emby配置了htpps访问, 请写Y, 否则N]
```

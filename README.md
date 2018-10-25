# alipay(服务端支付宝)

### 密钥生成工具下载

支付宝提供一键生成工具便于开发者生成一对RSA密钥，可通过下方链接下载密钥生成工具：

http://p.tb.cn/rmsportal_6680_secret_key_tools_RSA_macosx.zip

下载该工具后，解压打开文件夹，运行“RSA签名验签工具.bat”（WINDOWS）或“RSA签名验签工具.command”（MAC_OSX）。

### 密钥工具使用注意
1、双击脚本文件 “RSA签名验签工具.command” 即运行RSA签名验签工具。
   使用SHA1withRSA生成签名。

2、如果双击脚本提示：“打不开"RSA签名验签工具.command"，因为它来自身份不明的开发者。”，请按如下步骤操作后，即可打开

(1)打开“系统偏好设置”

(2)打开“安全性与隐私”，点击左下角"点按锁按钮以进行更改"，此时会提示系统的登录密码，密码输入正确后会停留在"安全性与隐私"窗口

(3)在“安全性与隐私”窗口中“允许从以下位置下载的应用”会有三个选项(Mac App Store、Mac App Store和被认可的开发者、任何来源)，选择“任何来源”，此时会
提示是否“允许来自任何来源”，点击“允许来自任何来源”。

### 在服务器上程序执行方法
- 安装依赖

$ pip3 install django

$ pip install pycryptodome   # 专门用来做算法加密的

- 运行程序示例
python3 manage.py runserver 0.0.0.0:80

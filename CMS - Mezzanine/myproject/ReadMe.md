## Mezzanine （Windows10下）安装配置与修启动
- **DEMO VERSION**
### 1、下载安装Mezzanine
```
pip install mezzanine
```
### 2、创建项目
```
mezzanine-project 项目名
```
### 3、进入项目目录
```
cd 项目名
```
### 4、初始化数据库
```
python manage.py createdb
```
### 5、启动项目
```
python manage.py runserver
```
#### 5.1指定URL启动`(具体没摸透)`
```
python manage.py runserver localhost:端口号
```
> 指定URL启动，需要再settings.py中修改ALLOWED_HOST
>
> ```
> # ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
> # 修改如下
> ALLOWED_HOSTS = ["*"]
> ```


































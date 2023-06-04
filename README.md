## 项目结构

### appfront

前端部分，使用 `Vue2` 实现。

### MicroServices

`Django` 服务器

### myapp

后端部分

## 运行方式

### 首次运行

如果是首次运行，请先按照一下流程，将项目所需数据库建好。

1. 安装 MySQL 数据库，并创建名为 `microservices` 的数据库。

2. 在项目根目录使用终端运行以下内容

   ```shell
   python manage.py makemigrations
   python manage.py migrate
   ```
3. 终端进入 `appfront` 目录，运行 `npm install` 安装前端所需依赖。

### 前端

终端进入 `appfront` 目录，然后执行如下命令

```shell
npm run serve
```

### 后端

在项目根目录执行如下命令

```shell
python manage.py runserver
```

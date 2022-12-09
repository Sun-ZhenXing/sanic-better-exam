# 思政刷题简易服务

当前是 Sanic 搭建的简易后端，这里查看 [前端项目](https://gitee.com/sun-zhenxing/vue-better-exam.git)。

## 依赖

- Python >= 3.7
- `sanic`
- `python-docx`

安装依赖：

```bash
pip install -r requirements.txt
```

## 运行

确保你的前端已经打包完成，下面的命令用于克隆和打包前端项目：

```bash
git clone https://gitee.com/sun-zhenxing/vue-better-exam.git
cd vue-better-exam

yarn install
yarn build
```

将打包后的 `dist/` 文件夹复制到当前项目的 `static/` 下，然后执行下面的命令即可：

```bash
python server.py
```

默认监听 `127.0.0.1:8080`，如果你没有 Nginx 等代理服务器，可以在 [`server.py`](./server.py) 将其修改为 `0.0.0.0:80` 或者 `0.0.0.0:443`，然后运行服务。

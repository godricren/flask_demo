# url
协议：http/https
域名：www.baidu.com
端口号：http:80,https:443 一般不需要输入端口浏览器会默认添加
例子： https://www.baidu.com:443/path
/path是需要自己写的，前面的部分基本上是固定的
**url与视图，也可以称为path与视图**
## 路由与视图的映射
```python
@app.route('/')
def hello_world():
    return 'Hello World!'
```
## url 传参
1. 把参数固定在path中
```python
@app.route('/blog/<blog_id>')
def blog_detail(bolg_id):
    return f'Hello {blog_id} '
```
2. 可选参数的传递

```python
from flask import request
@app.route('book/list')
def book_list():
    #  arguments 参数
    #  requests.args 类字典类型
    page = request.args.get('page', default=1, type=int)
    return f'您获取的是第{page}的图书列表！'
```
# 模版渲染

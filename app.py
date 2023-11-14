from flask import Flask, request

'''
Flask类进行实例化
__name__为当前app.py这个模块
1. 以后出现bug， 可以帮助我们快速定位
2. 对于寻找模版文件，有一个相对路径
'''
app = Flask(__name__)

'''
创建一个路由和视图函数的映射
/ 代表跟路由（电脑中的路径同一个意思）
'''
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello you!'


@app.route('/profile')
def profile():
    return "I'm profile center"
# 带默认参数值的url
@app.route('/book/list')
def blog_list():
    page = request.args.get('page', default=1, type=int)
    return f'您获取的是第{page}页的图书列表！'

# 带参数的url
@app.route('/blog/<blog_id>')
def blog_detail(blog_id):
    return f'hello {blog_id}'

# 带参数的url
'''
1. debug模式
 1.1 修改代码后不需要停止项目，直接在浏览器中刷新就可以看到修改效果
 1.2 如果开发中遇到bug，开启debug模式在浏览器中可以看到出错信息
 开启方式：Edit configurations -> FLASK_DEBUG
 app.run(debug = True)
2. host
 局域网中其他终端通过IP地址访问当前主机
 开启方式：
  edit configurations --> additional options: --host=0.0.0.0
  app.run(host = 0.0.0.0)
3. port修改
 默认使用5000，端口号如果需要修改
 edit configurations --> additional options: --port=8000
'''
if __name__ == '__main__':
    app.run()

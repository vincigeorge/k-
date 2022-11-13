from flask import Flask, make_response, request
from flask_cors import CORS  # 引用CORS，后期需要VUE支持跨域访问会用到

# Flask类只有一个必须指定的参数，即程序主模块或者包的名字，__name__是系统变量，该变量指的是本py文件的文件名
app = Flask(__name__)
# resources全局配置允许跨域的API接口，我们这边为了学习，配置所有，详细学习请百度搜索文档
CORS(app, resources=r'/*')


@app.route('/', methods=['GET', 'POST'])
def run():
    getJson = request.get_json()
    username = str(getJson.get('username'))  # json数据格式
    password = int(getJson.get('password'))  # json数据格式

    if username == 'admin' and password == 123:
        res = {
            'code': 0,
            'msg': "OK",
            'data': {
                'test': '测试页面'
            }
        }
    else:
        res = {
            'code': 999,
        }
    return make_response(res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False, threaded=True)

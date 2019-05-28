# -*- coding:utf-8 -*-
# /usr/bin/python
'''
@Author:  Yan Errol  
@Email:2681506@gmail.com   
@Date:  2019-05-28  17:11
@File：webserver.py
@Describe:webserver
'''


from flask import Flask
from flask import request
import pandas as pd
import server_demo


# 传递根目录
class WebServer:
    '''
    导入Flask框架，这个框架可以快捷地实现了一个WSGI应用
    '''

    def __init__(self, properties):
        self.port = properties['port']
        self.host = None
        if 'host' in properties.keys():
            self.host = properties['host']
        self.app = Flask('predict service')
        self.properties = properties

        @self.app.route('/')
        def predict():
            param_dict = {}
            if request.method == 'POST':
                data_request = request.form.to_dict()
                for k, v in data_request.items():
                    param_dict[k] = v

            else:
                for k, v in request.args.items():
                    param_dict[k] = v

            title = param_dict['title']
            docx_path= param_dict['docx_path']
            csv_path= param_dict['csv_path']
            print(title,docx_path,csv_path)
            val = server_demo.cal_sim_sent(title,docx_path,csv_path)
            inputs = []

            inputs = pd.DataFrame(inputs)
            param_dict['inputs'] = inputs

            ret_info = val

            return ret_info

    def start(self):
        '''开始服务 '''
        if self.host != None:
            self.app.run(host=self.host, port=self.port, debug=True, use_reloader=False)
        else:
            self.app.run(port=self.port, debug=True, use_reloader=False)


def main():
    '''
    webserve :实例   http://127.0.0.1:8888/?title=江苏公司千里眼平台数据自动上传总部&docx_path=/Users/yanerrol/Desktop/Text_Similarity/test_input/test.docx&csv_path=/Users/yanerrol/Desktop/Text_Similarity/data/test.csv
    :return:
    '''
    #args = parser_args()
    properties = {"host":"127.0.0.1",'port':"8888"}
    server = WebServer(properties)
    server.start()



if __name__ == "__main__":
    main()
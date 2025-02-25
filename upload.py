# coding:utf-8
import os
import argparse
from urllib.parse import quote_plus
import requests

# 创建命令行参数解析器
parser = argparse.ArgumentParser(description='上传指定目录下的所有文件到 anythingLLM知识库工具')
parser.add_argument('--host', default='localhost', help='API 主机地址，默认为 localhost')
parser.add_argument('--port', type=int, default=3001, help='API 端口号，默认为 3001')
parser.add_argument('--key', required=True, help='授权API KEY密钥，必填参数')
parser.add_argument('--input', default='.', help='要上传文件的目录，默认为当前目录')

# 解析命令行参数
args = parser.parse_args()

# 构建 API 接口的 URL
url = f'http://{args.host}:{args.port}/api/v1/document/upload'

# 请求头
headers = {
    'accept': 'application/json',
    'Authorization': f'Bearer {args.key}'
}

# 遍历目录下的所有文件
for root, dirs, files in os.walk(args.input):
    for file in files:
        file_path = os.path.join(root, file)
        # 对文件名进行 URL 编码
        encoded_file_name = quote_plus(os.path.basename(file_path))

        encoded_file_name = os.path.basename(file_path).encode("GBK").decode("GBK")

        try:
            # 打开文件并准备上传
            with open(file_path, 'rb') as f:
                # 构建表单数据
                data = {
                    'name': encoded_file_name.encode("utf-8")
                }
                files = {
                    'file': (os.path.basename(file_path), f)
                }

                # 发送 POST 请求
                response = requests.post(url, headers=headers, data=data, files=files)

                # 检查响应状态码
                if response.status_code == 200:
                    print(f"成功上传文件: {file_path}")
                    print("服务器响应:", response.text)
                else:
                    print(f"上传文件 {file_path} 失败:")
                    print("错误信息:", response.text)
        except Exception as e:
            print(f"上传文件 {file_path} 失败:")
            print("错误信息:", str(e))
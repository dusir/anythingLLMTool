# coding:utf-8
import os
import subprocess
import argparse

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
        # 构建 curl 命令
        curl_command = [
            'curl',
            '-X', 'POST',
            url
        ]
        # 添加请求头
        for key, value in headers.items():
            curl_command.extend(['-H', f'{key}: {value}'])
        # 添加表单字段
        curl_command.extend([
            '-F', f"name={os.path.basename(file_path)}",
            '-F', f"file=@/{file_path}"
        ])
        try:
            # 执行 curl 命令
            result = subprocess.run(curl_command, capture_output=True, text=True, check=True)
            print(f"成功上传文件: {file_path}")
            print("服务器响应:", result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"上传文件 {file_path} 失败:")
            print("错误信息:", e.stderr)
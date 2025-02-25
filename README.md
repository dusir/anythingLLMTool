# anythingLLMTool

## anythingLLM知识库文档上传只能一个文档一个文档的上传，非常麻烦，所以我们搞了一个命理行工具，辅助大家上传文件夹里所有支持的文件。

## 上传文件到 anythingLLM知识库工具,可以将你指定的目录下的所有支持的文件上传到你的anythingLLM知识库当中，然后你就可以批量操作了。

```bash
python upload.py --key=XXXX-XXXX-XXXX-XXXX --input=/data
```
比如我的env：
```
python upload.py  --key AZ9FPRR-0ZFM3FT-NXXQJZ8-21M4GSB --input /Users/bob/Documents/github/data

```
对应目录举例：
$ ls  ../data/  

103：大模型应用开发极简入门：基于 GPT-4 和 ChatGPT_2024.pdf  
104：一本书读懂AIGC：ChatGPT、AI绘画、智能文明与生产力变革_2023.pdf  
从零开始大模型开发与微调基于PyTorch与ChatGLM.pdf  
大规模语言模型：从理论到实践.pdf  

我的目录里有这几个pdf文件。

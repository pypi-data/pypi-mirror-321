# ShangshanAI SDK

一个用于下载和处理数据的Python SDK。

## 安装

```bash
pip install shangshanAI
```

## 下载模型

```python
from shangshanAI import snapshot_download
model_dir = snapshot_download('testuser/model_llm')
print(model_dir)
```

## 功能特性

- 支持文件下载
- 自动重试机制
- 进度显示

## 许可证

MIT License
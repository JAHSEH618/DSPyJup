# DSPyJup - DSPy Framework with Jupyter Notebooks

这是一个基于 DSPy 框架的项目，主要用于探索和实现各种大语言模型应用。项目包含了多个 Jupyter Notebook 示例，演示了如何使用 DSPy 构建智能应用。

## 项目概述

DSPy 是一个用于算法优化 LM 提示和权重的框架，即使使用较弱的模型也能获得强大结果。本项目通过 Jupyter Notebook 的形式展示 DSPy 在实际场景中的应用。

## 主要特性

- 使用 DSPy 框架进行提示优化和程序优化
- 集成 OpenAI 和 LiteLLM 模型
- 利用 MLflow 进行实验跟踪
- 包含多个实际应用场景的示例 Notebook

## 项目结构

```
.
├── DSPyCodes/           # DSPy 相关代码
├── JupNotebooks/        # Jupyter Notebook 示例
│   ├── demo1.ipynb      # DSPy 基础功能演示
│   ├── airlineCustomerService.ipynb  # 航空公司客服系统示例
│   └── ...
├── data/                # 数据文件
├── models/              # 模型文件
├── mlruns/              # MLflow 实验记录
├── requirements.txt     # 项目依赖
└── README.md           # 项目说明文档
```

## 安装依赖

```bash
pip install -r requirements.txt
```

## 环境配置

项目需要配置以下环境变量：

```bash
export OPENAI_API_KEY="your_openai_api_key"
```

## 使用方法

1. 启动 Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

2. 打开 `JupNotebooks/` 目录下的示例文件开始探索

## 示例说明

### demo1.ipynb
基础情感分类示例，展示了如何使用 DSPy 创建简单的分类任务。

### airlineCustomerService.ipynb
航空公司客服系统示例，演示了如何构建一个复杂的 ReAct Agent 来处理航班预订、查询和取消等操作。

## 技术栈

- [DSPy](https://github.com/stanfordnlp/dspy) - 大语言模型提示优化框架
- [OpenAI API](https://platform.openai.com/docs/) - OpenAI 模型接口
- [LiteLLM](https://github.com/BerriAI/litellm) - 统一的大语言模型接口
- [MLflow](https://mlflow.org/) - 机器学习实验跟踪平台
- [Pydantic](https://docs.pydantic.dev/) - 数据验证和设置管理
- [Jupyter Notebook](https://jupyter.org/) - 交互式开发环境

## 许可证

本项目仅供学习和研究使用。
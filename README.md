# langchain入门记录

## LLM模型调用

核心能力：（1）支持模板化调用, 核心类：`ChatPromptTemplate` (2) 支持streaming输出, 核心方法：`model.stream(messages)`
参照代码: [langchain-deepseek.ipynb](langchain-deepseek.ipynb)

## 文档加载器document loaders,嵌入embeddings,vector store

这些抽象旨在支持从（矢量）数据库或者其他来源检索数据，以便与LLM工作流集成。常见的表现形式如：RAG(Retrieval augmented generation)

Langchain实现了一个 `Document`抽象，表示一个文本单元和关联的元数据，它有三个属性：

1. `page_content`: 表示内容的字符串
2. `metadata`: 包含任意元数据的dict, 如文档来源，文档与其他文档的关系等
3. `id`: （可选的）文档的字符串标识符

> 单个`Document`对象通常表示较大文档的一个块

## 工具调用

# 提示词工程

- 提示词工程基础
- 多智能体在提示词工程中的莹莹
- 提示词的要素与技巧
- 思维链COT
- 常见自然语言任务的提示词
- RAG与工具

## 0. 引言

随着大模型的快速发展，**提示工程(Prompt Engineering)**应运而生，通过设计和优化提示词确保LLM更好的满足用户需求。掌握提示工程

# 示例应用

## mini版本-deepsearch


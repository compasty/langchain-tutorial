# langchain入门记录

## LLM模型调用

核心能力：（1）支持模板化调用, 核心类：`ChatPromptTemplate` (2) 支持streaming输出, 核心方法：`model.stream(messages)`
参照代码: [langchain-deepseek.ipynb](langchain-deepseek.ipynb)

## 消息类型

在 LangChain 中，聊天消息（Chat Messages）是与对话式大模型交互的基础抽象。不同“角色”的消息会影响模型的行为与上下文控制。常见类型包括：
- SystemMessage（系统消息）
- HumanMessage（用户消息）
- AIMessage（模型消息）
- ToolMessage（工具返回消息）
- FunctionMessage（函数返回消息，较老接口）
- ChatMessage（自定义角色消息）
- 多模态变体（如带图片、音频的消息）

## ChatMessageHistory

ChatMessageHistory 是 LangChain 中用于管理“对话历史（消息队列）”的轻量级存储抽象。它提供统一的 API 来追加、读取和清空历史消息，常与 Memory（记忆）组件、对话式链条（LCEL/Chains）以及代理（Agents）一起使用，确保模型在多轮对话中能看到必要的上下文。

核心作用：
- 作为“短期会话缓冲区”：记录 System/Human/AI/Tool 等消息。
- 为 Memory 接口适配：如 ConversationBufferMemory、ConversationTokenBufferMemory 等的后端。
- 提供持久化（可选）：可以无状态（内存）或接入外部存储（Redis、Postgres、FAISS、Chroma 等扩展实现）

存储的元素是“消息对象”（如SystemMessage, HumanMessage, ChatMessage等）。

ChatMessageHistory 本身是“消息存储”；而 Memory 是“如何把历史嵌入到提示里”的策略。常见的策略有：

- `ConversationBufferMemory`: 将全部历史按原文拼接进 prompt。适合短对话/上下文较小场景。
- `ConversationBufferWindowMemory`: 仅保留最近 k 轮对话，降低令牌占用。
- `ConversationTokenBufferMemory`: 基于 token 预算截断，自动控制上下文长度。
- `CombinedMemory` / `EntityMemory`等：将历史拆分成不同视图或结构化摘要


## 文档加载器document loaders,嵌入embeddings,vector store

这些抽象旨在支持从（矢量）数据库或者其他来源检索数据，以便与LLM工作流集成。常见的表现形式如：RAG(Retrieval augmented generation)

Langchain实现了一个 `Document`抽象，表示一个文本单元和关联的元数据，它有三个属性：

1. `page_content`: 表示内容的字符串
2. `metadata`: 包含任意元数据的dict, 如文档来源，文档与其他文档的关系等
3. `id`: （可选的）文档的字符串标识符

> 单个`Document`对象通常表示较大文档的一个块

## 工具调用

# langgraph

LangGraph 是基于 LangChain 的“有状态有边界”的工作流/代理框架，用来把 LLM 应用建模为“图”（节点+边+状态）。它特别适合多步推理、工具编排、循环与分支控制（如 ReAct、规划-执行-反思、故障重试等），并提供持久化的“对话/任务状态”与可观测能力。

使用场景：

- ReAct/Tool-Use 多轮代理（规划→执行工具→整合→下一步）。
- 复杂的 RAG 流程（检索→评估→改写查询→二次检索→生成）。
- 长任务编排（抓取→清洗→抽取→总结→回传）

## Agent&Workflow

**Agent(智能体)** 是在大语言模型应用中，通过“感知-决策-行动-反馈”的闭环来完成任务的可编排实体。它不仅生成文本，还能根据目标与环境状态自主选择工具、调用外部系统、迭代计划并纠错.

- 感知（Perception）：读取指令、上下文、环境状态（对话历史、检索结果、传感数据）。
- 决策（Decision）：基于策略（Prompt/规则/策略模型）选择下一步动作或工具。
- 行动（Action）：调用工具/函数/API（如搜索、数据库查询、代码执行）。
- 反馈（Feedback）：处理工具结果，更新记忆/状态，必要时再次规划，直至完成目标

Anthropic将agent系统划分为两类：
1. `workflow`: 按照预定义的工作流编排LLM和工具，固定代码路径
2. `agent`: 更复杂的系统，能够根据环境状态和目标动态调整执行路径。

> langgraph中一切都是图，Agent是图中的一个节点，可以使用`create_react_agent`创建。

## langgraph CLI

langgraph CLI 是一个用于管理和操作 langgraph 应用的命令行工具。它提供了一系列命令，用于创建、部署、监控和调试 langgraph 应用。

- `langgraph build`: Build LangGraph API server Docker image.
- `langgraph dev`: Run LangGraph API server in development mode with...
- `langgraph dockerfile`: Generate a Dockerfile for the LangGraph API server, with...
- `langgraph new`: Create a new LangGraph project from a template.
- `langgraph up`: Launch LangGraph API server.

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



## agent(代理)开发

代理就像一个多功能的接口，它能够接触并使用一套工具。根据用户的输入，代理会决定调用哪些工具。它不仅可以同时使用多种工具，而且可以将一个工具的输出数据作为另一个工具的输入数据。

ReAct（Reasoning-Acting）框架表达的是“行动”和“推理”之间的协同作用，这种协同作用使得咱们人类能够学习新任务并做出决策或推理。这个框架的来源: [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/pdf/2210.03629)， 其核心启发：**大语言模型可以通过生成推理痕迹和任务特定行动来实现更大的协同作用。**
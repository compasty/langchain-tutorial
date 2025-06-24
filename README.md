# langchain入门记录

## agent(代理)开发

代理就像一个多功能的接口，它能够接触并使用一套工具。根据用户的输入，代理会决定调用哪些工具。它不仅可以同时使用多种工具，而且可以将一个工具的输出数据作为另一个工具的输入数据。

ReAct（Reasoning-Acting）框架表达的是“行动”和“推理”之间的协同作用，这种协同作用使得咱们人类能够学习新任务并做出决策或推理。这个框架的来源: [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/pdf/2210.03629)， 其核心启发：**大语言模型可以通过生成推理痕迹和任务特定行动来实现更大的协同作用。**
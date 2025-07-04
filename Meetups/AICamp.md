# AI Camp 2023/10/30

https://www.meetup.com/dc-ai-llms/events/296543682/

## Detecting and Debugging AI Agent Drift
Speaker: Josh Reini, DevRel Engineer @TruEra
Abstract: In a LLM-powered autonomous agent system, LLMs function as the agent’s brain by using planning and inference to decide what tools to use and how.
These tools can act as real-time data sources or perform real actions such as ordering food delivery, booking flights or setting doctor’s appointments.
However LLM agents, like other ML systems, are subject to drift. This talk will cover the causes of LLM drift, and how to identify and debug them with open source TruLens.

Testing RAGs for hallucinations. The RAG Triad:
Query -(Is the context relevant to the query?)->
Context -(Is the response supported by the context?)->
Response -(?)-> Loop

## Caching for ChatGPT and More with Vector Databases
Speaker: Yujian Tang, Developer Advocate @Zilliz
Abstract: A few months ago, AI was “hip” and “cool”, but it wasn’t mainstream. Then, ChatGPT single handedly put AI, and large language models (LLMs) in particular,
on everyone’s radar. Since then, people have made all sorts of applications using GPT and its extensions including a bot to automatically order pizza.
Despite all the potential of LLMs, they still have some limitations. In this talk, we will cover how to overcome some of these limitations by using
vector databases to inject domain specific knowledge. We will also share some open source tools that cache LLM responses helping you decrease the
cost and increase the performance of your LLM app.

## LLMs for Continuous Research
Speaker: Nisha Iyer, Advisor @ CoNote
Abstract: CI/CD embraces the power of continuous work, agile development and ability to iterate and move fast. The missing piece is often research,
alongside the stealth process of CI/CD. Traditional UX Research cycles take time and effort, as they should. With CoNote, an AI Product that scales
and charges your research. Today, I will talk through what makes our AI engine unique and how we use LLMs in production. I will also talk through
some of the exciting AI features to come and some ideating that we are doing as a team to make our engine even more powerful.
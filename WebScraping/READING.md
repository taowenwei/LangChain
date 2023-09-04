## 1. Define agents prompt

The <span style="color:red;">agent prompt</span> below,
```python
auto_agent_instructions()
```

## 2. given a question, match it with an agent by using OpenAI.ChatCompletion

*The chatCompletion API allows developers to send a series of messages as input to the model and receive a model-generated message as output.*

```python
send_chat_completion_request (c:\Users\WTAO-WIN\OneDrive\Documents\LangChain\gpt-researcher\agent\llm_utils.py:65)
create_chat_completion (c:\Users\WTAO-WIN\OneDrive\Documents\LangChain\gpt-researcher\agent\llm_utils.py:52)
choose_agent (c:\Users\WTAO-WIN\OneDrive\Documents\LangChain\gpt-researcher\agent\llm_utils.py:110)
websocket_endpoint (c:\Users\WTAO-WIN\OneDrive\Documents\LangChain\gpt-researcher\main.py:52)
<module> (<string>:1)
```

## 3. run the agent with a predefined query prompt by using OpenAI.ChatCompletion

The <span style="color:red;">query prompt</span> below,
```python
generate_search_queries_prompt()
```

```python
send_chat_completion_request (c:\Users\WTAO-WIN\OneDrive\Documents\LangChain\gpt-researcher\agent\llm_utils.py:65)
create_chat_completion (c:\Users\WTAO-WIN\OneDrive\Documents\LangChain\gpt-researcher\agent\llm_utils.py:52)
call_agent (c:\Users\WTAO-WIN\OneDrive\Documents\LangChain\gpt-researcher\agent\research_agent.py:80)
create_search_queries (c:\Users\WTAO-WIN\OneDrive\Documents\LangChain\gpt-researcher\agent\research_agent.py:93)
conduct_research (c:\Users\WTAO-WIN\OneDrive\Documents\LangChain\gpt-researcher\agent\research_agent.py:141)
run_agent (c:\Users\WTAO-WIN\OneDrive\Documents\LangChain\gpt-researcher\agent\run.py:50)
start_streaming (c:\Users\WTAO-WIN\OneDrive\Documents\LangChain\gpt-researcher\agent\run.py:38)
websocket_endpoint (c:\Users\WTAO-WIN\OneDrive\Documents\LangChain\gpt-researcher\main.py:60)
<module> (<string>:1)
```

It then returns a list of queries.

## 4. run DuckDuckGo against each query to return a list of website URLs

```python
web_search (c:\Users\WTAO-WIN\OneDrive\Documents\LangChain\gpt-researcher\actions\web_search.py:19)
async_search (c:\Users\WTAO-WIN\OneDrive\Documents\LangChain\gpt-researcher\agent\research_agent.py:103)
run_search_summary (c:\Users\WTAO-WIN\OneDrive\Documents\LangChain\gpt-researcher\agent\research_agent.py:125)
conduct_research (c:\Users\WTAO-WIN\OneDrive\Documents\LangChain\gpt-researcher\agent\research_agent.py:143)
run_agent (c:\Users\WTAO-WIN\OneDrive\Documents\LangChain\gpt-researcher\agent\run.py:50)
start_streaming (c:\Users\WTAO-WIN\OneDrive\Documents\LangChain\gpt-researcher\agent\run.py:38)
websocket_endpoint (c:\Users\WTAO-WIN\OneDrive\Documents\LangChain\gpt-researcher\main.py:60)
<module> (<string>:1)
```


## 5. load each URL and get summary

* get html - scrape_text_with_selenium()
    * use `headless` web browsers
    * use selenium's `webdriver` to load the URL and get its html body part
    * use `BeautifulSoup` to extract texts from ['h1', 'h2', 'h3', 'h4', 'h5', 'p'] tags
    * split text to chunks
* get summary from the chunks - summarize_text()
    * use predefined <span style="color:red;">summary prompt</span>
    * use OpenAI.ChatCompletion again for generating summary

## 6. write report by using report promot

The <span style="color:red;">report prompt</span> below,
```python
generate_report_prompt()
```

use OpenAI.ChatCompletion for generating report
```python
create_chat_completion (c:\Users\WTAO-WIN\OneDrive\Documents\LangChain\gpt-researcher\agent\llm_utils.py:51)
call_agent (c:\Users\WTAO-WIN\OneDrive\Documents\LangChain\gpt-researcher\agent\research_agent.py:80)
write_report (c:\Users\WTAO-WIN\OneDrive\Documents\LangChain\gpt-researcher\agent\research_agent.py:170)
run_agent (c:\Users\WTAO-WIN\OneDrive\Documents\LangChain\gpt-researcher\agent\run.py:52)
start_streaming (c:\Users\WTAO-WIN\OneDrive\Documents\LangChain\gpt-researcher\agent\run.py:38)
websocket_endpoint (c:\Users\WTAO-WIN\OneDrive\Documents\LangChain\gpt-researcher\main.py:60)
<module> (<string>:1)
```


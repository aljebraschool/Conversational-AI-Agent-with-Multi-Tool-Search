import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_classic.agents import initialize_agent, AgentType
from langchain_community.callbacks import StreamlitCallbackHandler
import os
from dotenv import load_dotenv

#load environment variable
load_dotenv()

#create arxiv wrapper and tool
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max = 500)
arxiv_tool = ArxivQueryRun(api_wrapper=arxiv_wrapper)

#create wikipedia wrapper and tool
wikipedia_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=500)
wikipedia_tool = WikipediaQueryRun(api_wrapper=wikipedia_wrapper)

#create another tool for searching on the internet
search = DuckDuckGoSearchRun(name = "Search")

st.title("Agents and Tools with Langchain")
st.markdown("""
**Interactive AI Agent with Search Capabilities**
This chatbot can search the internet, Wikipedia, and ArXiv to answer your questions.
""")
""" 
in this example, we're using StreamlitCallbackHandler to display the thoughts and actions of the agents 
in the interactive streamlit app 
"""

#Sidebar for api key
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Groq api key", type="password", help="Get your API key from console.groq.com")

# FIX 1: Add API key validation
if not api_key:
    st.warning("⚠️ Please enter your Groq API key in the sidebar to continue.")
    st.stop()

#create a default session state for the streamlit app
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "assistant", 
            "content": "Hello! I'm an AI chatbot equipped with internet search capabilities. I can search Wikipedia, ArXiv papers, and the web to help answer your questions. How can I assist you today?"
            
        }
    ]

#create a chat history subheader
st.subheader("💬 Chat History")
for message in st.session_state.messages:
    #give the chat message its role 
    with st.chat_message(message["role"]):
        #then write to it
        st.write(message["content"])



if prompt := st.chat_input("Ask me anything..."):
    #add user message to session
    st.session_state.messages.append({"role":"user", "content":prompt})

    #display user message
    with st.chat_message("user"):
        st.write(prompt)

    #initialize model and agent
    try:
        model = ChatGroq(
            api_key=api_key, 
            model = "llama-3.1-8b-instant", 
            streaming=True, 
            temperature=0.1
            )
        tools = [search, arxiv_tool, wikipedia_tool]

        #convert tools to agent to use it (This is an agent executor that will be used to load the LLM and use its given tools)
        search_agent = initialize_agent(
            tools=tools, 
            llm = model,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            handling_parsing_errors = True,
            verbose = True

            )
        
        #display ai response 
        with st.chat_message("assistant"):
            #create container that will be used to show ai reasoning response
            with st.container():
                st.write("🤔 **Thinking and searching...**")

                #create callback handler for displaying thought
                st_callbacks = StreamlitCallbackHandler(
                    st.container(),
                    expand_new_thoughts = False,
                    collapse_completed_thoughts = True
                )

            #pass only the current prompt not entire message history
            with st.spinner("Processing your request..."):
                try:
                    response = search_agent.run(prompt, callbacks=[st_callbacks])

                    #add ai response to session state
                    st.session_state.messages.append({

                            "role": "assistant", 
                            "content": response

                         })
                    
                    #display the final response
                    st.success("✅ **Final Answer:**")
                    st.write(response)

                except Exception as agent_error:
                    error_message = f"sorry, I encountered an error while processing your request: {str(agent_error)}"
                    st.session_state.messages.append({
                        "role":"assistant",
                        "content": error_message
                    })

    except Exception as e:
        error_message = f"error initializing model {str(e)}"
        st.error(error_message)
        st.info("Please check your API key and try again!")

# Add clear chat button
if st.sidebar.button("🗑️ Clear Chat History"):
    st.session_state["messages"] = [
        {
            "role": "assistant", 
            "content": "Hello! I'm an AI chatbot equipped with internet search capabilities. How can I assist you today?"
        }
    ]
    st.rerun()

# Add some helpful information in sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### 🔧 Available Tools:")
st.sidebar.markdown("• 🌐 **Web Search** - DuckDuckGo")
st.sidebar.markdown("• 📚 **Wikipedia** - Encyclopedia articles") 
st.sidebar.markdown("• 📄 **ArXiv** - Academic papers")

st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 Example Questions:")
st.sidebar.markdown("• What is quantum computing?")
st.sidebar.markdown("• Latest AI research papers")
st.sidebar.markdown("• Current events today")




























# #create a chat input widget for the prompt
# prompt = st.chat_input(placeholder="What is machine learning:?")

# if prompt:
#     #appending the prompt user entered to the session state
#     st.session_state.messages.append({"role": "user", "content":prompt})
#     #give the chat message its role 
#     st.chat_message("user")
#     #then write to it
#     st.write(prompt)

#     #set up your model
#     model = ChatGroq(api_key = api_key, model = "deepseek-r1-distill-llama-70b", streaming=True)

#     tools = [search, arxiv_tool, wikipedia_tool]

#     #convert tools to agent to use it (This is an agent executor that will be used to load the LLM and use its given tools)
#     search_agent = initialize_agent(AgentType.ZERO_SHOT_REACT_DESCRIPTION, tools=tools, llm=model, handling_parsing_error = True)

#     #this will display the reasoning of the ai as its builds its response
#     with st.chat_message("ai"):
#         #it will use container for multiple element and also be able to expand it
#         chatbot_thought = StreamlitCallbackHandler(st.container(), expand_new_thought = False)
#         #run the agent
#         response = search_agent.run(st.session_state.messages, callbacks = [chatbot_thought])
#         #append the new response in the session state again
#         st.session_state.messages.append({"role":"ai", "content":response})
#         #show the response 
#         st.write(response)
        

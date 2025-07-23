# Conversational AI Agent with Multi-Tool Search
A complete end-to-end Streamlit application that enables intelligent conversations with an AI agent equipped with multiple search capabilities. This project uses LangChain agents powered by Groq's language models with memory to maintain conversation context and provide accurate, well-researched answers.

📝 **Description**

This application allows users to have natural conversations with an AI agent that can search multiple sources to answer questions. The agent remembers conversation history and can provide contextual responses based on previous interactions.

Using the Agent-Tool approach with conversation memory, the system:

1. Processes user queries through a conversational interface
2. Determines the best tools to use for each query
3. Searches Wikipedia for encyclopedia information
4. Searches ArXiv for academic papers and research
5. Searches the web using DuckDuckGo for current information
6. Maintains conversation memory for contextual responses
7. Generates comprehensive answers using Groq's language models

🌐 **Live Demo**
Access the live demo on Streamlit Cloud:
Your App Link [Here](#) <!-- Add your deployed app link here -->

<img width="1661" height="829" alt="image" src="https://github.com/user-attachments/assets/c6bf78f4-55e4-46f3-9dfa-f394b115c7b8" />


🚀 **Features**
- **Complete Conversational Experience**: Multi-turn conversations with memory
- **Multi-Source Search**: Wikipedia, ArXiv, and web search capabilities
- **Intelligent Tool Selection**: Agent automatically chooses the best tools for each query
- **Conversation Memory**: Remembers chat history for contextual responses
- **Real-time Reasoning Display**: Shows agent's thinking process and tool usage
- **User-Friendly Interface**: Clean Streamlit-based UI with chat history
- **Error Handling & Recovery**: Robust error management for better user experience
- **Expandable Tool Integration**: Easy to add new search tools and capabilities

📂 **Repository Structure**
```bash
Streamlit-Conversational-Agent
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── .env                     # Environment variables template
├── README.md                # This file
└── assets/                  # Screenshots and demo images
    └── demo_screenshot.png
```

🛠️ **Installation**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/Streamlit-Conversational-Agent.git
   cd Streamlit-Conversational-Agent
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

🔑 **API Keys**

This application requires an API key from:
- [Groq Console](https://console.groq.com) - For the language model

Create a `.env` file in the project's root directory with the following variable:
```bash
GROQ_API_KEY=your_groq_api_key_here
```

(For Streamlit Cloud deployment, add this as a secret in your Streamlit Cloud dashboard instead.)

📋 **Local Usage**

1. **Set up your environment:**
   - Ensure you have your Groq API key in the `.env` file or enter it in the sidebar

2. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

3. **Interact with the Agent:**
   - Enter your Groq API key in the sidebar settings
   - Start asking questions in the chat input box
   - The agent will automatically choose the best tools to answer your questions
   - View the agent's reasoning process in real-time
   - Continue the conversation - the agent remembers your chat history

**Example Queries:**
- "What is quantum computing?" (Uses Wikipedia)
- "Find recent papers about machine learning" (Uses ArXiv)
- "What's happening in AI news today?" (Uses web search)
- "Tell me more about that" (Uses conversation memory)

🚀 **Deploying to Streamlit Cloud**

1. **Push your code to GitHub:**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud:**
   - Go to [Streamlit Cloud](https://share.streamlit.io)
   - Connect your GitHub repository
   - Select `app.py` as the main file
   - Add your `GROQ_API_KEY` in the secrets section

3. **Configure secrets in Streamlit Cloud:**
   ```toml
   GROQ_API_KEY = "your_groq_api_key_here"
   ```

4. **Deploy and share your app link!**

🧩 **How It Works**

1. **User Input Processing**
   - User enters a question in the chat interface
   - The system adds the query to conversation memory

2. **Agent Reasoning**
   - Agent analyzes the question using ReAct methodology (Reasoning + Acting)
   - Determines which tools are most relevant for the query

3. **Tool Execution**
   - **Wikipedia Tool**: Searches encyclopedia articles for factual information
   - **ArXiv Tool**: Searches academic papers and research documents
   - **Web Search Tool**: Uses DuckDuckGo for current web information

4. **Response Generation**
   - Agent synthesizes information from multiple sources
   - Generates a comprehensive answer using Groq's language model
   - Maintains conversation context for follow-up questions

5. **Memory Management**
   - Stores conversation history using LangChain's memory system
   - Provides contextual responses based on previous interactions

🔧 **Technologies Used**

- **[Streamlit](https://streamlit.io/)** - Web interface and deployment platform
- **[LangChain](https://www.langchain.com/)** - Agent framework and tool orchestration
- **[Groq](https://groq.com/)** - Fast language model inference
- **LangChain Community Tools** - Wikipedia, ArXiv, and DuckDuckGo integrations
- **ConversationBufferWindowMemory** - Chat history management
- **StreamlitCallbackHandler** - Real-time agent reasoning display

📦 **Requirements**

```txt
streamlit
langchain
langchain-groq
langchain-community
python-dotenv
wikipedia
arxiv
duckduckgo-search
```

See `requirements.txt` for complete dependency list with versions.

⚙️ **Configuration Options**

You can customize the agent behavior by modifying these parameters in `app.py`:

- **Memory Window**: Change `k=5` in `ConversationBufferWindowMemory` to remember more/fewer exchanges
- **Model Selection**: Modify the Groq model (currently using `deepseek-r1-distill-llama-70b`)
- **Search Results**: Adjust `top_k_results` and `doc_content_chars_max` for search tools
- **Agent Type**: Switch between different agent types for various behaviors

🔍 **Available Tools**

| Tool | Purpose | Source |
|------|---------|--------|
| 🌐 **Web Search** | Current events, general web information | DuckDuckGo |
| 📚 **Wikipedia** | Encyclopedia articles, factual information | Wikipedia API |
| 📄 **ArXiv** | Academic papers, research documents | ArXiv API |

🤝 **Contributing**

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

**Ideas for contributions:**
- Add more search tools (Google Scholar, PubMed, etc.)
- Implement different memory strategies
- Add export functionality for conversations
- Improve UI/UX with additional features
- Add support for file uploads and document analysis

📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

🙏 **Acknowledgements**

- **Groq** for providing fast LLM inference
- **LangChain** for the comprehensive agent framework
- **Streamlit** for the intuitive web application platform
- **Wikipedia**, **ArXiv**, and **DuckDuckGo** for providing free access to information
- The open-source community for the amazing tools and libraries

---

**Made with ❤️ and AI**

For questions or support, please open an issue or reach out via [your-email@example.com](mailto:your-email@example.com)

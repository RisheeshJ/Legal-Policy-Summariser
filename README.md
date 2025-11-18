Legal Document Summarizer 📜⚖️
An intelligent AI-powered tool that automatically analyzes legal documents and policies, transforming complex legal text into clear, actionable Do's and Don'ts with concise summaries.
🌟 Features

AI-Powered Analysis: Utilizes Gemma 3 LLM for intelligent document processing
Dual Input Methods:

Upload documents (.txt, .pdf, .doc, .docx)
Direct text paste into the interface


Smart Summarization: Generates comprehensive summaries with structured Do's and Don'ts
User-Friendly Interface: Clean Gradio-based UI for seamless interaction
Copy-Ready Output: Easy-to-copy results for documentation
Document Validation: Automatically identifies non-legal documents

🚀 Demo
Show Image
Upload a legal document or paste text directly to get instant analysis
🛠️ Tech Stack

Python 3.8+
LangChain: LLM orchestration framework
Ollama: Local LLM runtime
Gradio: Web UI framework
Gemma 3 (1B): Language model for analysis

📋 Prerequisites
Before running this project, ensure you have:

Python 3.8 or higher installed
Ollama installed on your system
Gemma 3 model pulled in Ollama

Installing Ollama
bash# For Linux/Mac
curl -fsSL https://ollama.com/install.sh | sh

# For Windows
# Download from https://ollama.com/download
Pulling Gemma 3 Model
bashollama pull gemma3:1b
🔧 Installation

Clone the repository

bashgit clone https://github.com/yourusername/legal-document-summarizer.git
cd legal-document-summarizer

Create a virtual environment (recommended)

bashpython -m venv venv

# On Windows
venv\Scripts\activate

# On Linux/Mac
source venv/bin/activate

Install required packages

bashpip install -r requirements.txt
📦 Requirements
Create a requirements.txt file with:
txtgradio
langchain-ollama
requests
🎯 Usage

Start the application

bashpython app.py
```

2. **Access the interface**
   - The app will launch automatically in your default browser
   - Or manually navigate to: `http://localhost:7860`

3. **Analyze documents**
   - **Option 1**: Upload a legal document file
   - **Option 2**: Paste document text directly into the text box
   - Click "Analyze Document" to get results

## 💡 How It Works

1. **Input Processing**: The tool accepts either file uploads or direct text input
2. **Content Extraction**: Reads and processes the document content
3. **AI Analysis**: Passes the content to Gemma 3 LLM with specialized legal prompts
4. **Output Generation**: Returns a structured summary with:
   - Brief overview at the top
   - Detailed Do's section
   - Detailed Don'ts section

## 📝 Example Output
```
Summary:
This privacy policy outlines how Company X collects, uses, and protects user data...

DO's:
✓ Read and understand the privacy policy before using services
✓ Review your privacy settings regularly
✓ Contact support for data access requests
...

DON'Ts:
✗ Don't share your account credentials
✗ Don't ignore privacy setting updates
✗ Don't assume data is automatically deleted
...
🎨 Customization
Changing the Model
Edit the model_name variable in the code:
pythonmodel_name = "gemma3:1b"  # Change to your preferred model
Adjusting Temperature
Modify the temperature parameter for more creative/conservative outputs:
pythonllm = ChatOllama(model=model_name, temperature=0.2)  # Range: 0.0 to 1.0
⚠️ Important Notes

Not Legal Advice: This tool is for informational purposes only
Consult Professionals: Always consult a licensed attorney for legal decisions
AI Limitations: LLM outputs may not be 100% accurate
Privacy: Documents are processed locally; no data is sent to external servers
# Legal-Policy-Summariser
An intelligent legal document analysis tool that uses LLM (Large Language Model) to automatically summarize legal policies and documents into clear, actionable Do's and Don'ts. Built with Gradio UI for easy file uploads or direct text input.

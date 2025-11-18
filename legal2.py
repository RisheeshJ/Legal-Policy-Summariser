#legal policy/documents summariser into do's and donts
import gradio as gr
import requests
import base64
import webbrowser
from langchain_ollama import ChatOllama

model_name = "gemma3:1b"
llm = ChatOllama(model=model_name, temperature=0.2)

def legal_gen(user_document: str)-> str:
    prompt = f"""
act like a very experienced lawyer with years of experience and summarise the following legal document/legal policy
into detailed and clear do's and dont's, along with a short summary at the top, make sure you dont miss any point.
Note:1) if u think a document is not alegal policy document, just say:"its not a law related document"
2) dont write things like "i am not an lawyer" , "consult a real lawyer" or "do u want to elaborate"etc at the end, 
just give summary and do's and dont's as i have mentioned.
{user_document}
"""
    result=llm.invoke(prompt).content.strip()
   
    return result

def process_input(file, text_input):
    """Process either uploaded file or text input"""
    document_content = ""
    
    # Check if file is uploaded
    if file is not None:
        try:
            with open(file.name, 'r', encoding='utf-8') as f:
                document_content = f.read()
        except Exception as e:
            return f"Error reading file: {str(e)}"
    
    # Check if text is provided
    elif text_input and text_input.strip():
        document_content = text_input.strip()
    
    else:
        return "Please either upload a file or enter text in the text box."
    
    # Generate summary using the legal_gen function
    try:
        summary = legal_gen(document_content)
        return summary
    except Exception as e:
        return f"Error generating summary: {str(e)}"

# Create Gradio interface
with gr.Blocks(title="Legal Document Summarizer") as demo:
    gr.Markdown("# Legal Document Summarizer")
    gr.Markdown("Upload a legal document/policy OR paste text directly to get a detailed summary with Do's and Don'ts")
    
    with gr.Row():
        with gr.Column():
            file_input = gr.File(
                label="Upload Legal Document (Optional)",
                file_types=[".txt", ".pdf", ".doc", ".docx"],
                type="filepath"
            )
            
            text_input = gr.Textbox(
                label="Or Paste Document Text Here (Optional)",
                lines=10,
                placeholder="Paste your legal document or policy text here..."
            )
            
            submit_btn = gr.Button("Analyze Document", variant="primary")
        
        with gr.Column():
            output = gr.Textbox(
                label="Summary with Do's and Don'ts",
                lines=20,
                max_lines=30,
                show_copy_button=True
            )
    
    submit_btn.click(
        fn=process_input,
        inputs=[file_input, text_input],
        outputs=output
    )
    
    gr.Markdown("### Note: This tool uses AI to analyze legal documents. For critical decisions, always consult a licensed attorney.")

# Launch the interface
if __name__ == "__main__":
    demo.launch()
import gradio as gr
from app.tutor import IndianCurriculumTutor
from app.config import Config

config = Config()

def create_interface():
    tutor = IndianCurriculumTutor()

    with gr.Blocks(title="Indian Curriculum Tutor", theme="soft") as interface:
        gr.Markdown(f"""
        ## 📘 {config.pdf_path.split('/')[-1]} Tutor  
        **Model:** {config.model_name} ({config.api_provider.upper()})  
        **Embeddings:** {config.embedding_model}  
        **Device:** {config.device.upper()}
        """)
        question = gr.Textbox(label="Ask about the textbook", lines=3)
        submit = gr.Button("Get Answer", variant="primary")
        clear = gr.Button("Clear")
        output = gr.Textbox(label="Answer", lines=10, interactive=False)

        submit.click(tutor.answer_question, inputs=[question], outputs=[output])
        clear.click(lambda: ("", ""), outputs=[question, output])

    return interface
# 🇮🇳 Indian Curriculum PDF Tutor – Fixed Model Error Version

An AI-powered PDF Q&A Tutor built using Gradio + LangChain + HuggingFace + OpenAI/OpenRouter for Indian school textbooks (English/Hindi). It reads your textbook PDF and answers questions using a local vector store and cloud LLM.
## 🧠 Features
- 📘 PDF-based contextual Q&A (NCERT or state board books)
- 🧠 SentenceTransformer + FAISS for multilingual search
- 💬 GPT (OpenAI or OpenRouter) for answer generation
- 🌐 Gradio interface for interactive Q&A
- 🛠️ Easy to switch between GPU/CPU

## 📂 Project Structure
indian-curriculum-tutor/
├── app/                  # Core logic (LLM, embeddings, PDF, config)
├── interface/            # Gradio UI
├── data/                 # Your curriculum PDF (e.g., iemh101.pdf)
├── .env                  # API keys & settings (DO NOT COMMIT)
├── run.py                # Entry point to start the app
├── requirements.txt      # Dependencies
└── README.md             # You're reading it now
## ✅ Setup Instructions
### 1. 🔁 Clone or Download
git clone https://github.com/arjunaraoj/indian-curriculum-tutor.git
cd indian-curriculum-tutor
### 2. 📦 Install Dependencies
Make sure you have Python 3.8+ and `pip` installed.
pip install -r requirements.txt
### 3. 🔐 Configure API Keys
Create a `.env` file in the root folder:
PDF_PATH=data/iemh101.pdf
# Option 1: OpenAI (default)
API_PROVIDER=openai
OPENAI_API_KEY=sk-xxxxxxx
MODEL_NAME=gpt-3.5-turbo

# Option 2: OpenRouter (optional)
# API_PROVIDER=openrouter
# OPENROUTER_API_KEY=your_openrouter_key
# MODEL_NAME=mistralai/mixtral-8x7b-instruct
### 4. 📄 Add Your PDF

Place your curriculum PDF in the `data/` folder. For example:
data/iemh101.pdf
Update the `PDF_PATH` in your `.env` file accordingly.
### 5. 🚀 Launch the Application
Run the app:
python run.py
It will start the tutor on:
http://localhost:7865

## 🖼️ UI Preview
Once running, you’ll see:

- A PDF title and model info
- A textbox to enter your question
- A generated academic answer using GPT
## 🔄 Example Q&A

**Q:** _"Explain Newton’s First Law in simple words"_

**A:**  
> Newton's First Law says that if something is not moving, it will stay still, and if it’s moving, it will keep moving unless something stops it.  
> **Example**: A football stays still unless you kick it.

## 🧠 How It Works

| Step               | Tech Used                                  |
|--------------------|---------------------------------------------|
| PDF Parsing        | `PyPDFLoader` from `langchain_community`    |
| Text Chunking      | `RecursiveCharacterTextSplitter`            |
| Embeddings         | `HuggingFaceEmbeddings` (multilingual)      |
| Vector Store       | `FAISS`                                     |
| LLM Connection     | `ChatOpenAI` (OpenAI or OpenRouter)         |
| UI                 | `Gradio`                                     |

## 💡 Tips

- Use `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` for Indian languages
- Switch to OpenRouter if OpenAI quota is exceeded
- Increase chunk size or overlap for better accuracy
## 🛠️ Troubleshooting

- ❌ **PDF not found** → Check `PDF_PATH` in `.env`
- ❌ **Model not supported** → Use correct model format:
  - OpenAI: `gpt-3.5-turbo`, `gpt-4`
  - OpenRouter: `provider/model` like `mistralai/mixtral-8x7b-instruct`
- ❌ **CUDA error** → Fall back to CPU by setting `device = cpu`
## 📜 License
MIT License – Use freely with attribution.

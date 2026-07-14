# 📚 Smart Study Buddy

**Smart Study Buddy** is an AI-powered study assistant that transforms PDF study notes into an interactive learning experience. Students can upload their notes, ask questions based specifically on the uploaded content, and automatically generate revision flashcards.

The project uses a **Retrieval-Augmented Generation (RAG)** workflow to retrieve relevant information from uploaded notes before generating an answer.

---

## ✨ Features

### 📄 PDF Notes Upload

Upload study materials in PDF format and automatically extract the text for processing.

### 💬 AI-Powered Notes Q&A

Ask questions about the uploaded notes and receive answers grounded in the document content.

### 🔍 Semantic Search

The application converts text chunks into vector embeddings and retrieves the most relevant sections for each question.

### 🃏 AI Flashcard Generator

Automatically generate concise question-and-answer flashcards from uploaded notes for quick revision.

### 📚 Source Transparency

View the sections of the uploaded notes that were retrieved to generate an answer.

### 🌙 Light & Dark Mode

Switch between light and dark themes for a comfortable study experience.

### 🎨 Modern User Interface

A responsive Streamlit interface featuring pastel and vibrant gradients, elevated cards, modern spacing, and interactive components.

---

## 🧠 How It Works

```text
Upload PDF
    ↓
Extract Text
    ↓
Split Text into Chunks
    ↓
Generate Vector Embeddings
    ↓
Store Embeddings in ChromaDB
    ↓
User Asks a Question
    ↓
Retrieve Relevant Chunks
    ↓
Send Context + Question to Gemini
    ↓
Generate a Notes-Based Answer
```

This approach is known as **Retrieval-Augmented Generation (RAG)**.

---

## 🛠️ Tech Stack

| Technology                      | Purpose                                                  |
| ------------------------------- | -------------------------------------------------------- |
| Python                          | Core programming language                                |
| Streamlit                       | Web application interface                                |
| LangChain                       | AI application and RAG workflow                          |
| Google Gemini                   | Large Language Model for answer and flashcard generation |
| Google Generative AI Embeddings | Converts text into vector embeddings                     |
| ChromaDB                        | Vector database for semantic retrieval                   |
| PyPDF                           | Extracts text from uploaded PDF documents                |
| python-dotenv                   | Secure environment variable management                   |

---

## 📁 Project Structure

```text
Smart-study-buddy/
│
├── app.py
│
├── requirements.txt
├── README.md
├── .gitignore
│
└── utils/
    ├── pdf_loader.py
    ├── text_splitter.py
    ├── vector_store.py
    ├── retriever.py
    └── llm.py
```

### File Responsibilities

* **`app.py`** — Main Streamlit application and user interface.
* **`pdf_loader.py`** — Extracts text from uploaded PDF files.
* **`text_splitter.py`** — Divides large documents into manageable chunks.
* **`vector_store.py`** — Generates embeddings and stores them in ChromaDB.
* **`retriever.py`** — Retrieves the most relevant document chunks.
* **`llm.py`** — Configures and initializes the Gemini language model.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/mythilyparise/Smart-study-buddy.git
```

```bash
cd Smart-study-buddy
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```text
GOOGLE_API_KEY=your_google_api_key_here
```

> ⚠️ Never upload your `.env` file or API keys to GitHub.

The `.env` file is excluded through `.gitignore`.

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🚀 Usage

1. Select a subject from the sidebar.
2. Upload your study notes as a PDF.
3. Wait for the notes to be processed.
4. Use **Ask Your Notes** to ask document-based questions.
5. View the retrieved source sections used for the answer.
6. Open **Generate Flashcards** to create revision cards.
7. Choose the number of flashcards you want.
8. Switch between light and dark modes according to your preference.

---

## 🔒 Grounded AI Responses

Smart Study Buddy is designed to answer questions using the uploaded notes as context.

If the required information cannot be found in the provided notes, the application is instructed to respond:

> *I couldn't find that information in the uploaded notes.*

This helps reduce unsupported answers and keeps the learning experience focused on the student's study material.

---

## 🌟 Future Enhancements

* 📝 AI-generated quizzes and MCQs
* 📊 Student progress tracking
* 💾 Persistent study sessions
* 📚 Multiple PDF support
* 🔊 Text-to-speech revision
* 🧠 Difficulty-based flashcards
* 📥 Flashcard export
* 🔐 User authentication
* ☁️ Cloud deployment
* 📱 Mobile-friendly improvements

---

## 🎯 Project Objective

The objective of Smart Study Buddy is to make studying more interactive and efficient by combining document understanding, semantic search, retrieval, and generative AI.

Instead of manually searching through lengthy notes, students can interact directly with their study material and generate useful revision resources.

---

## 👩‍💻 Author

**Mythily Parise**

B.Tech Computer Science Engineering — Artificial Intelligence & Machine Learning

GitHub: `mythilyparise`

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

**Learn smarter. Revise faster. Study with AI. 📚✨**

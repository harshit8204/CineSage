# 🎬 CineSage

An AI-powered movie information extraction tool that uses LangChain and Mistral AI to parse structured movie data from unstructured text paragraphs. Available as both a CLI tool and a Streamlit web app.

---

## ✨ Features

- **Structured Extraction** — Automatically extracts movie title, release year, genre(s), director, cast, rating, and summary from free-form text
- **Pydantic Validation** — Uses a strongly-typed `Movie` schema to ensure clean, consistent output
- **Dual Interface** — Run it from the command line (`core.py`) or via a browser UI (`UIcore.py`)
- **Multi-Provider Support** — Dependencies include OpenAI, Groq, Google Gemini, Mistral, and HuggingFace for flexible model swapping
- **Embeddings Ready** — Includes embedding scripts for vector search use cases

---

## 🗂️ Project Structure

```
CineSage/
├── core.py                  # CLI: extract movie info from a paragraph
├── UIcore.py                # Streamlit UI version
├── embeddings.py            # OpenAI-based text embeddings
├── huggingface_embedding.py # HuggingFace-based text embeddings
└── requirements.txt         # Python dependencies
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/harshit8204/CineSage.git
cd CineSage
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
MISTRAL_API_KEY=your_mistral_api_key_here
# Add other keys as needed:
# OPENAI_API_KEY=...
# GROQ_API_KEY=...
# GOOGLE_API_KEY=...
```

---

## 🖥️ Usage

### CLI Mode

```bash
python core.py
```

You'll be prompted to enter a paragraph about a movie. The app will extract and print structured information.

**Example input:**
```
The Dark Knight, directed by Christopher Nolan and released in 2008, is a superhero thriller 
starring Christian Bale and Heath Ledger. It holds an IMDb rating of 9.0 and follows Batman 
as he battles the anarchic Joker in Gotham City.
```

**Example output:**
```json
{
  "title": "The Dark Knight",
  "release_year": 2008,
  "genre": ["Action", "Crime", "Drama"],
  "director": "Christopher Nolan",
  "cast": ["Christian Bale", "Heath Ledger"],
  "rating": 9.0,
  "summary": "Batman battles the anarchic Joker in Gotham City."
}
```

### Streamlit Web App

```bash
streamlit run UIcore.py
```

Open `http://localhost:8501` in your browser, paste a movie paragraph, and click **Analyze**.

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| LLM | Mistral AI (`mistral-small-2506`) |
| Framework | LangChain |
| Output Parsing | Pydantic + `PydanticOutputParser` |
| UI | Streamlit |
| Embeddings | OpenAI / HuggingFace |
| Config | python-dotenv |

---

## 📦 Dependencies

```
langchain
langchain-mistralai
langchain-openai
langchain-google-genai
langchain-community
langchain_huggingface
mistralai
openai
groq
google-generativeai
pydantic
python-dotenv
tiktoken
ipykernel
```

---

## 👤 Author

**Harshit** — [@harshit8204](https://github.com/harshit8204)

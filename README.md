# 💡 QuoteSense — AI-Powered Quote Recommender

An intelligent web application that recommends meaningful quotes using **AI-powered semantic search** and **vector embeddings with Endee Vector Database**.

---

## 🎯 Project Overview

QuoteSense is a real-world AI application that:

- 🧠 Understands user intent using Natural Language Processing (NLP)  
- 🔍 Recommends quotes based on **meaning (not keywords)**  
- ⚡ Uses vector embeddings for semantic similarity  
- 📦 Stores and retrieves data using Endee Vector Database  
- 🌐 Provides fast and interactive web experience  

---

## 🏗️ System Architecture

```
User Input (Natural Language)
│
▼
┌──────────────────────────────┐
│ Sentence Transformer Model │
│ (all-MiniLM-L6-v2)         │
│ → Converts text to vectors │
└──────────────┬───────────────┘
│
▼
┌──────────────────────────────┐
│ Endee Vector Database      │
│ - Stores quote embeddings  │
│ - Performs similarity search│
└──────────────┬───────────────┘
│
▼
┌──────────────────────────────┐
│ FastAPI Backend            │
│ - Handles API requests     │
│ - Returns top matches      │
└──────────────┬───────────────┘
│
▼
┌──────────────────────────────┐
│ Web Frontend               │
│ HTML + CSS + JavaScript    │
│ Displays quotes + similarity│
└──────────────────────────────┘
```

---

## 🚀 Features

### 🔹 Core Functionality

- 🔍 **Semantic Search** – Understands meaning, not just keywords  
- 🤖 **AI Recommendations** – Powered by Sentence Transformers  
- ⚡ **Fast API Backend** – Built with FastAPI  
- 📦 **Vector Database** – Endee integration  
- 🎯 **Context-Aware Results** – Based on user intent  
- 🎨 **Interactive UI** – Clean and responsive frontend  

### 🔹 Technical Highlights

- 🧠 NLP-based intelligent recommendation system  
- ⚡ Real-time semantic similarity search  
- 📊 Displays similarity score for each quote  
- 🔄 Auto indexing at startup  
- 🧹 Data preprocessing using Pandas  

---

## 🛠️ Tech Stack

| Component        | Technology              | Purpose                |
|-----------------|------------------------|------------------------|
| Backend         | FastAPI                | API handling           |
| Embeddings      | Sentence Transformers  | Text → Vector          |
| Vector DB       | Endee                  | Storage & search       |
| Frontend        | HTML, CSS, JavaScript  | User Interface         |
| Data Processing | Pandas                 | CSV handling           |

---

## 📋 Prerequisites

- Python 3.9+
- Docker
- Git

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Kabilroy/Semantic-Quote-Recommender-Endee.git
cd quotesense
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Endee Vector Database

```bash
docker run -d -p 8080:8080 endeeio/endee-server:latest
```

### 4️⃣ Run Backend

```bash
uvicorn backend.main:app --reload
```

### 5️⃣ Open Application

Navigate to your browser and open:

```
http://127.0.0.1:8000
```

---

## 🔍 How to Search Quotes

1. Open the web application in your browser
2. Enter natural language queries in the search box
3. Get AI-recommended quotes instantly

### 📝 Example Queries

- "I feel sad"
- "Need motivation"
- "Advice for life"
- "Feeling lost and confused"
- "How to succeed"

---

## 📊 How It Works

1. **Load Quotes** – Quotes are loaded from CSV dataset
2. **Create Embeddings** – Converted into embeddings using Sentence Transformers
3. **Store in Vector DB** – Stored in Endee vector database
4. **User Query** – User query is converted into embedding
5. **Similarity Search** – Top similar quotes are retrieved using vector similarity
6. **Display Results** – Quotes are ranked by similarity score and displayed

---

## 📁 Project Structure

```
quote-recommender/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── utils.py             # Utility functions
│   ├── index.html           # Frontend HTML
│   ├── style.css            # Frontend CSS
│   └── script.js            # Frontend JavaScript
│
├── data/
│   └── quotes.csv           # Quote dataset
│
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 📊 Example Output

### Query:
```
"I feel sad"
```

### Result:
```
"Life is what happens when you're busy making other plans."
— John Lennon (82% match)

"In the middle of difficulty lies opportunity."
— Albert Einstein (78% match)

"Everything you want is on the other side of fear."
— George Addair (75% match)
```

---

## 🎯 Use Cases Demonstrated

✅ Semantic Search (NLP-based)  
✅ Vector Similarity Search  
✅ AI Recommendation System  
✅ Real-world AI Web Application  
✅ Endee Vector Database Integration  

---

## 🚀 Future Improvements

- 🔍 Filter by tags (motivation, life, etc.)
- 🎨 Advanced UI (cards, animations)
- 🌐 Cloud deployment (Render / Vercel)
- 📱 Mobile responsiveness
- 🔊 Voice-based input
- 💾 User favorites/bookmarking
- 🌙 Dark mode support

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

This project is for educational purposes.

---

## 👩‍💻 Author

**KABILAN P**

---

## 📞 Support

If you encounter any issues, please:

1. Check the GitHub Issues section
2. Review the installation steps
3. Ensure Docker and all dependencies are properly installed
4. Check that Endee Vector Database is running on port 8080

---

## 🔗 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Sentence Transformers](https://www.sbert.net/)
- [Endee Vector Database](https://endee.io/)
- [Pandas Documentation](https://pandas.pydata.org/)

---

**Happy Quote Hunting! 🎯✨**

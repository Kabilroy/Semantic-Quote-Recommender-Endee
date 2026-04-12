## 💡 QuoteSense — AI-Powered Quote Recommender

Built using FastAPI, Sentence Transformers, and **Endee Vector Database** for intelligent semantic quote recommendations

---

## ✨ Features

| Feature                  | Description                                                           |
| ------------------------ | --------------------------------------------------------------------- |
| 🔍 Semantic Search       | Natural language queries — understands meaning, not just keywords     |
| 🤖 AI Recommendations    | Uses Sentence Transformers to find contextually similar quotes        |
| 📦 Vector Database       | Stores embeddings efficiently using **Endee DB** for fast retrieval   |
| ⚡ Fast API Backend       | Built with FastAPI for high performance and real-time responses       |
| 🎯 Context-Aware Results | Returns quotes based on emotions, intent, and meaning                 |
| 🎨 Clean Web UI          | Simple and interactive interface using HTML, CSS, and JavaScript      |
| 📊 Similarity Score      | Displays relevance score for each recommended quote                   |
| 🔄 Auto Indexing         | Automatically loads and embeds quotes into Endee at startup           |
| 🧹 Data Cleaning         | Handles CSV formatting, missing values, and column normalization      |
| 🧠 NLP-Based System      | Demonstrates real-world Natural Language Processing (NLP) application |

---

## 🏗️ Architecture

```
User Query (natural language)
        │
        ▼
┌──────────────────────────┐
│ Sentence Transformer     │
│ (all-MiniLM-L6-v2)       │
│ → Converts text to vector│
└──────────┬───────────────┘
           │ query embedding
           ▼
┌──────────────────────────┐
│        Endee DB          │
│   Vector Database        │
│  - Stores quote vectors  │
│  - Uses cosine similarity│
└──────────┬───────────────┘
           │ ranked results
           ▼
┌──────────────────────────┐
│      FastAPI Backend     │
│  - Handles API requests  │
│  - Returns top matches   │
└──────────┬───────────────┘
           │ JSON response
           ▼
┌──────────────────────────┐
│     Web Frontend         │
│ HTML + CSS + JS          │
│ Displays quotes + score  │
└──────────────────────────┘
```

---

## 🛠️ Tech Stack

| Component       | Technology            | Purpose                         |
| --------------- | --------------------- | ------------------------------- |
| Backend         | FastAPI               | High-performance API handling   |
| Embeddings      | Sentence Transformers | Converts text to vectors        |
| Vector DB       | **Endee DB**          | Stores and retrieves embeddings |
| Frontend        | HTML, CSS, JavaScript | User interface                  |
| Data Processing | Pandas                | CSV handling and preprocessing  |

---

## 🎯 Usage Example

**Query:**

```
"I feel sad"
```

**Result:**

```
"Life is what happens when you're busy making other plans."
— John Lennon (82% match)
```

---

## 📁 Project Structure

```
quote-recommender/
├── backend/
│   ├── main.py
│   ├── utils.py
│   ├── index.html
│   ├── style.css
│   ├── script.js
│
├── data/
│   └── quotes.csv
│
├── requirements.txt
└── README.md
```

---

## 🚀 Key Highlights

* Uses AI + NLP instead of keyword matching
* Demonstrates real-world vector search using **Endee DB**
* Clean separation of frontend + backend
* Scalable design using vector databases

---

## 📌 Future Improvements

* 🔍 Filter by tags (using Endee `$in` operator)
* 📊 Range filtering (using `$range`)
* 🎨 Advanced UI design (cards, animations)
* 🌐 Deploy as a live web app
* 📱 Mobile responsiveness
* 🔊 Voice-based query input

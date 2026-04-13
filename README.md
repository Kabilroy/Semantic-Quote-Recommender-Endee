## 💡 QuoteSense — AI-Powered Quote Recommender

QuoteSense is an intelligent web application that recommends meaningful quotes based on user input using **AI-powered semantic search**. Instead of simple keyword matching, it understands the *context and intent* of the query to deliver relevant and inspiring quotes.

---

## 🚀 Features

* 🔍 Semantic search based on meaning (not just keywords)
* 🤖 AI-powered recommendations using Sentence Transformers
* ⚡ Fast backend built with FastAPI
* 📦 Vector database using ChromaDB
* 🎨 Simple and interactive web interface
* 📊 Displays similarity score for each quote

---

## 🛠️ Tech Stack

* **Backend:** FastAPI (Python)
* **AI Model:** Sentence Transformers (`all-MiniLM-L6-v2`)
* **Database:** ChromaDB (Vector DB)
* **Frontend:** HTML, CSS, JavaScript
* **Libraries:** Pandas, Uvicorn

---

## 📂 Project Structure

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

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/quotesense.git
cd quotesense
```

---

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Run the application

```
uvicorn backend.main:app --reload
```

---

### 4️⃣ Open in browser

```
http://127.0.0.1:8000
```

---

## 📊 How It Works

1. Quotes are loaded from a CSV file
2. Converted into vector embeddings using Sentence Transformers
3. Stored in ChromaDB (vector database)
4. User query is converted into embedding
5. Similar quotes are retrieved using vector similarity

---

## 🧪 Example Queries

* "I feel sad"
* "Need motivation"
* "Advice for life"
* "Success mindset"

---

## 📌 Future Improvements

* 🔍 Filter by tags and author
* 🎨 Improved UI/UX
* 🌐 Deployment to cloud
* 📱 Mobile-friendly design
* 🔊 Voice input support

---

## 🤝 Contributing

Feel free to fork this repository and contribute improvements!

---

## 📜 License

This project is for educational and personal use.

---

## 👩‍💻 Author

kabilan P

---

⭐ If you like this project, give it a star on GitHub!

### ✅ `README.md`

```markdown
# 🛒 Shopping List AI Agent

An AI-powered shopping list manager built with **LangGraph**, **LangChain**, and **Streamlit**.  
The agent interprets natural language commands to **add**, **remove**, and **view** items with quantities in a persistent `.json` file.

---

## 🚀 Features

- 💬 Natural language interaction with a function-calling LLM agent
- 🔁 Persistent memory using a local JSON file
- 🛠️ Tool-calling using LangChain-compatible tools
- 📊 Quantity-aware item management
- 🧠 Heuristics for “remove everything” requests (e.g., *"rimuovi tutto il latte"*)
- 🌐 Web UI via Streamlit
- 🐳 Fully containerized with Docker (port `8051`)

---

## 📁 Project Structure


progetto_aitho/
├── src/
│   ├── main.py         # Streamlit UI
│   ├── agent.py        # LLM & agent setup
│   ├── graph.py        # LangGraph graph setup
│   ├── memory.py       # JSON storage logic
│   ├── tools.py        # Tool definitions
├── requirements.txt    # Dependencies
├── Dockerfile          # Container setup
└── README.md           # Project instruction

```

---

## 🧑‍💻 Setup Instructions

### 🔧 Option 1: Run Locally

1. **Clone the repository**

```bash
git clone https://github.com/PieroFiorica/progetto_aitho.git
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set up your .env file**

```bash
 nano /src/.env_template
```

4. **Start the app**

```bash
streamlit run /src/main.py --server.port 8501
```

Then open your browser at: 
**[http://localhost:8501](http://localhost:8501)**

---

### 🐳 Option 2: Run with Docker

1. **Build the image**

```bash
docker build -t progetto_aitho .
```

2. **Run the container**

```bash
docker run -p 8051:8051 progetto_aitho 
```

Then open your browser at: 
**[http://localhost:8051](http://localhost:8051)**

---

## 🧠 Example Commands

You can type:

* `"aggiungi 3 mele"`
* `"rimuovi 2 gelati"`
* `"rimuovi tutto il latte"`
* `"mostra la lista"`

Or click the **📋 Visualizza Lista** button.

---

## 📝 Notes

* All shopping list data is stored in `shopping_list.json`
* Removing items down to quantity ≤ 0 will automatically delete them
* The app supports both singular and bulk item operations

---

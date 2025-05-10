# Streamlit Template App

A minimal, production-ready Streamlit application template with:

- 📁 File uploads
- 🗃 SQLite database logging
- 📦 Persistent file storage
- 🚀 Devcontainer support for VSCode
- 🧪 Ready for testing and type-checking

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/avar365/app_template.git
cd app_template
```

### 2. (Optional) Open in Devcontainer (VSCode)

Make sure you have the **Remote - Containers** extension installed in VSCode.  
Open the folder and click **"Reopen in Container"** when prompted.

### 3. Install dependencies (locally or in container)

```bash
pip install -r requirements.txt
```

---

## Run the App

```bash
streamlit run src/my_project/main.py
```

---

## Project Structure

```
.
├── src/
│   └── my_project/
│       ├── main.py           # Streamlit entrypoint
│       ├── db.py             # DB connection / logic
│       ├── file_handler.py   # File upload/delete logic
│       └── utils/            # Helper functions
├── uploads/                  # Persistent uploaded files
├── data/                     # SQLite DB or temp files
├── pyproject.toml
├── .gitignore
├── README.md
└── .devcontainer/
```

---

## Environment & Security

- All secrets should be managed via a `.env` file (not committed).
- The `.env.example` file shows required variables.
- No passwords or tokens in code. Ever.
- For CI/CD, consider GitHub Actions secrets and runtime env injection.

---

## TODOs

- [ ] Add unit tests
- [ ] Add mypy + ruff config
- [ ] Dockerfile for deployment
- [ ] CI pipeline (GitHub Actions)

---

## Author

Maintained by **Andreas** · [website](https://)

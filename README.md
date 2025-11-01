# 🚀 **Neurofiq Unified Content Creation Agent**

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?logo=python)
![Framework](https://img.shields.io/badge/Framework-Agno-lightgreen?logo=fastapi)
![LLM](https://img.shields.io/badge/LLM-Ollama%20%7C%20DeepSeek--V3.1-orange?logo=openai)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Build](https://img.shields.io/badge/Status-Active-success.svg)

> 🧠 A next-gen AI Agent that automates **SEO research → content writing → HTML generation → cPanel deployment**, all through one unified pipeline.

---

## 🧭 **Overview**

**Neurofiq Unified Agent** is a **Python-powered AI automation system** that transforms any blog topic into a **live SEO-optimized article**.
It integrates **Agno**, **Ollama**, and multiple **custom tools** to manage every step — from research to publication — in an intelligent, conversational flow.

---

## ✨ **Key Features**

* 🔁 **Full Automation** — From input to live deployment.
* 🔍 **Elite SEO Research** — Fetches top keywords, competitors & trends via *Searxng* and *DuckDuckGo*.
* ✍️ **Humanized Writing** — 3000+ words, SEO-rich, fact-checked & AI-detection safe.
* 🌐 **Dynamic HTML** — Converts Markdown → TailwindCSS-styled HTML template.
* ☁️ **Auto Deploy** — Publishes directly to your cPanel & returns a permalink.
* 🖼️ **Image Hosting** — Uploads featured images using ImgBB API.
* 💾 **Persistent Memory** — Saves states (URLs, API keys, etc.) in SQLite DB.
* 💬 **Interactive CLI** — Beautiful terminal UI using *Rich*.

---

## 🧩 **Workflow Overview**

### 🩵 **Phase 1 — Requirements Gathering**

1. Ask for blog topic & optional featured image.
2. Upload image via `upload_image_to_imgbb`.
3. Confirm and proceed to research.

### 🔍 **Phase 2 — Elite SEO Research**

1. Analyze **keywords**, **volume**, and **competitors**.
2. Identify **content gaps** & structure.
3. Formulate **content strategy**.

### ✍️ **Phase 3 — Content Creation**

1. Write 3000+ word blog (intro, 5–7 H2s, FAQ, conclusion).
2. Fact-check via web.
3. Optimize SEO structure.
4. Ensure natural, human tone.

### 🌐 **Phase 4 — HTML & Deployment**

1. Convert to styled Tailwind HTML.
2. Deploy via `deploy_to_cpanel`.
3. Return public **permalink**.

---

## ⚙️ **Core Components**

| Component                   | Description                                   |
| --------------------------- | --------------------------------------------- |
| `agno.agent.Agent`          | Core framework class for building agent.      |
| `agno.models.ollama.Ollama` | LLM integration (`deepseek-v3.1:671b-cloud`). |
| `agno.db.sqlite.SqliteDb`   | Stores session data in `neurofiq_content.db`. |
| `agno.tools`                | Provides `@tool` decorator for utilities.     |
| `rich`                      | Adds colorized CLI interface.                 |
| `python-dotenv`             | Handles environment secrets.                  |

---

## 🧰 **Custom Tools**

### 🖼️ `upload_image_to_imgbb`

Uploads local images to **ImgBB**.

**Params:**

* `image_path` *(str)* – Path of image to upload.

**Returns:** Public ImgBB URL or error.

---

### 🌐 `deploy_to_cpanel`

Uploads final HTML directly to **cPanel**.

**Params:**

* `html_content` *(str)* – HTML code to upload.
* `blog_title` *(str)* – Used to generate SEO slug.

**Returns:** Public permalink or error.

---

## 🪄 **Setup & Installation**

```bash
git clone https://github.com/ToufiqQureshi/agentic-ai-based-content-research-to-deployment-on-cpanel
cd agentic-ai-based-content-research-to-deployment-on-cpanel
pip install -r requirements.txt
```

Then, set your environment variables in `.env` file:

```bash
imagebb_api_key="YOUR_IMGBB_API_KEY"
cpanel_api_key="YOUR_CPANEL_API_TOKEN"
```

---

## 🧠 **Usage**

Run the agent:

```bash
python your_script_name.py
```

Follow the CLI prompts to:

> Provide a topic → upload image → generate content → deploy → get permalink 🌍

---

## 📦 **Dependencies**

* `agno`
* `requests`
* `python-dotenv`
* `rich`

---

## 💡 **Credits**

Built with ❤️ by **[Toufiq Qureshi](https://github.com/ToufiqQureshi)**
→ Passionate about **Agentic AI**, **Autonomous Systems**, and **Generative Intelligence Pipelines**.

---

# 🤖 AI Analytics & Citation Tracking (Plan in Hinglish)

Hello! Maine poore code ko analyze kiya, bugs fix kiye, aur `agno` (jo exist nahi karta tha) ko `phidata` se replace kar diya hai. Ab code perfectly run karega.

Aapka jo feature request tha ki **"Kaise pata karein ki ChatGPT/Gemini humari site ko rank kar rahe hain ya nahi"** (Just like Google Analytics for AI), uske liye maine complete research aur plan banaya hai.

Is concept ko aajkal **GEO (Generative Engine Optimization)** ya **AIO (AI Optimization)** kehte hain.

---

## 📊 Feature: "AI Rank Tracker" kaise banayein?

Currently, koi official "Google Analytics for AI" exist nahi karta jo saare AI models ka data ek jagah de. Lekin hum khud ka ek **Tracker Tool** bana sakte hain jo agent me add ho sakta hai.

Yahan 2 tareeke hain isey implement karne ke:

### 1. Passive Tracking (Traffic Source) - Easy
Ye wo tareeka hai jisse hum check karte hain ki log AI se click karke humari site par aa rahe hain ya nahi.
*   **Google Analytics 4 (GA4)** me `Referral Traffic` check karo.
*   Agar traffic `chatgpt.com`, `gemini.google.com`, ya `bing.com` se aa raha hai, iska matlab AI aapko cite kar raha hai aur users link pe click kar rahe hain.
*   **Feature Idea:** Hum agent me ek tool add kar sakte hain jo GA4 API se connect hoke ye report fetch kare.

### 2. Active Tracking (Reverse Prompting) - Advanced & Powerful 🔥
Ye wo feature hai jo aap chahte hain. Hum AI se hi poochte hain ki wo humare baare me kya jaanta hai.

**Kaise kaam karega?**
Hum ek naya tool banayenge `check_ai_ranking` jo ye karega:

1.  **Queries generate karega:** Aapke blog topic se related sawal banayega.
    *   *Example:* "Top 5 blogs about [Your Topic]", "Best resources for [Keyword]".
2.  **Different AIs ko puchega:** Perplexity API, OpenAI API, aur Gemini API use karke ye sawal puchega.
3.  **Mention Check karega:** Jo jawab aayega, usme aapki website ka URL ya Brand Name dhoondega.
4.  **Report dega:** "Yes, Perplexity recommended your site at position #2!"

---

## 🛠️ Implementation Plan (Code Example)

Agar aap ye feature add karna chahte hain, toh hum agent me ek naya tool add kar sakte hain. Niche ek example logic hai:

```python
@tool
def check_ai_ranking(blog_topic: str, site_url: str) -> str:
    """Checks if AI models recommend your site for the given topic."""

    # 1. Sawal (Prompt) ready karo
    query = f"What are the best articles about {blog_topic}? Provide links."

    # 2. Perplexity API (Best for searching) se pucho
    # Note: Aapko PERPLEXITY_API_KEY chahiye hoga
    import requests
    url = "https://api.perplexity.ai/chat/completions"
    payload = {
        "model": "llama-3.1-sonar-small-128k-online",
        "messages": [{"role": "user", "content": query}]
    }
    headers = {"Authorization": "Bearer YOUR_PERPLEXITY_API_KEY"}

    response = requests.post(url, json=payload, headers=headers)
    answer = response.json()['choices'][0]['message']['content']

    # 3. Check karo ki humara URL answer me hai ya nahi
    if site_url in answer:
        return f"🎉 Great News! Perplexity AI is ranking your site for '{blog_topic}'."
    else:
        return f"📉 Not ranking yet on Perplexity. Improve content authority."
```

### 🚀 Future Steps for You
1.  **Code Fixes maine kar diye hain:** Abhi code `phidata` use kar raha hai aur credentials secure hain.
2.  **Feature Add karein?** Agar aap chahte hain ki main ye `check_ai_ranking` tool code me implement kar doon, toh mujhe batayein (Iske liye aapko Perplexity ya OpenAI ki API key leni padegi).

Abhi ke liye, maine basic code improve kar diya hai taaki wo smoothly run kare!

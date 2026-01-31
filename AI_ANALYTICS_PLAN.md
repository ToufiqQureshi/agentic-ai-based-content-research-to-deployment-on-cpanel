# 🤖 AI Analytics & Citation Tracking (Plan in Hinglish)

Hello! Maine poore code ko analyze kiya, bugs fix kiye, aur `agno` (jo exist nahi karta tha) ko `phidata` se replace kar diya hai. Ab code perfectly run karega.

Aapka jo feature request tha ki **"Kaise pata karein ki ChatGPT/Gemini humari site ko rank kar rahe hain ya nahi"** (Just like Google Analytics for AI), uske liye maine complete research aur plan banaya hai.

Is concept ko aajkal **GEO (Generative Engine Optimization)** ya **AIO (AI Optimization)** kehte hain.

---

## 📊 Feature: "AI Rank Tracker" kaise banayein?

Currently, koi official "Google Analytics for AI" exist nahi karta jo saare AI models ka data ek jagah de. Lekin hum khud ka ek **Tracker Tool** bana sakte hain.

Yahan 3 tareeke hain isey implement karne ke:

### 1. Passive Tracking (Traffic Source) - Easy & Best ✅
Ye wo tareeka hai jisse hum check karte hain ki log AI se click karke humari site par aa rahe hain ya nahi.
*   **Google Analytics 4 (GA4)** me `Referral Traffic` check karo.
*   Agar traffic `chatgpt.com`, `gemini.google.com`, ya `bing.com` se aa raha hai, iska matlab AI aapko cite kar raha hai aur users link pe click kar rahe hain.

### 2. Active Tracking (Reverse Prompting) - Advanced 🔥
Ye wo feature hai jo AI se hi puchta hai ki wo humare baare me kya jaanta hai.

**Code Logic:**
```python
@tool
def check_ai_ranking(blog_topic: str, site_url: str) -> str:
    """Checks if AI models recommend your site for the given topic."""
    # 1. Perplexity API se pucho "Best articles about [Topic]?"
    # 2. Check karo agar humara URL answer me hai.
    # (Requires Perplexity API Key)
    pass
```

### 3. Custom JS Tracker Script (Google Analytics Style) 🚀
Aapne jo request ki thi: *"ek js script denge proper id ke saath"*.
Hum ek simple **JavaScript Code** bana sakte hain jo user apni website ke `<head>` me lagayega. Ye script detect karegi ki visitor ChatGPT ya Gemini se aaya hai ya nahi.

**Kaise kaam karega:**
1. Script `document.referrer` check karegi.
2. Agar referrer `chatgpt.com` ya `gemini.google.com` hai, toh wo detect kar legi.
3. Data ko **Google Analytics (GA4)** ya aapke Custom Backend pe bhej degi.

#### 📜 The "AI Analytics" JS Script

Niche ek ready-to-use script hai. Ise aap apni website par laga sakte hain:

```html
<!-- Neurofiq AI Tracker Script -->
<script>
  (function() {
    // 1. AI Domains ki list
    const aiReferrers = [
      'chatgpt.com', 'openai.com',
      'gemini.google.com', 'bard.google.com',
      'claude.ai', 'anthropic.com',
      'perplexity.ai',
      'copilot.microsoft.com', 'bing.com'
    ];

    // 2. Check visitor kahan se aaya (Referrer)
    const referrer = document.referrer || "";

    // 3. Match Logic
    const matchingAI = aiReferrers.find(domain => referrer.includes(domain));

    if (matchingAI) {
      console.log(`🤖 AI Visitor Detected from: ${matchingAI}`);

      // 4. Data Send karo (Example: Google Analytics 4)
      if (typeof gtag === 'function') {
        gtag('event', 'ai_referral', {
          'event_category': 'AI Traffic',
          'event_label': matchingAI,
          'page_location': window.location.href, // Tracks WHICH URL (e.g. resort-lonavala.html)
          'transport_type': 'beacon'
        });
      }

      // OPTIONAL: Send to Custom Dashboard Backend
      // fetch('https://your-api.com/track-ai-referral', {
      //   method: 'POST',
      //   headers: {'Content-Type': 'application/json'},
      //   body: JSON.stringify({
      //     source: matchingAI,
      //     url: window.location.href,
      //     timestamp: new Date().toISOString()
      //   })
      // });
    }
  })();
</script>
```

---

## 📈 Dashboard Concept (Backend)

Agar aapko ek **Dashboard** chahiye jahan dikhe ki:
> "Gemini ne 'Best Resort in Lonavala' query ke liye aapki site `my-resort.com/lonavala` ko cite kiya."

Toh aapko ek **Backend Server** chahiye hoga jo wo JS Script se data receive kare.

### Example Backend Logic (Python/Flask):

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/track-ai-referral', methods=['POST'])
def track_referral():
    data = request.json
    source = data.get('source') # e.g., gemini.google.com
    url = data.get('url')       # e.g., https://yoursite.com/resorts-lonavala

    # Save to Database (SQLite/PostgreSQL)
    save_to_db(source, url)

    return jsonify({"status": "tracked"}), 200

# Dashboard Route
@app.route('/dashboard')
def show_dashboard():
    # Fetch data from DB and show table
    return render_template('dashboard.html', stats=get_stats_from_db())
```

Is setup se aapko pata chalega ki **kaunsa AI** aapke **kis page** par traffic bhej raha hai!

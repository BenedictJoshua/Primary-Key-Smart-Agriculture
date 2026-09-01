import json
import os
import random
import re
import urllib.request
import urllib.error
from datetime import datetime

# ------------------------------------------------------------
# HF API TOKEN
# Set this via environment variable, NOT hardcoded in the file.
#   Linux/macOS:  export HF_API_TOKEN="hf_xxxxxxxxxxxxxxxx"
#   Windows CMD:  set HF_API_TOKEN=hf_xxxxxxxxxxxxxxxx
#   Windows PS:   $env:HF_API_TOKEN="hf_xxxxxxxxxxxxxxxx"
# ------------------------------------------------------------
HF_FREE_API_TOKEN = os.environ.get("HF_API_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"


def web_answer(question):
    """
    Search the web (DuckDuckGo, no API key needed) and return a direct answer
    built from the top result, so the bot can answer current-events/factual
    questions on its own.
    """
    try:
        from duckduckgo_search import DDGS
    except ImportError:
        try:
            from ddgs import DDGS
        except ImportError:
            return None

    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(question, max_results=3))
    except Exception:
        return None

    if not results:
        return None

    top = results[0]
    snippet = top.get("body", "").strip()
    if not snippet:
        return None

    # Trim to a clean, direct-sounding answer (first sentence or two)
    sentences = re.split(r"(?<=[.!?])\s+", snippet)
    answer = " ".join(sentences[:2]).strip()
    return answer


def ask_ai(question):
    """Fallback to a real AI model for anything the rule-based bot can't answer."""
    if not HF_FREE_API_TOKEN:
        return ("I don't have a specific answer for that, and my AI fallback isn't "
                "configured (HF_API_TOKEN is not set).")

    payload = {
        "inputs": (
            "You are a helpful assistant. Answer the question clearly and briefly. "
            f"Question: {question}"
        ),
        "parameters": {
            "max_new_tokens": 150,
            "temperature": 0.3,
            "return_full_text": False
        }
    }

    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {HF_FREE_API_TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "PrimaryKey-SmartAgri/1.0"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            result = json.loads(response.read().decode("utf-8"))

            if isinstance(result, list) and len(result) > 0:
                return result[0].get("generated_text", "").strip() or "I'm not sure how to answer that."

            if isinstance(result, dict) and "error" in result:
                if "estimated_time" in result:
                    wait = result.get("estimated_time", 20)
                    return f"My AI brain is warming up. Try again in about {wait:.0f} seconds."
                return f"AI Error: {result['error']}"

            return "I'm not sure how to answer that."

    except urllib.error.HTTPError as e:
        return f"AI request failed (HTTP {e.code}). Please try again."
    except urllib.error.URLError as e:
        return f"AI request failed: could not reach the server ({e.reason})."
    except Exception as e:
        return f"AI request failed: {e}"


class SmartAgriBot:
    def __init__(self):
        # ---------------------------------------------------------
        # Casual / small-talk responses so the bot feels conversational
        # ---------------------------------------------------------
        self.greetings = {
            "hi": ["Hi there! How can I help you with your farming today?",
                   "Hello! What would you like to know about your crops?"],
            "hello": ["Hello! How can I assist you today?",
                      "Hi! Ready to help with your farming questions."],
            "hey": ["Hey! What's on your mind?"],
            "good morning": ["Good morning! Hope your fields are doing well today."],
            "good afternoon": ["Good afternoon! How can I help?"],
            "good evening": ["Good evening! What can I do for you?"],
        }

        self.how_are_you = [
            "I'm doing well, thank you for asking! How are you?",
            "I'm good, thanks! How about you?",
        ]

        self.thanks = [
            "You're welcome! Let me know if you need anything else.",
            "Happy to help! Feel free to ask more questions.",
        ]

        self.farewells = [
            "Goodbye! Wishing you a great harvest.",
            "Take care! Come back anytime you need farming advice.",
        ]

        self.identity = (
            "I'm the Smart Agriculture Assistant from Team Primary Key. "
            "I can help with crop recommendations, fertilizers, soil fertility, "
            "irrigation, pest management — and I can also answer general questions."
        )

        self.fertilizer_tips = {
            "paddy": "Use urea, DAP, and potash in split doses for better paddy yield.",
            "rice": "Apply nitrogen-rich fertilizers such as urea along with phosphorus and potassium.",
            "cotton": "Use NPK 80:40:40 and add organic compost for improved soil health.",
            "maize": "Apply nitrogen-rich fertilizers such as urea and phosphorus during early growth stages.",
        }

    # ---------------------------------------------------------
    # Simple local crop recommendation using NPK values
    # ---------------------------------------------------------
    def recommend_crop(self, text):
        n = re.search(r"N\s*=\s*(\d+)", text, re.IGNORECASE)
        p = re.search(r"P\s*=\s*(\d+)", text, re.IGNORECASE)
        k = re.search(r"K\s*=\s*(\d+)", text, re.IGNORECASE)

        if not (n and p and k):
            return None

        n = int(n.group(1))
        p = int(p.group(1))
        k = int(k.group(1))

        if n > 80 and p > 40 and k > 40:
            return "Rice is the most suitable crop for this soil profile."
        elif n > 60 and p > 30:
            return "Maize is a suitable crop for this soil profile."
        elif k > 50:
            return "Cotton may perform well in this soil profile."
        else:
            return "Groundnut or pulses may be suitable for this soil profile."

    # ---------------------------------------------------------
    # A few "utility" questions worth answering locally,
    # instantly, without hitting the AI model
    # ---------------------------------------------------------
    def handle_utility(self, q):
        if re.search(r"\bwhat.*time.*\b|\bcurrent time\b", q):
            return f"The current time is {datetime.now().strftime('%I:%M %p')}."

        if re.search(r"\bwhat.*date.*\b|\btoday.*date\b", q):
            return f"Today's date is {datetime.now().strftime('%B %d, %Y')}."

        return None

    # ---------------------------------------------------------
    # Main response engine
    # ---------------------------------------------------------
    def get_response(self, query):
        q = query.lower().strip()

        # ---- Small talk -----------------------------------------
        if re.search(r"\bhow are you\b|\bhow r u\b|\bhow're you\b", q):
            return random.choice(self.how_are_you)

        if re.search(r"\bwho are you\b|\bwhat are you\b|\bwhat can you do\b", q):
            return self.identity

        if re.search(r"\bthank(s| you)?\b", q):
            return random.choice(self.thanks)

        if re.search(r"\bbye\b|\bgoodbye\b|\bsee you\b|\btake care\b", q):
            return random.choice(self.farewells)

        for greeting, responses in self.greetings.items():
            if re.search(rf"\b{re.escape(greeting)}\b", q):
                return random.choice(responses)

        # ---- Quick utility answers (time/date) -------------------
        utility_result = self.handle_utility(q)
        if utility_result:
            return utility_result

        # ---- Crop recommendation from NPK values ------------------
        crop_result = self.recommend_crop(query)
        if crop_result:
            return crop_result

        # ---- Fertilizer advice -------------------------------------
        for crop, advice in self.fertilizer_tips.items():
            if crop in q:
                return advice

        # ---- General farming knowledge ------------------------------
        if "rainy season" in q or "monsoon" in q:
            return "Rice, maize, and groundnut are commonly recommended crops for the rainy season."

        if "soil fertility" in q:
            return "Improve soil fertility by adding compost, farmyard manure, green manure crops, and balanced NPK fertilizers."

        if "pest" in q or "aphid" in q:
            return "Use neem oil spray, maintain field sanitation, and apply recommended biopesticides for aphid control."

        if "water" in q or "irrigation" in q:
            return "Use drip irrigation where possible and irrigate early morning or evening to reduce water loss."

        # ---- Nothing matched locally -> try a live web search first --
        result = web_answer(query)
        if result:
            return result

        # ---- Fall back to the AI model if search found nothing -------
        return ask_ai(query)


# -------------------------------------------------------------
# Interactive Console
# -------------------------------------------------------------
def main():
    bot = SmartAgriBot()

    print("============================================================")
    print("   TEAM PRIMARY KEY - SMART AGRICULTURE AI ASSISTANT")
    print("============================================================")
    if not HF_FREE_API_TOKEN:
        print("NOTE: HF_API_TOKEN is not set, so general (non-farming)")
        print("      questions will not be answered by the AI model.")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            user_input = input("You: ").strip()

            if user_input.lower() == "exit":
                print("Exiting Smart Agriculture AI Assistant...")
                break

            if not user_input:
                continue

            response = bot.get_response(user_input)

            print("\nBot:")
            print(response)
            print("------------------------------------------------------------\n")

        except KeyboardInterrupt:
            print("\nSession interrupted.")
            break


if __name__ == "__main__":
    main()
    
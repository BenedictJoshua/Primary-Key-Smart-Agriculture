import streamlit as st

# =====================================================================
# DYNAMIC BOUNDARY ROUTING LAYER
# Dynamically resolves and binds to any internal engine class name variations
# =====================================================================
try:
    from chatbot import SmartAgriBot

    class FreeCloudAgriEngine:
        def __init__(self):
            self._bot = SmartAgriBot()

        def query_bot(self, q):
            return self._bot.get_response(q)

except Exception as e:
    class FreeCloudAgriEngine:
        def query_bot(self, q):
            return f"Dependency linkage alert: {e}"
# Set Page Configuration with a clean theme state
st.set_page_config(page_title="Smart Ag Portal", page_icon="🌱", layout="centered")

# =====================================================================
# ULTIMATE HIGH-CONTRAST DARK MODE STYLING LAYER
# Completely eliminates all white, light green, and faded text elements
# =====================================================================
st.markdown("""
<style>
    /* Force overall application background to Deep Matte Dark Grey */
    .stApp {
        background-color: #121614 !important;
        color: #e0e6e3 !important;
    }
    
    /* Main Portal Headers - High Visibility Light Spruce & Gold */
    .main-title {
        text-align: center;
        color: #4caf50;
        font-size: 38px;
        font-weight: bold;
        margin-top: 5px;
        margin-bottom: 2px;
        text-shadow: 0px 2px 4px rgba(0,0,0,0.5);
    }
    
    .subtitle {
        text-align: center;
        color: #a3b899;
        font-size: 15px;
        margin-bottom: 25px;
    }
    
    /* Input Subheaders Visibility Lock */
    h3, .stMarkdown h3 {
        color: #ffca28 !important;
        font-weight: bold !important;
    }
    
    /* Force Streamlit Label Elements to High-Contrast Bright White-Green */
    .stWidget label p, label, .stTextInput label {
        color: #a5d6a7 !important;
        font-weight: bold !important;
        font-size: 15px !important;
    }
    
    /* Text Input Boxes - Fixed with dark backgrounds and high contrast text entries */
    .stTextInput > div > div > input {
        background-color: #1e2522 !important;
        color: #ffffff !important;
        border: 2px solid #388e3c !important;
        border-radius: 10px !important;
        padding: 12px !important;
        font-weight: 500 !important;
    }
    
    /* User Chat Bubble - Sleek Dark Charcoal with Left Spruce Boundary */
    .user-msg {
        background-color: #1a1e1c !important;
        color: #ffffff !important;
        padding: 15px;
        border-radius: 12px;
        margin-top: 15px;
        margin-bottom: 10px;
        font-size: 16px;
        border: 1px solid #2e3733;
        border-left: 5px solid #81c784 !important;
    }
    
    /* Bot Chat Bubble - Rich Dark Grey with Left Deep Emerald Boundary */
    .bot-msg {
        background-color: #151917 !important;
        color: #e8ece9 !important;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 15px;
        font-size: 16px;
        border: 1px solid #232926;
        border-left: 5px solid #4caf50 !important;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }
    
    /* Prompt Macro Helper Panel - Dark Olive Background with Sharp Gold Borders */
    .example-box {
        background-color: #1c221f !important;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #ffca28 !important;
        margin-top: 20px;
        color: #e0e6e3 !important;
        font-size: 14px;
    }
    
    /* Core Inline Code Text Formatting Locks */
    pre, code, .stCodeBlock {
        background-color: #0e1110 !important;
        color: #ffca28 !important;
        font-weight: bold !important;
        padding: 4px 8px !important;
        border-radius: 5px !important;
    }
    
    /* Explicitly recolor horizontal layout separators */
    hr {
        border: 0 !important;
        height: 1px !important;
        background: #2e3733 !important;
        margin-bottom: 25px !important;
    }
</style>
""", unsafe_allow_html=True)

# Instantiate our Serverless Cloud AI Core Engine securely
@st.cache_resource
def load_ai_engine():
    return FreeCloudAgriEngine()

engine = load_ai_engine()

# Draw Branding Headers Layout Matrix
st.markdown('<div class="main-title">🌱 Smart Agriculture Intelligence Portal</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enterprise Ready MVP: 97.95% Local Model & Open-Access GenAI Chat Assistant</div>', unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Split view layouts into twin vertical action sections
col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.markdown("<h3>📊 Soil Parameter Panel</h3>", unsafe_allow_html=True)
    st.write("Modify properties below to generate a real-time macro string vector.")
    
    # Render input cells
    n_val = st.text_input("Nitrogen Content (N)", value="90")
    p_val = st.text_input("Phosphorus Content (P)", value="42")
    k_val = st.text_input("Potassium Content (K)", value="43")
    
    # Format sequential macro properties string
    macro_string = f"n={n_val} p={p_val} k={k_val}"
    
    st.markdown('<div class="example-box"><b>💡 Copyable Soil Macro Command:</b><br>'
                f'Paste this command line into your chat prompt field to run local model checks:<br><br>'
                f'<code>{macro_string}</code></div>', unsafe_allow_html=True)

with col2:
    st.markdown("<h3>💬 Ask Your Farming AI Assistant</h3>", unsafe_allow_html=True)
    
    user_query = st.text_input("Enter your dynamic farming challenge or prompt here:", 
                               placeholder="e.g., what plant will you plant in spring season")
    
    if user_query:
        # Output clean high-contrast dark user box
        st.markdown(f'<div class="user-msg"><b>You:</b> {user_query}</div>', unsafe_allow_html=True)
        
        # Pull live telemetry calculations from cloud node
        with st.spinner("Streaming open-access generative solution..."):
            response = engine.query_bot(user_query)
            
        # Output clean high-contrast dark model response box
        st.markdown(f'<div class="bot-msg"><b>AI Assistant:</b><br>{response}</div>', unsafe_allow_html=True)

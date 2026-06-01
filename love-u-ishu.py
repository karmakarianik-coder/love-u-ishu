import random
import streamlit as st

# 1. Page Configuration (Modern Wide Layout)
st.set_page_config(page_title="Be My Valentine? ❤️", layout="centered", page_icon="❤️")

# 2. Modern UI Styling using Custom CSS
st.markdown("""
    <style>
        /* Hide default Streamlit header/footer elements for a clean look */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Main Container Styling */
        .main-container {
            text-align: center;
            padding: 20px;
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        }
        
        /* Typography */
        .title-text {
            font-size: 2.8rem;
            font-weight: 700;
            color: #2c3e50;
            margin-bottom: 5px;
        }
        .subtitle-text {
            font-size: 1.2rem;
            color: #7f8c8d;
            margin-bottom: 30px;
        }
        
        /* Custom Button Styling override for Streamlit */
        div.stButton > button:first-child {
            border-radius: 50px;
            padding: 12px 35px;
            font-size: 1.1rem;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        }
        
        /* YES Button Specific Style */
        div[data-testid="column"]:nth-of-type(1) div.stButton > button:first-child {
            background-color: #2ecc71;
            color: white;
            border: none;
            width: 100%;
        }
        div[data-testid="column"]:nth-of-type(1) div.stButton > button:first-child:hover {
            background-color: #27ae60;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(46, 204, 113, 0.3);
        }
        
        /* NO Button Specific Style */
        div[data-testid="column"]:nth-of-type(2) div.stButton > button:first-child {
            background-color: #ffffff;
            color: #e74c3c;
            border: 2px solid #e74c3c;
        }
        div[data-testid="column"]:nth-of-type(2) div.stButton > button:first-child:hover {
            background-color: #fdf2f2;
        }
        
        /* Success Screen Design */
        .success-card {
            background: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05);
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Session State Initialization
if "no_offset_x" not in st.session_state:
    st.session_state.no_offset_x = 0
if "no_offset_y" not in st.session_state:
    st.session_state.no_offset_y = 0
if "is_accepted" not in st.session_state:
    st.session_state.is_accepted = False

# 4. Logic Functions
def jump_no_button():
    # Sophisticated random ranges so it doesn't break out of screen grid completely
    st.session_state.no_offset_x = random.choice([-120, -80, 80, 120, -160, 160])
    st.session_state.no_offset_y = random.choice([-40, -20, 20, 40, 60, -60])

def accept_proposal():
    st.session_state.is_accepted = True

# --- SCREEN RENDERING ---

# SCREEN A: When Success/Accepted
if st.session_state.is_accepted:
    st.balloons()
    st.markdown("""
        <div class="success-card">
            <h1 style='color: #d33a64; font-size: 3rem; margin-bottom: 10px;'>Yeyy! It's an absolute YES! 💖</h1>
            <p style='color: #64748b; font-size: 1.3rem; margin-bottom: 25px;'>You just made my entire year. Best choice ever! 🥰</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Elegant Aesthetic GIF
    st.image(
        "https://giphy.com",
        use_container_width=True
    )

# SCREEN B: Main Question Screen
else:
    # Text Header Container
    st.markdown("""
        <div class="main-container">
            <div class="title-text">Will you be my Valentine? 🥺❤️</div>
            <div class="subtitle-text">Think carefully, but honestly there's only one right answer...</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Main Cute Illustration Centered
    st.image(
        "https://giphy.com",
        width=380
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True) # Clean structural spacing
    
    # Professional Button Column Layout (Clean grid split)
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.button("Yes, I'd love to! 😍", on_click=accept_proposal)
        
    with col2:
        # Injecting dynamic positions smoothly via wrapper div margins
        st.markdown(
            f"<div style='margin-left: {st.session_state.no_offset_x}px; margin-top: {st.session_state.no_offset_y}px; transition: margin 0.2s ease-out;'>",
            unsafe_allow_html=True
        )
        st.button("No thanks 😢", on_click=jump_no_button)
        st.markdown("</div>", unsafe_allow_html=True)

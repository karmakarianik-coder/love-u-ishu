import random
import streamlit as st

# Page configuration
st.set_page_config(page_title="Be My Valentine? ❤️", layout="centered")


if "no_x" not in st.session_state:
    st.session_state.no_x = 0.0  # Initial left alignment
if "no_y" not in st.session_state:
    st.session_state.no_y = 0.0  # Initial top alignment
if "accepted" not in st.session_state:
    st.session_state.accepted = False


def move_no_button():
    # Random margins generate karna button ko shift karne ke liye
    st.session_state.no_x = random.randint(-150, 150)
    st.session_state.no_y = random.randint(-50, 50)



def accept_valentine():
    st.session_state.accepted = True


# --- UI Layout ---

if st.session_state.accepted:
    st.balloons()
    st.markdown(
        "<h1 style='text-align: center; color: #e91e63;'>Yeeeeeeyyyyy! I Love You bby ! 💖🥰🎉</h1>",
        unsafe_allow_html=True,
        )
    st.image(
        "https://giphy.com",
        use_column_width=True,
        )

else:
    st.markdown(
        "<h1 style='text-align: center; color: #ff4d4d;'>Will you be my Valentine? 🥺❤️</h1>",
        unsafe_allow_html=True,
        )

    st.image(
        "https://giphy.com",
        width=300,
        )

    st.write("")  # Spacing ke liye

    # Do columns banana Buttons ke liye
    col1, col2 = st.columns([1, 1])

    with col1:
        st.button("Yes 😍", on_click=accept_valentine, use_container_width=True)

    with col2:
        # Custom spacing create karna python session state se taaki button move hota dikhe
        st.markdown(
            f"<div style='margin-left: {st.session_state.no_x}px; margin-top: {st.session_state.no_y}px;'>",
            unsafe_allow_html=True,
            )
        st.button("No 😢", on_click=move_no_button)
        st.markdown("</div>", unsafe_allow_html=True)

import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="SPUR Model Parameter Explorer",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── password gate ───────────────────────────────────────────────
def check_password():
    """Returns True if the user has entered the correct password."""
    expected = st.secrets.get("app", {}).get("password", "")

    if st.session_state.get("authenticated"):
        return True

    st.markdown(
        """
        <style>
          .login-box { max-width: 420px; margin: 120px auto; text-align: center; }
          .login-box h1 { font-size: 28px; margin-bottom: 8px; }
          .login-box p  { color: #888; margin-bottom: 32px; }
        </style>
        <div class="login-box">
          <h1>📡 SPUR Explorer</h1>
          <p>Enter the access password to continue.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        pwd = st.text_input("Password", type="password", label_visibility="collapsed",
                            placeholder="Enter password…")
        if st.button("Access Explorer", use_container_width=True, type="primary"):
            if pwd == expected:
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("Incorrect password — please try again.")
    return False


if not check_password():
    st.stop()

# ─── load and render the explorer HTML ───────────────────────────
html_path = os.path.join(os.path.dirname(__file__), "spur_explorer.html")

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# render at full viewport height with scrolling enabled
components.html(html_content, height=900, scrolling=True)

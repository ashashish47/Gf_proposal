import streamlit as st
import random
from datetime import datetime

st.set_page_config(
    page_title="Official Girlfriend Proposal ❤️",
    page_icon="💖",
    layout="centered"
)

# ---------- CSS ----------
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg,#ffe6f0,#fff5f8);
}

.big-title{
    text-align:center;
    font-size:3rem;
    color:#ff4d88;
    font-weight:bold;
}

.love-card{
    padding:20px;
    border-radius:20px;
    background:white;
    box-shadow:0px 4px 15px rgba(0,0,0,0.1);
    margin:10px 0px;
}

.yes-btn button{
    background-color:#ff4d88 !important;
    color:white !important;
    border-radius:15px !important;
    height:60px !important;
    font-size:24px !important;
}

@keyframes heartbeat{
    0%{transform:scale(1);}
    25%{transform:scale(1.1);}
    50%{transform:scale(1);}
    75%{transform:scale(1.1);}
    100%{transform:scale(1);}
}

.heart{
    text-align:center;
    font-size:80px;
    animation:heartbeat 1s infinite;
}
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown('<div class="heart">❤️</div>', unsafe_allow_html=True)
st.markdown(
    '<p class="big-title">A Little Question For You...</p>',
    unsafe_allow_html=True
)

st.balloons()

# # ---------- Music ----------
# st.subheader("🎵 Our Song")
# uploaded_audio = st.file_uploader(
#     "Upload your special song (optional)",
#     type=["mp3","wav"]
# )

# if uploaded_audio:
#     st.audio(uploaded_audio)

# ---------- Memory Section ----------
st.subheader("📸 Some Things I Never Want To Forget")

memories = [
    "✨ The first time you made me smile uncontrollably",
    "✨ Our random late-night conversations",
    "✨ Every moment you supported me",
    "✨ Every laugh we've shared",
    "✨ Every memory that became special because you were in it"
]

for m in memories:
    st.markdown(f"- {m}")

# ---------- Love Letter ----------
st.subheader("💌 Open This Letter")

with st.expander("Click to read ❤️"):
    st.markdown("""
Dear Love,

Maybe we've already shared countless moments together.

Maybe we've laughed, cared for each other, annoyed each other,
and created memories we'll remember forever.

But there's one thing I never properly did...

I never officially asked the most important question.

And honestly?

I would choose you again and again,
every single day.

❤️
""")

# ---------- Reasons ----------
st.subheader("🌹 Reasons Why You're Amazing")

reasons = [
    "Your smile",
    "Your kindness",
    "Your beautiful heart",
    "The way you make ordinary days special",
    "The fact that you're YOU"
]

for r in reasons:
    st.success(r)

# ---------- Gift ----------
st.subheader("🎁 Surprise")

if st.button("Open Surprise Gift"):
    st.snow()
    st.markdown("""
    ## 🌹

    If I could gift you one thing,
    it would be the ability to see yourself through my eyes.

    Then you'd know exactly how special you are.
    """)

st.divider()

# ---------- Proposal ----------
st.markdown(
    """
    <h1 style='text-align:center;color:#ff4d88;'>
    ❤️ Official Question ❤️
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align:center;'>Will you officially be my girlfriend? 💖</h3>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    yes = st.button("YES ❤️")

with col2:
    funny_no = random.choice([
        "No 🙈",
        "Are you sure? 🤔",
        "Think Again 😏",
        "Really? 😭",
        "Wrong Answer 😂"
    ])
    st.button(funny_no)

# ---------- Accepted ----------
if yes:
    st.balloons()
    st.snow()

    st.success("SHE SAID YES! ❤️")

    st.markdown(f"""
    # 💍 Official Relationship Certificate

    This certifies that

    ## ❤️ You & Me ❤️

    are officially and unquestionably together.

    Effective Date:
    **{datetime.now().strftime("%d %B %Y")}**

    Signed:
    **The Lucky Boyfriend**
    """)

    st.markdown("""
    ## 🌍 Forever starts now.
    """)

    st.info("I love you ❤️")

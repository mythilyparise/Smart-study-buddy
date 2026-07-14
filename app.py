import streamlit as st

from utils.pdf_loader import extract_text
from utils.text_splitter import split_text
from utils.vector_store import create_vector_store
from utils.retriever import get_retriever
from utils.llm import get_llm


# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="Smart Study Buddy",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# THEME TOGGLE
# =========================================================
dark_mode = st.sidebar.toggle("🌙 Dark Mode", value=False)

if dark_mode:
    bg_color = "#111118"
    text_color = "#F4F4F6"
    heading_color = "#FFFFFF"
    card_bg = "rgba(31, 31, 43, 0.94)"
    secondary_bg = "#1C1C28"
    input_bg = "#252532"
    border_color = "#554A72"
    sidebar_bg = "#181822"
else:
    bg_color = "#FAF9FF"
    text_color = "#28252E"
    heading_color = "#000000"
    card_bg = "rgba(255, 255, 255, 0.88)"
    secondary_bg = "#F5F0FF"
    input_bg = "#FFFFFF"
    border_color = "#DED3FF"
    sidebar_bg = "#F2ECFF"


# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown(
    f"""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@700&display=swap');


/* =========================
   GLOBAL
========================= */

html, body, [class*="css"] {{
    font-family: 'DM Sans', sans-serif;
}}

.stApp {{
    background:
        radial-gradient(circle at 10% 10%, rgba(196, 156, 255, 0.16), transparent 25%),
        radial-gradient(circle at 90% 20%, rgba(88, 196, 255, 0.13), transparent 25%),
        radial-gradient(circle at 70% 90%, rgba(255, 170, 105, 0.12), transparent 25%),
        {bg_color};

    color: {text_color};
}}

.block-container {{
    padding-top: 2rem;
    padding-bottom: 5rem;
    max-width: 1200px;
}}


/* =========================
   HEADINGS
========================= */

h1, h2, h3, h4, h5, h6 {{
    color: {heading_color} !important;
}}

p, label {{
    color: {text_color};
}}


/* =========================
   SIDEBAR
========================= */

[data-testid="stSidebar"] {{
    background: {sidebar_bg};
    border-right: 1px solid {border_color};
}}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {{
    color: {heading_color} !important;
}}


/* =========================
   HERO
========================= */

.hero {{
    padding: 50px;
    border-radius: 30px;

    background:
        linear-gradient(
            135deg,
            #9B7BFF,
            #C56CFF,
            #FF79AE,
            #FFAA71
        );

    box-shadow:
        0 25px 60px rgba(120, 75, 200, 0.28);

    margin-bottom: 35px;

    position: relative;
    overflow: hidden;
}}

.hero::before {{
    content: "";
    position: absolute;

    width: 250px;
    height: 250px;

    border-radius: 50%;

    background:
        rgba(255,255,255,0.15);

    right: -70px;
    top: -100px;
}}

.hero h1 {{
    font-family:
        'Playfair Display',
        serif;

    font-size:
        50px;

    color:
        #000000 !important;

    margin:
        0;

        text-align:
        center;
}}

.hero p {{
    color:
        #1D1528 !important;

    font-size:
        18px;

    max-width:
        700px;

    margin-top:
        15px;

        text-align:
        center;
}}


/* =========================
   CARDS
========================= */

.glass-card,
.answer-card,
.flashcard {{

    background:
        {card_bg};

    border:
        1px solid {border_color};

    border-radius:
        22px;

    padding:
        28px;

    box-shadow:
        0 15px 40px
        rgba(70, 50, 130, 0.13);

    color:
        {text_color};
}}

.glass-card {{
    margin:
        25px 0;
        text-align:
        center;
}}


/* =========================
   ANSWER CARD
========================= */

.answer-card {{
    border-left:
        6px solid #8A63FF;

    margin:
        25px 0;

        text-align:
        left;
}}

.answer-card p {{
    color:
        {text_color} !important;

    line-height:
        1.7;

        text-align:
        center;
}}


/* =========================
   FLASHCARDS
========================= */

.flashcard {{
    margin:
        20px 0;

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease;
}}

.flashcard:hover {{
    transform:
        translateY(-5px);

    box-shadow:
        0 22px 50px
        rgba(115, 75, 190, 0.20);
}}

.flashcard-number {{
    color:
        #9A6BFF;

    font-weight:
        700;

    font-size:
        13px;

    letter-spacing:
        1.5px;
}}


/* =========================
   FILE UPLOADER
========================= */

[data-testid="stFileUploader"] {{
    background:
        {card_bg};

    border:
        2px dashed #A989FF;

    border-radius:
        22px;

    padding:
        20px;

    box-shadow:
        0 12px 35px
        rgba(100, 70, 170, 0.12);
}}


/* =========================
   BUTTONS
========================= */

.stButton > button {{

    border:
        none;

    border-radius:
        15px;

    padding:
        12px 28px;

    font-weight:
        700;

    color:
        white !important;

    background:
        linear-gradient(
            135deg,
            #7657FF,
            #B45CFF,
            #FF6FAE
        );

    box-shadow:
        0 10px 28px
        rgba(120, 85, 255, 0.32);

    transition:
        all 0.25s ease;
}}

.stButton > button:hover {{

    transform:
        translateY(-3px);

    box-shadow:
        0 16px 35px
        rgba(120, 85, 255, 0.42);
}}


/* =========================
   INPUTS
========================= */

.stTextInput input {{

    background:
        {input_bg};

    color:
        {text_color};

    border:
        1px solid {border_color};

    border-radius:
        14px;

    padding:
        14px;
}}


/* =========================
   TABS
========================= */

.stTabs [data-baseweb="tab-list"] {{

    gap:
        10px;

    background:
        {secondary_bg};

    padding:
        8px;

    border-radius:
        18px;
}}

.stTabs [data-baseweb="tab"] {{

    border-radius:
        13px;

    padding:
        10px 22px;

    color:
        {text_color};

    font-weight:
        600;
}}

.stTabs [aria-selected="true"] {{

    background:
        linear-gradient(
            135deg,
            #E4D8FF,
            #FFD8EA
        );

    color:
        #000000 !important;
}}


/* =========================
   EXPANDERS
========================= */

[data-testid="stExpander"] {{

    background:
        {card_bg};

    border:
        1px solid {border_color};

    border-radius:
        16px;

    overflow:
        hidden;
}}


/* =========================
   STREAMLIT CLEANUP
========================= */

#MainMenu {{
    visibility:
        hidden;
}}

footer {{
    visibility:
        hidden;
}}

</style>
""",
    unsafe_allow_html=True
)


# =========================================================
# HERO SECTION
# =========================================================
st.markdown(
    """
<div class="hero"><h1>

    Smart Study Buddy ✨

    
        Turn your notes into intelligent answers and personalized
        flashcards with your AI-powered study companion.
    

</div></h1>
""",
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.markdown("## 📚 Study Space")

subject = st.sidebar.selectbox(
    "Choose Subject",
    [
        "Operating Systems",
        "DBMS",
        "Computer Networks",
        "Artificial Intelligence",
        "Python"
    ]
)

st.sidebar.success(
    f"✨ Studying: {subject}"
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
### 🚀 Features

💬 Notes-based AI Q&A

🃏 AI Flashcard Generator

📖 Source-based answers

✨ Light & Dark Mode
"""
)


# =========================================================
# PDF UPLOAD
# =========================================================
st.markdown("## 📄 Upload Your Study Notes")

st.write(
    "Upload a PDF and transform your notes into an interactive learning experience."
)

uploaded_file = st.file_uploader(
    "Drop your PDF notes here",
    type=["pdf"]
)


# =========================================================
# PROCESS PDF
# =========================================================
if uploaded_file is not None:

    st.success(
        f"✨ {uploaded_file.name} uploaded successfully!"
    )

    text = extract_text(uploaded_file)

    chunks = split_text(text)

    with st.spinner(
        "✨ Preparing your intelligent study space..."
    ):

        vector_store = create_vector_store(
            chunks
        )

    retriever = get_retriever(
        vector_store
    )

    st.success(
        "🎉 Your notes are ready!"
    )


    # =====================================================
    # NOTE DETAILS
    # =====================================================
    col1, col2 = st.columns(2)

    with col1:

        with st.expander(
            "📄 View Extracted Notes"
        ):

            st.text_area(
                "PDF Content",
                text,
                height=300
            )

    with col2:

        with st.expander(
            "🧩 View Text Chunks"
        ):

            st.write(
                f"Total Chunks: {len(chunks)}"
            )

            for i, chunk in enumerate(chunks):

                st.markdown(
                    f"**Chunk {i + 1}**"
                )

                st.write(chunk)

                st.divider()


    # =====================================================
    # MAIN TABS
    # =====================================================
    qa_tab, flashcard_tab = st.tabs(
        [
            "💬 Ask Your Notes",
            "🃏 Generate Flashcards"
        ]
    )


    # =====================================================
    # Q&A TAB
    # =====================================================
    with qa_tab:

        st.markdown(
            "## 💬 Ask Your Notes"
        )

        st.write(
            "Ask anything from your uploaded study material."
        )

        question = st.text_input(
            "Your question",
            placeholder="Example: What is a loss function?"
        )

        if st.button(
            "✨ Find My Answer",
            key="answer_button"
        ):

            if question.strip() == "":

                st.warning(
                    "Please enter a question first."
                )

            else:

                with st.spinner(
                    "🔎 Searching your notes..."
                ):

                    docs = retriever.invoke(
                        question
                    )

                    context = "\n\n".join(
                        doc.page_content
                        for doc in docs
                    )

                    prompt = f"""
You are Smart Study Buddy, an AI tutor.

Answer the question ONLY using the provided notes.

If the answer cannot be found in the provided notes,
say exactly:

"I couldn't find that information in the uploaded notes."

Do not use outside knowledge.

SUBJECT:
{subject}

NOTES:
{context}

QUESTION:
{question}

ANSWER:
"""

                    llm = get_llm()

                    response = llm.invoke(
                        prompt
                    )


                # CLEAN RESPONSE
                if isinstance(
                    response.content,
                    list
                ):

                    answer = "".join(
                        item.get(
                            "text",
                            ""
                        )

                        for item
                        in response.content

                        if isinstance(
                            item,
                            dict
                        )
                    )

                else:

                    answer = (
                        response.content
                    )


                # DISPLAY ANSWER
                st.markdown(
                    f"""
<div class="answer-card">

    🤖 Your Answer

    {answer}

</div>
""",
                    unsafe_allow_html=True
                )


                # SOURCES
                st.markdown(
                    "### 📚 Sources from Your Notes"
                )

                for i, doc in enumerate(docs):

                    with st.expander(
                        f"📖 Source {i + 1}"
                    ):

                        st.write(
                            doc.page_content
                        )


    # =====================================================
    # FLASHCARD TAB
    # =====================================================
    with flashcard_tab:

        st.markdown(
            "## 🃏 AI Flashcard Studio"
        )

        st.write(
            "Transform your notes into beautiful revision cards."
        )

        number_of_cards = st.slider(
            "How many flashcards?",
            min_value=3,
            max_value=15,
            value=5
        )

        if st.button(
            "✨ Create My Flashcards",
            key="flashcard_button"
        ):

            with st.spinner(
                "🎨 Creating your flashcards..."
            ):

                flashcard_context = (
                    text[:15000]
                )

                flashcard_prompt = f"""
You are Smart Study Buddy.

Create exactly {number_of_cards}
high-quality study flashcards.

Use ONLY the provided notes.

Use this exact format:

QUESTION: question
ANSWER: answer
---

Keep questions useful for exams.

Keep answers clear and concise.

Do not use outside knowledge.

SUBJECT:
{subject}

NOTES:
{flashcard_context}
"""

                llm = get_llm()

                flashcard_response = (
                    llm.invoke(
                        flashcard_prompt
                    )
                )


            # CLEAN RESPONSE
            if isinstance(
                flashcard_response.content,
                list
            ):

                flashcard_text = "".join(
                    item.get(
                        "text",
                        ""
                    )

                    for item
                    in flashcard_response.content

                    if isinstance(
                        item,
                        dict
                    )
                )

            else:

                flashcard_text = (
                    flashcard_response.content
                )


            # SPLIT FLASHCARDS
            cards = flashcard_text.split(
                "---"
            )

            st.success(
                "✨ Your flashcards are ready!"
            )

            card_number = 1

            for card in cards:

                card = card.strip()

                if card:

                    st.markdown(
                        f"""
<div class="flashcard">

    <div class="flashcard-number">
        FLASHCARD {card_number}
    </div>

    <br>

    {card}

</div>
""",
                        unsafe_allow_html=True
                    )

                    card_number += 1


# =========================================================
# EMPTY STATE
# =========================================================
else:

    st.markdown(
        """
<div class="glass-card"><h3>

     Ready to start studying?

    
        Upload your PDF notes above and unlock AI-powered
        answers and personalized flashcards.
    

</div></h3>
""",
        unsafe_allow_html=True
    )
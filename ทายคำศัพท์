import random
import streamlit as st

# ---------- ข้อมูลคำศัพท์ ----------
VOCAB = [
    {"thai": "โต๊ะ",       "en": "Table",        "emoji": "🗄️"},
    {"thai": "เก้าอี้",     "en": "Chair",        "emoji": "🪑"},
    {"thai": "เตียง",      "en": "Bed",          "emoji": "🛏️"},
    {"thai": "โซฟา",       "en": "Sofa",         "emoji": "🛋️"},
    {"thai": "ตู้เย็น",     "en": "Refrigerator", "emoji": "🧊"},
    {"thai": "โทรทัศน์",    "en": "Television",   "emoji": "📺"},
    {"thai": "โคมไฟ",      "en": "Lamp",         "emoji": "💡"},
    {"thai": "กระจก",      "en": "Mirror",       "emoji": "🪞"},
    {"thai": "ตู้เสื้อผ้า",  "en": "Wardrobe",     "emoji": "🚪"},
    {"thai": "นาฬิกา",     "en": "Clock",        "emoji": "🕰️"},
]

st.set_page_config(page_title="ทายคำศัพท์ ของใช้ในบ้าน", page_icon="🏠", layout="centered")

# ---------- สไตล์ ปรับให้เข้าถึงง่าย: ปุ่มใหญ่ ตัวอักษรใหญ่ สีตัดกันชัด ----------
st.markdown(
    """
    <style>
    .stButton > button {
        width: 100%;
        min-height: 3.4em;
        font-size: 1.15rem;
        font-weight: 600;
        border-radius: 14px;
        border: 2px solid #D8E2DC;
        white-space: normal;
    }
    .stButton > button:focus-visible {
        outline: 3px solid #17434A;
        outline-offset: 2px;
    }
    .item-emoji {
        text-align: center;
        font-size: 5.5rem;
        line-height: 1;
    }
    .thai-word {
        text-align: center;
        font-size: 2rem;
        font-weight: 700;
        margin-top: 0.3rem;
        color: #17434A;
    }
    .prompt-text {
        text-align: center;
        font-size: 1.1rem;
        color: #5B6B62;
        margin-bottom: 1.2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------- ฟังก์ชันช่วยจัดการสถานะเกม ----------
def start_game():
    order = VOCAB.copy()
    random.shuffle(order)
    st.session_state.order = order
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.selected = None
    st.session_state.choices = None
    build_choices()


def build_choices():
    item = st.session_state.order[st.session_state.current]
    distractors = random.sample([v for v in VOCAB if v["en"] != item["en"]], 3)
    choices = distractors + [item]
    random.shuffle(choices)
    st.session_state.choices = choices


def submit_answer(choice_en, correct_en):
    st.session_state.answered = True
    st.session_state.selected = choice_en
    if choice_en == correct_en:
        st.session_state.score += 1


def next_question():
    st.session_state.current += 1
    st.session_state.answered = False
    st.session_state.selected = None
    if st.session_state.current < len(VOCAB):
        build_choices()


# ---------- เริ่มต้นสถานะครั้งแรก ----------
if "order" not in st.session_state:
    start_game()

total = len(VOCAB)

# ---------- หัวข้อ ----------
st.markdown("<h1 style='text-align:center;'>🏠 ทายคำศัพท์ ของใช้ในบ้าน</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; color:#5B6B62;'>เลือกคำภาษาอังกฤษที่ตรงกับของใช้ในบ้านแต่ละชิ้น</p>",
    unsafe_allow_html=True,
)

# ---------- จบเกม ----------
if st.session_state.current >= total:
    score = st.session_state.score
    ratio = score / total
    if ratio == 1:
        emoji, title = "🏆", "เก่งมาก! เต็ม 10 ข้อ!"
    elif ratio >= 0.7:
        emoji, title = "🎉", "ทำได้ดีมาก!"
    elif ratio >= 0.4:
        emoji, title = "🙂", "ไปได้สวย ฝึกอีกนิดนะ"
    else:
        emoji, title = "💪", "ลองใหม่อีกครั้งนะ"

    st.markdown(f"<div class='item-emoji'>{emoji}</div>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align:center; color:#17434A;'>{title}</h2>", unsafe_allow_html=True)
    st.markdown(
        f"<p style='text-align:center; font-size:1.1rem;'>คุณตอบถูก {score} จาก {total} ข้อ</p>",
        unsafe_allow_html=True,
    )
    st.progress(1.0)
    if st.button("🔁 เล่นอีกครั้ง"):
        start_game()
        st.rerun()

# ---------- หน้าคำถาม ----------
else:
    item = st.session_state.order[st.session_state.current]

    col_progress, col_score = st.columns([4, 1.3])
    with col_progress:
        st.progress(st.session_state.current / total)
    with col_score:
        st.markdown(
            f"<div style='text-align:right; font-weight:700; color:#17434A;'>"
            f"คะแนน {st.session_state.score}/{total}</div>",
            unsafe_allow_html=True,
        )

    st.markdown(f"<div class='item-emoji'>{item['emoji']}</div>", unsafe_allow_html=True)
    st.markdown(
        f"<div class='thai-word'>{item['thai']}</div>"
        f"<p style='text-align:center; color:#5B6B62; margin-top:0.2rem;'>"
        f"ข้อที่ {st.session_state.current + 1} จาก {total}</p>",
        unsafe_allow_html=True,
    )
    st.markdown("<p class='prompt-text'>ข้อนี้ภาษาอังกฤษเรียกว่าอะไร?</p>", unsafe_allow_html=True)

    choices = st.session_state.choices
    cols = st.columns(2)

    for idx, choice in enumerate(choices):
        col = cols[idx % 2]
        with col:
            if not st.session_state.answered:
                if st.button(f"{idx + 1}. {choice['en']}", key=f"opt_{st.session_state.current}_{idx}"):
                    submit_answer(choice["en"], item["en"])
                    st.rerun()
            else:
                # แสดงผลเฉลยหลังตอบแล้ว: เขียว = ถูก, แดง = ตัวที่กดแล้วผิด
                is_correct = choice["en"] == item["en"]
                is_selected = choice["en"] == st.session_state.selected
                if is_correct:
                    st.success(f"{idx + 1}. {choice['en']} ✅")
                elif is_selected:
                    st.error(f"{idx + 1}. {choice['en']} ❌")
                else:
                    st.button(f"{idx + 1}. {choice['en']}", key=f"opt_{st.session_state.current}_{idx}", disabled=True)

    # ---------- คำใบ้ ----------
    if not st.session_state.answered:
        with st.expander("💡 ขอคำใบ้ (ตัวอักษรแรก)"):
            st.write(f"คำตอบเริ่มต้นด้วยตัวอักษร **{item['en'][0]}**")

    # ---------- ผลลัพธ์ + ปุ่มข้อถัดไป ----------
    if st.session_state.answered:
        if st.session_state.selected == item["en"]:
            st.success(f"ถูกต้อง! \"{item['thai']}\" คือ {item['en']}")
        else:
            st.error(f"ยังไม่ถูก คำตอบที่ถูกต้องคือ {item['en']}")

        label = "ข้อถัดไป →" if st.session_state.current < total - 1 else "ดูผลคะแนน →"
        if st.button(label, type="primary"):
            next_question()
            st.rerun()

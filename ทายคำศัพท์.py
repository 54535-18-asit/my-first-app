import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา — ของใช้ในบ้าน")

TIME_LIMIT = 60  # วินาที (10 ข้อ เลยให้เวลามากกว่าเดิม)

# ----------------------------------------------------
# 📌 คำศัพท์ 10 คำ + คำใบ้แบบเติมตัวอักษร
# ----------------------------------------------------
QUESTIONS = [
    {"key": "ans1",  "hint": "T _ _ l e",        "emoji": "🗄️", "answer": "table"},
    {"key": "ans2",  "hint": "C h _ i r",         "emoji": "🪑", "answer": "chair"},
    {"key": "ans3",  "hint": "B _ d",             "emoji": "🛏️", "answer": "bed"},
    {"key": "ans4",  "hint": "S _ f a",           "emoji": "🛋️", "answer": "sofa"},
    {"key": "ans5",  "hint": "R e f r i g e r _ t o r", "emoji": "🧊", "answer": "refrigerator"},
    {"key": "ans6",  "hint": "T e l e v i s i _ n",     "emoji": "📺", "answer": "television"},
    {"key": "ans7",  "hint": "L _ m p",           "emoji": "💡", "answer": "lamp"},
    {"key": "ans8",  "hint": "M i r r _ r",       "emoji": "🪞", "answer": "mirror"},
    {"key": "ans9",  "hint": "W a r d r _ b e",   "emoji": "🚪", "answer": "wardrobe"},
    {"key": "ans10", "hint": "C l _ c k",         "emoji": "🕰️", "answer": "clock"},
]

# ----------------------------------------------------
# 1. กำหนดค่าเริ่มต้นใน session_state ถ้ายังไม่มี
# ----------------------------------------------------
for q in QUESTIONS:
    val_key = f"{q['key']}_val"
    if val_key not in st.session_state:
        st.session_state[val_key] = ""


# 📌 ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
def reset_game():
    for q in QUESTIONS:
        st.session_state[f"{q['key']}_val"] = ""  # เคลียร์ค่าทุกช่อง
    st.session_state.start = time.time()  # เริ่มเวลาใหม่
    st.session_state.is_ended = False  # ปิด Dialog


# ----------------------------------------------------
# 📌 ฟังก์ชัน MessageBox (Dialog)
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(answers):
    st.balloons()
    score = 0

    for i, q in enumerate(QUESTIONS, start=1):
        u_ans = answers[q["key"]].strip().lower()
        if u_ans == q["answer"]:
            st.success(f"✅ ข้อ {i} ({q['emoji']}): ถูกต้อง — {q['answer']}")
            score += 1
        else:
            st.error(f"❌ ข้อ {i} ({q['emoji']}): ยังไม่ถูกต้อง (คุณตอบ '{u_ans}' / เฉลย '{q['answer']}')")

    st.info(f"🏆 ได้คะแนนรวม: {score} จาก {len(QUESTIONS)} คะแนน")

    if score == len(QUESTIONS):
        st.success("🎉 You win! เต็มทุกข้อ!")
    elif score >= len(QUESTIONS) * 0.6:
        st.success("👍 เก่งมาก!")
    else:
        st.error("💀 You lose! ลองใหม่อีกครั้งนะ")


# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

# ----------------------------------------------------
# 2. แถบแสดงเวลานับถอยหลัง
# ----------------------------------------------------
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(TIME_LIMIT - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# ----------------------------------------------------
# 3. ช่องรับคำตอบทั้ง 10 ข้อ (ผูก value กับ session_state เพื่อเคลียร์ได้)
# ----------------------------------------------------
current_answers = {}
for i, q in enumerate(QUESTIONS, start=1):
    val_key = f"{q['key']}_val"
    ans = st.text_input(
        f"ข้อ {i}: `{q['hint']}` {q['emoji']}",
        value=st.session_state[val_key],
        key=f"input_{q['key']}",
    )
    st.session_state[val_key] = ans
    current_answers[q["key"]] = ans

# ----------------------------------------------------
# 4. ปุ่มส่งคำตอบ
# ----------------------------------------------------
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()

# ----------------------------------------------------
# 5. แสดง Dialog ผลลัพธ์
# ----------------------------------------------------
if st.session_state.get("is_ended", False):
    show_result_dialog(current_answers)

st.divider()

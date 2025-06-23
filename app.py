import streamlit as st
def render_section(title, icon, color, content_en, content_hu):
    st.markdown(
        f"""
        <div style='background-color: {color}; padding:1rem; border-radius:0.75rem; margin-bottom:1.5rem; color:#000000'>
            <h3>{icon} {title}</h3>
            <p><strong>EN:</strong> {content_en}</p>
            <p><strong>HU:</strong> {content_hu}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.set_page_config(page_title="📘 RE Vizsgafelkészítő – Modul 1", layout="wide")
st.title("📘 Introduction and Overview of Requirements Engineering (Modul 1)")
st.markdown("#### 💡 Ismerd meg a Requirements Engineering alapjait – angolul és magyarul")

# 👇 Alfejezetválasztó
section = st.selectbox("Válassz alfejezetet:", [
    "1.1 What is Requirements Engineering?",
    "1.2 Why is RE important?",
    "1.3 Where is RE applied?",
    "1.4 How is RE performed?",
    "1.5 Role and Tasks of a Requirements Engineer",
    "1.6 What to Learn about RE"
])

# 🎨 Színek és ikonok hozzárendelése
colors = {
    "1.1": "#e6f0ff", "1.2": "#e6ffe6", "1.3": "#fff5cc",
    "1.4": "#f0e6ff", "1.5": "#ffe6e6", "1.6": "#f2f2f2"
}
icons = {
    "1.1": "📘", "1.2": "💡", "1.3": "🌍", "1.4": "⚙️", "1.5": "👤", "1.6": "🎓"
}
code = section[:3]

# 🌐 Kétnyelvű tartalom
if section == "1.1 What is Requirements Engineering?":
    render_section(
    "1.1 What is Requirements Engineering?",
    icons[code],
    colors[code],
    "Requirements Engineering (RE) is about specifying and managing what stakeholders need a system to do. It distinguishes between three types of requirements: functional, quality, and constraints.",
    "A Requirements Engineering (RE) célja a rendszerekkel szemben támasztott igények meghatározása és kezelése. Három fő követelménytípus létezik: funkcionális, minőségi (quality), és korlátozások (constraints)."
    )

elif section == "1.2 Why is RE important?":
    render_section(
        "1.2 Why is Requirements Engineering important?",
        icons[code],
        colors[code],
        "Good RE reduces risks, improves understanding, enables cost estimation, and lays the foundation for testing. Poor RE leads to unclear or missing requirements.",
        "A jó RE csökkenti a hibák kockázatát, javítja a megértést, segíti a költségbecslést és tesztelést. A rossz RE homályos vagy hiányzó követelményekhez vezet."
    )


elif section == "1.3 Where is RE applied?":
    st.markdown(f"""<div style='background-color:{colors[code]}; padding:1rem; border-radius:0.5rem'>
    <h3>{icons[code]} 1.3 Where is RE applied?</h3>
    <p><strong>EN:</strong> RE is used for any kind of system – especially in software-heavy systems involving physical and organizational elements. Requirements may be system, stakeholder, user, domain or business-related.</p>
    <p><strong>HU:</strong> Az RE bármilyen rendszerre alkalmazható, különösen szoftverközpontú rendszerekben. A követelmények származhatnak rendszer-, stakeholder-, felhasználói-, üzleti- vagy doménszintről.</p>
    </div>""", unsafe_allow_html=True)

elif section == "1.4 How is RE performed?":
    st.markdown(f"""<div style='background-color:{colors[code]}; padding:1rem; border-radius:0.5rem'>
    <h3>{icons[code]} 1.4 How is Requirements Engineering performed?</h3>
    <p><strong>EN:</strong> RE includes eliciting, documenting, validating, and managing requirements. Analysis and conflict resolution are part of elicitation. Tailoring the RE process is key.</p>
    <p><strong>HU:</strong> Az RE részei: igények feltárása, dokumentálása, érvényesítése és kezelése. Az elemzés és konfliktuskezelés is a feltárás része. Fontos az RE folyamat testreszabása.</p>
    </div>""", unsafe_allow_html=True)

elif section == "1.5 Role and Tasks of a Requirements Engineer":
    st.markdown(f"""<div style='background-color:{colors[code]}; padding:1rem; border-radius:0.5rem'>
    <h3>{icons[code]} 1.5 Role and Tasks of a Requirements Engineer</h3>
    <p><strong>EN:</strong> This role is played by those who elicit, document, validate, and manage requirements. They bridge the gap between the problem and the solution.</p>
    <p><strong>HU:</strong> A Requirements Engineer szerepét olyan emberek töltik be, akik követelményeket gyűjtenek, dokumentálnak, érvényesítenek és kezelnek — hidat képeznek a probléma és a megoldás között.</p>
    </div>""", unsafe_allow_html=True)

elif section == "1.6 What to Learn about RE":
    st.markdown(f"""<div style='background-color:{colors[code]}; padding:1rem; border-radius:0.5rem'>
    <h3>{icons[code]} 1.6 What to Learn about Requirements Engineering</h3>
    <p><strong>EN:</strong> The CPRE Foundation syllabus covers principles (2), documentation (3), elaboration (4), processes (5), management (6), and tool support (7).</p>
    <p><strong>HU:</strong> A CPRE vizsgaalap tananyaga az alábbiakat fedi le: elvek (2), dokumentáció (3), kibontás (4), folyamatok (5), menedzsment (6), és eszköztámogatás (7).</p>
    </div>""", unsafe_allow_html=True)

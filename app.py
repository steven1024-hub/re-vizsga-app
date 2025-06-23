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
    render_section(
        "1.3 Where is RE applied?",
        icons[code],
        colors[code],
        "RE is used for any kind of system – especially in software-heavy systems involving physical and organizational elements. Requirements may be system, stakeholder, user, domain or business-related.",
        "Az RE bármilyen rendszerre alkalmazható, különösen szoftverközpontú rendszerekben. A követelmények származhatnak rendszer-, stakeholder-, felhasználói-, üzleti- vagy doménszintről."
    )

elif section == "1.4 How is RE performed?":
    render_section(
        "1.4 How is Requirements Engineering performed?",
        icons[code],
        colors[code],
        "The major tasks in RE are elicitation, documentation, validation, and management of requirements. Tool support may help. Requirements analysis and conflict resolution are considered part of elicitation. To perform RE properly, a tailored RE process must be chosen.",
        "Az RE fő feladatai: követelmények feltárása, dokumentálása, érvényesítése és kezelése. A szerszámtámogatás (tool support) segíthet. A követelmények elemzése és a konfliktuskezelés a feltárás része. A RE megfelelő végrehajtásához a folyamatot testre kell szabni."
    )

elif section == "1.5 Role and Tasks of a Requirements Engineer":
    render_section(
        "1.5 Role and Tasks of a Requirements Engineer",
        icons[code],
        colors[code],
        "A Requirements Engineer is a role (not necessarily a job title) taken by those who elicit, document, validate, and manage requirements. They have in-depth knowledge of RE and bridge the gap between problems and potential solutions.",
        "A Requirements Engineer nem feltétlenül munkakör, hanem szerep, amit azok töltenek be, akik követelményeket gyűjtenek, dokumentálnak, érvényesítenek és kezelnek. Mély ismereteik vannak az RE-ről, és hidat képeznek a problémák és a lehetséges megoldások között."
    )

elif section == "1.6 What to Learn about RE":
    render_section(
        "1.6 What to Learn about Requirements Engineering",
        icons[code],
        colors[code],
        "The syllabus covers fundamental RE principles, documenting requirements in various ways, elaboration techniques, suitable processes, managing existing requirements, and tool support.",
        "Ez a tananyag lefedi az RE alapelveit, a követelmények dokumentálásának különféle formáit, a kibontás gyakorlatait, a megfelelő folyamatok használatát, a követelmények kezelését és az eszköztámogatást."
    )

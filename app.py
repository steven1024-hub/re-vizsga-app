import streamlit as st

# 🌐 Egységes megjelenítésű HTML szekciókhoz
def render_section(title, icon, color, content_en, content_hu):
    st.markdown(
    f"""
    <div style="background-color: {color};
                padding:1.5rem;
                border-radius:0.75rem;
                margin-bottom:2rem;
                border: 1px solid #ccc;
                box-shadow: 0px 3px 8px rgba(0,0,0,0.05);
                color: #2c3e50;">
        <h3>{icon} {title}</h3>
        <p><strong>EN:</strong> {content_en}</p>
        <p><strong>HU:</strong> {content_hu}</p>
    </div>
    """,
    unsafe_allow_html=True
)
# 💄 Modern üzleti megjelenés – világos háttér + sötét betűk
st.markdown("""
    <style>
        .stApp {
            background-image: url("https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/ERP_components_diagram.png/1200px-ERP_components_diagram.png");
            background-repeat: no-repeat;
            background-position: center center;
            background-size: contain;
            background-attachment: fixed;
            background-color: #f8fbff;
            font-family: 'Segoe UI', sans-serif;
            color: #2c3e50;
        }
        
        html, body {
            background-color: #f8fbff;
            color: #2c3e50;
        }
        h1, h2, h3, h4 {
            color: #2c3e50;
        }
        .stButton > button {
            background-color: #2f80ed;
            color: white;
            font-weight: 600;
            border-radius: 0.5rem;
            padding: 0.5rem 1rem;
        }
        /* Rádió kérdésdoboz */
        .stRadio > div {
            background-color: #ffffff;
            color: #2c3e50 !important;
            padding: 0.75rem;
            border-radius: 0.5rem;
            margin-bottom: 0.5rem;
            border: 1px solid #ddd;
        }

        /* A válaszopciók (label-ek) színe */
            .stRadio label {
                color: #2c3e50 !important;
                font-weight: 500;
        }  /* ⬅️ itt hiányzott a zárókapcsos zárás! */

    </style>

        /* Kérdés fejléc (ha van formában) */
        .stForm label {
            color: #2c3e50 !important;
        }

        /* Gombok */
        .stButton > button {
            background-color: #2f80ed;
            color: white;
            font-weight: 600;
            border-radius: 0.5rem;
            padding: 0.5rem 1rem;
        }

        .stSelectbox > div {
            background-color: #ffffffcc;
        }
        /* ⬅️ Új blokk: kérdéscímkék */
        .stRadio label {
            color: #2c3e50 !important;
            font-weight: 500;
    }

    </style>
""", unsafe_allow_html=True)

# Alapbeállítások
st.set_page_config(page_title="📘 RE Vizsgafelkészítő – Modul 1", layout="wide")
st.title("📘 Introduction and Overview of Requirements Engineering (Modul 1)")
st.markdown("#### 💡 Ismerd meg a Requirements Engineering alapjait – angolul és magyarul")

# Nézetválasztó
section = st.selectbox("Válassz nézetet:", [
    "📘 Elméleti áttekintés",
    "🎴 Tanulókártyák",
    "✅ Kérdőíves Vizsga"
])

# Színek és ikonok
colors = {
    "1.1": "#fdf8e3",  # halvány sárga
    "1.2": "#e6ffe6",  # halvány zöld
    "1.3": "#fff5cc",  # halvány sárga
    "1.4": "#f0e6ff",  # halvány lila
    "1.5": "#ffe6e6",  # halvány rózsaszín
    "1.6": "#f2f2f2"   # világosszürke
}

icons = {
    "1.1": "📘", "1.2": "💡", "1.3": "🌍", "1.4": "⚙️", "1.5": "👤", "1.6": "🎓"
}
# 📘 Elméleti áttekintés
if section == "📘 Elméleti áttekintés":
    chosen = st.selectbox("Válassz alfejezetet:", [
        "1.1 What is Requirements Engineering?",
        "1.2 Why is RE important?",
        "1.3 Where is RE applied?",
        "1.4 How is RE performed?",
        "1.5 Role and Tasks of a Requirements Engineer",
        "1.6 What to Learn about RE"
    ])
    code = chosen[:3]

    if chosen == "1.1 What is Requirements Engineering?":
        render_section(
            chosen, icons[code], colors[code],
            "Requirements Engineering (RE) is about specifying and managing what stakeholders need a system to do. It distinguishes between three types of requirements: functional, quality, and constraints.",
            "A Requirements Engineering (RE) célja a rendszerekkel szemben támasztott igények meghatározása és kezelése. Három fő követelménytípus létezik: funkcionális, minőségi, és korlátozó jellegű."
        )
    elif chosen == "1.2 Why is RE important?":
        render_section(
            chosen, icons[code], colors[code],
            "Good RE reduces the risk of developing the wrong system, improves understanding, supports estimation, and provides a basis for testing.",
            "A jó RE csökkenti a hibás rendszerfejlesztés kockázatát, javítja a problémamegértést, támogatja a becslést, és alapot ad a teszteléshez."
        )
    elif chosen == "1.3 Where is RE applied?":
        render_section(
            chosen, icons[code], colors[code],
            "RE is applied to any type of system, but especially where software, physical and organizational elements are involved.",
            "Az RE bármilyen típusú rendszernél alkalmazható, különösen ott, ahol szoftveres, fizikai és szervezeti elemek vannak jelen."
        )
    elif chosen == "1.4 How is RE performed?":
        render_section(
            chosen, icons[code], colors[code],
            "Main tasks in RE include elicitation, documentation, validation and management of requirements. Tailoring the RE process is essential.",
            "Az RE fő feladatai: követelmények feltárása, dokumentálása, érvényesítése és kezelése. A folyamat testreszabása elengedhetetlen."
        )
    elif chosen == "1.5 Role and Tasks of a Requirements Engineer":
        render_section(
            chosen, icons[code], colors[code],
            "RE is a role, not a job title. They elicit, document, validate and manage requirements while bridging the gap between problems and solutions.",
            "A Requirements Engineer egy szerep, nem feltétlenül munkakör. Követelményeket tárnak fel, dokumentálnak, érvényesítenek és kezelnek – hidat képeznek a probléma és a megoldás között."
        )
    elif chosen == "1.6 What to Learn about RE":
        render_section(
            chosen, icons[code], colors[code],
            "The syllabus includes principles of RE, documentation practices, elaboration techniques, processes, management, and tools.",
            "A tananyag lefedi az RE alapelveit, dokumentációs gyakorlatokat, kibontási technikákat, folyamatokat, menedzsmentet és eszközöket."
        )

# 🎴 Tanulókártyák
elif section == "🎴 Tanulókártyák":
    st.subheader("🧠 Tanulókártyás gyakorlás")
    flashcards = {
        "Mi a RE célja?": "A stakeholder-ek igényeinek meghatározása és kezelése.",
        "Miért fontos a RE?": "Csökkenti a hibakockázatot, támogatja a megértést és a tesztelhetőséget.",
        "Hol alkalmazzák a RE-t?": "Mindenféle rendszernél, főleg szoftverközpontú és komplex rendszerekben.",
        "Hogyan történik a RE?": "Feltárás, dokumentálás, érvényesítés, kezelés — testreszabott folyamatban.",
        "Ki a Requirements Engineer?": "Az a személy, aki a követelményeket összegyűjti, kezeli, és közvetít a problémák és megoldások között.",
        "Mit kell megtanulni RE-ből?": "Elveket, dokumentálási módszereket, kibontást, folyamatokat, menedzsmentet, eszközöket."
    }

    for question, answer in flashcards.items():
        with st.expander(f"❓ {question}"):
            st.write(f"✅ {answer}")
# ✅ Kérdőíves Vizsga
elif section == "✅ Kérdőíves Vizsga":
    st.subheader("✅ Kérdőíves vizsga – Modul 1")
    score = 0
    total = 6

    with st.form("modul1_quiz"):
        st.write("Válaszolj a következő kérdésekre:")

        q1 = st.radio("1. Mi a Requirements Engineering elsődleges célja?", [
            "Rendszerek tesztelése és karbantartása",
            "Stakeholder-ek igényeinek meghatározása és kezelése",
            "Projektköltségek kiszámítása"
        ])

        q2 = st.radio("2. Mi jellemző a jó RE-re?", [
            "Csak a fejlesztés végén kezdődik",
            "Minimalizálja a dokumentációt",
            "Csökkenti a hibakockázatot, segíti a megértést és a becslést"
        ])

        q3 = st.radio("3. Milyen rendszerekre alkalmazható RE?", [
            "Csak webes alkalmazásokra",
            "Mindenféle rendszerre, különösen komplex szoftveres rendszerekre",
            "Kizárólag üzleti szoftverekre"
        ])

        q4 = st.radio("4. Melyik NEM tartozik az RE fő tevékenységei közé?", [
            "Követelmények feltárása",
            "Kódoptimalizálás",
            "Követelmények érvényesítése"
        ])

        q5 = st.radio("5. Milyen szerepet tölt be a Requirements Engineer?", [
            "Hardvertechnikus",
            "A problémák és megoldások közötti kapcsolatot teremti meg",
            "Marketing asszisztens"
        ])

        q6 = st.radio("6. Mit ölel fel az RE alapszintű tananyaga?", [
            "Projektmenedzsment és erőforrás-allokáció",
            "Tesztelési stratégiák és hibakeresés",
            "RE alapelvek, dokumentálás, kibontás, folyamatok, menedzsment, eszközök"
        ])

        submitted = st.form_submit_button("Eredmények megtekintése")

    if submitted:
        # Értékelés
        if q1 == "Stakeholder-ek igényeinek meghatározása és kezelése": score += 1
        if q2 == "Csökkenti a hibakockázatot, segíti a megértést és a becslést": score += 1
        if q3 == "Mindenféle rendszerre, különösen komplex szoftveres rendszerekre": score += 1
        if q4 == "Kódoptimalizálás": score += 1
        if q5 == "A problémák és megoldások közötti kapcsolatot teremti meg": score += 1
        if q6 == "RE alapelvek, dokumentálás, kibontás, folyamatok, menedzsment, eszközök": score += 1

        percent = round((score / total) * 100)
        st.subheader(f"🎯 Eredményed: {score}/{total} – {percent}%")

        # Feedback blokk
        if percent == 100:
            st.success("🌟 Gratulálunk! Teljesítetted a Modul 1 összes kérdését hibátlanul!")
            st.balloons()
            st.markdown("### 🎓 **Modul 1 teljesítve!**\n\nKiváló alapokat szereztél a következő témakörhöz.")
        elif percent >= 80:
            st.success("🎉 Nagyon jó! Már csak egy kis finomhangolás van hátra.")
        elif percent >= 60:
            st.warning("🙂 Jó úton jársz, de érdemes még egy kicsit átnézni a tananyagot.")
        else:
            st.error("😅 Ne csüggedj! A tanulókártyák segíthetnek az ismétlésben.")

        st.markdown("---")
        st.markdown("👉 **Tipp**: Próbáld ki újra a tanulókártyákat vagy nézd át az elméleti összefoglalót, mielőtt továbblépnél a 2. modulra.")

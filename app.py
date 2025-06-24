import streamlit as st
if "modul_state" not in st.session_state:
    st.session_state["modul_state"] = 1

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
                    color: #ffffff;">
            <h3>{icon} {title}</h3>
            <p><strong>EN:</strong> {content_en}</p>
            <p><strong>HU:</strong> {content_hu}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# 💄 Modern üzleti megjelenés – navy blue háttér + világos tartalom
st.markdown("""
    <style>
        .stApp {
            background-color: #001f3f;
            font-family: 'Segoe UI', sans-serif;
            color: #fffdd0;
        }

        html, body {
            background-color: #001f3f;
            color: #ffffff;
        }

        h1, h2, h3, h4 {
            color: #fffdd0;
        }

        .stButton > button {
            background-color: #2f80ed;
            color: white;
            font-weight: 600;
            border-radius: 0.5rem;
            padding: 0.5rem 1rem;
        }

        .stRadio > div {
            background-color: #003366;
            color: #ffffff;
            padding: 0.75rem;
            border-radius: 0.5rem;
            margin-bottom: 0.5rem;
            border: 1px solid #4d648d;
        }

        .stRadio label {
            color: #fffdd0 !important;
            font-weight: 500;
        }

        .stForm label {
            color: #ffffff !important;
        }

        .stSelectbox > div {
            background-color: #ffffff10;
            color: #ffffff;
        }
    </style>
""", unsafe_allow_html=True)

# Alapbeállítások
st.set_page_config(page_title="📘 RE Vizsgafelkészítő – Modul 1", layout="wide")
# Dinamikus fejléc és nézetopciók
if "modul1_completed" not in st.session_state:
    st.session_state["modul1_completed"] = False

if st.session_state["modul_state"] == 1:
    st.title("📘 Introduction and Overview of Requirements Engineering (Modul 1)")
    st.markdown("#### 💡 Ismerd meg a Requirements Engineering alapjait – angolul és magyarul")
    options = ["📄 Elméleti áttekintés", "🎴 Tanulókártyák", "✅ Kérdőíves Vizsga"]
    
elif st.session_state["modul_state"] == 2:
    st.title("📗 Fundamental Principles of RE (Modul 2)")
    st.markdown("#### 💡 A Requirements Engineering univerzális alapelvei – angolul és magyarul")
    options = ["📄 Elméleti áttekintés", "🎴 Tanulókártyák", "✅ Kérdőíves Vizsga", "🔙 Vissza Modul 1-re"]

# Ez a választó komponens jeleníti meg a felületet
view = st.radio("🔍 Nézetválasztó", options)

# Visszalépés lehetősége Modul 1-re
if view == "🔙 Vissza Modul 1-re":
    st.info("🔄 Visszaváltottál a Modul 1-re.")
    st.session_state["modul_state"] = 1
    st.rerun()

if "go_to_second_block" not in st.session_state:
    st.session_state["go_to_second_block"] = False
if "jump_triggered" not in st.session_state:
    st.session_state["jump_triggered"] = False

if st.button("Ugrás a 2. blokkra") and not st.session_state["jump_triggered"]:
    st.session_state["go_to_second_block"] = True
    st.session_state["jump_triggered"] = True
    st.rerun()

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
if view == "📄 Elméleti áttekintés":
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
            chosen, icons[code], "#3d5c3d",
            "Requirements Engineering (RE) is the systematic process of discovering, analyzing, documenting, validating, and managing the requirements of a system. It aims to ensure that the system to be developed meets the desires and needs of its stakeholders. RE distinguishes between functional requirements (what the system should do), quality requirements (how well it should perform), and constraints (limitations on the solution space).",
            "A Requirements Engineering (RE) egy strukturált folyamat, amely magában foglalja a követelmények feltárását, elemzését, dokumentálását, érvényesítését és kezelését. Célja, hogy a fejlesztendő rendszer megfeleljen az érintettek igényeinek és elvárásainak. Az RE megkülönbözteti a funkcionális követelményeket (mit kell tennie a rendszernek), a minőségi követelményeket (milyen szinten kell teljesítenie), valamint a korlátozásokat (a megoldási térre vonatkozó megszorítások)."
        )

    elif chosen == "1.2 Why is RE important?":
        render_section(
            chosen, icons[code], "#3d5c3d",
            "Adequate RE reduces the risk of developing the wrong system, improves understanding of the problem, supports estimation of effort and cost, and provides a basis for testing. Inadequate RE often leads to missing, unclear, or incorrect requirements due to rushed implementation, poor communication, or lack of RE skills.",
            "A megfelelő RE csökkenti annak kockázatát, hogy hibás rendszert fejlesszünk, javítja a probléma megértését, támogatja a ráfordítás és költség becslését, valamint alapot ad a teszteléshez. Az elégtelen RE gyakran hiányzó, homályos vagy hibás követelményekhez vezet, amit sietség, kommunikációs problémák vagy a RE ismeretének hiánya okoz."
        )

    elif chosen == "1.3 Where is RE applied?":
        render_section(
            chosen, icons[code], "#3d5c3d",
            "RE is applicable to any kind of system, especially those involving software, physical components, and organizational elements. Requirements can be categorized as system, stakeholder, user, domain, or business requirements, depending on their origin and perspective.",
            "Az RE bármilyen típusú rendszerre alkalmazható, különösen olyanokra, amelyek szoftveres, fizikai és szervezeti elemeket tartalmaznak. A követelmények lehetnek rendszer-, stakeholder-, felhasználói-, domain- vagy üzleti követelmények, attól függően, hogy honnan származnak és milyen nézőpontot képviselnek."
        )

    elif chosen == "1.4 How is RE performed?":
        render_section(
            chosen, icons[code], "#3d5c3d",
            "The main RE tasks include elicitation, documentation, validation, and management of requirements. These tasks are supported by tools and must be tailored to the specific context. Conflict resolution and analysis are also part of the elicitation process.",
            "Az RE fő feladatai a követelmények feltárása, dokumentálása, érvényesítése és kezelése. Ezeket a feladatokat eszközök is támogathatják, és a konkrét környezethez kell igazítani őket. A konfliktuskezelés és elemzés szintén a feltárási folyamat része."
        )

    elif chosen == "1.5 Role and Tasks of a Requirements Engineer":
        render_section(
            chosen, icons[code], "#3d5c3d",
            "A Requirements Engineer is a role (not necessarily a job title) responsible for eliciting, documenting, validating, and managing requirements. They bridge the gap between problems and solutions and often collaborate with stakeholders, developers, and analysts.",
            "A Requirements Engineer egy szerep (nem feltétlenül munkakör), aki a követelmények feltárásáért, dokumentálásáért, érvényesítéséért és kezeléséért felel. Ő képezi a hidat a problémák és a megoldások között, és gyakran működik együtt érintettekkel, fejlesztőkkel és elemzőkkel."
        )

    elif chosen == "1.6 What to Learn about RE":
        render_section(
            chosen, icons[code], "#3d5c3d",
            "The CPRE syllabus covers RE principles, documentation techniques, elaboration practices, process configuration, requirements management, and tool support. It provides a foundational skill set for anyone involved in RE.",
            "A CPRE tananyag lefedi az RE alapelveit, dokumentációs technikáit, kibontási gyakorlatokat, folyamatkonfigurációt, követelménykezelést és eszköztámogatást. Ez egy alapvető készségkészletet biztosít minden RE-ben érintett számára."
        )


# 🎴 Tanulókártyák
elif view == "🎴 Tanulókártyák":
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
elif view  == "✅ Kérdőíves Vizsga":
    st.subheader("✅ Kérdőíves vizsga – Modul 1")
    score = 0
    total = 6

    with st.form("modul1_quiz"):
        st.markdown("### ❓ Válaszolj az alábbi kérdésekre:")

        q1 = st.radio("1️⃣ Mi a Requirements Engineering elsődleges célja?", [
            "Rendszerek tesztelése és karbantartása",
            "Stakeholder-ek igényeinek meghatározása és kezelése",
            "Projektköltségek kiszámítása"
        ], key="q1")

        q2 = st.radio("2️⃣ Mi jellemző a jó RE-re?", [
            "Csak a fejlesztés végén kezdődik",
            "Minimalizálja a dokumentációt",
            "Csökkenti a hibakockázatot, segíti a megértést és a becslést"
        ], key="q2")

        q3 = st.radio("3️⃣ Milyen rendszerekre alkalmazható RE?", [
            "Csak webes alkalmazásokra",
            "Mindenféle rendszerre, különösen komplex szoftveres rendszerekre",
            "Kizárólag üzleti szoftverekre"
        ], key="q3")

        q4 = st.radio("4️⃣ Melyik NEM tartozik az RE fő tevékenységei közé?", [
            "Követelmények feltárása",
            "Kódoptimalizálás",
            "Követelmények érvényesítése"
        ], key="q4")

        q5 = st.radio("5️⃣ Milyen szerepet tölt be a Requirements Engineer?", [
            "Hardvertechnikus",
            "A problémák és megoldások közötti kapcsolatot teremti meg",
            "Marketing asszisztens"
        ], key="q5")

        q6 = st.radio("6️⃣ Mit ölel fel az RE alapszintű tananyaga?", [
            "Projektmenedzsment és erőforrás-allokáció",
            "Tesztelési stratégiák és hibakeresés",
            "RE alapelvek, dokumentálás, kibontás, folyamatok, menedzsment, eszközök"
        ], key="q6")

        submitted = st.form_submit_button("📊 Eredmény megtekintése")

    if submitted:
        if q1 == "Stakeholder-ek igényeinek meghatározása és kezelése": score += 1
        if q2 == "Csökkenti a hibakockázatot, segíti a megértést és a becslést": score += 1
        if q3 == "Mindenféle rendszerre, különösen komplex szoftveres rendszerekre": score += 1
        if q4 == "Kódoptimalizálás": score += 1
        if q5 == "A problémák és megoldások közötti kapcsolatot teremti meg": score += 1
        if q6 == "RE alapelvek, dokumentálás, kibontás, folyamatok, menedzsment, eszközök": score += 1

        percent = round((score / total) * 100)
        st.subheader(f"🎯 Eredményed: {score}/{total} – {percent}%")
        
        if score >= 5:
            st.success("✅ Teljesítetted az 1. modult — feloldva a következő szint!")
            st.session_state["modul1_completed"] = True
            st.session_state["modul_state"] = 2
            st.rerun()

        else:
            st.warning("🔒 A modul 2 csak akkor elérhető, ha legalább 5 helyes válaszod van.")
        
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
        st.markdown("👉 Tipp: Próbáld ki újra a tanulókártyákat vagy nézd át az elméleti összefoglalót, mielőtt továbblépsz a 2. modulra.")
# 📗 Modul 2 – csak akkor választható, ha előző modul teljesült
elif st.session_state["modul_state"] == 2:
    if view == "📄 Elméleti áttekintés":
        st.subheader("📗 Modul 2 – Elméleti áttekintés")
        st.markdown("✅ Ez a szakasz részletesen bemutatja az RE kilenc alapelvét és azok gyakorlati alkalmazását.")
        # Első blokk
        render_section("Harmadik blokk", "🎯", "#cc3344", "Third block EN", "Harmadik blokk HU")
        render_section("2.1 Overview of Principles", "📗", "#3d5c3d", "Requirements Engineering is governed by nine universal principles: value-orientation, stakeholder orientation, shared understanding, context awareness, separation of concerns between problems, requirements and solutions, validation, evolution, innovation, and systematic work. These principles apply across RE tasks, regardless of domain or method.", "A Requirements Engineering kilenc univerzális alapelv mentén működik: értékorientáltság, stakeholder-központúság, közös megértés, kontextus-tudatosság, a problémák, követelmények és megoldások szétválasztása, érvényesítés, változáskezelés, innováció, valamint rendszerszemléletű és fegyelmezett munka.")
        render_section("2.2 Stakeholder needs and shared understanding", "👥", "#3d5c3d", "Successful RE is grounded in understanding and satisfying stakeholder needs. It establishes shared understanding among stakeholders, developers and Requirements Engineers, through explicit documentation and trust-building practices.", "A sikeres RE alapja a stakeholderek igényeinek mély megértése és kielégítése. A közös megértést kifejezett dokumentáción, visszacsatoláson és a bizalom kialakításán keresztül valósítja meg a stakeholderek, fejlesztők és RE-szakemberek között.")
        render_section("2.3 Context and system boundaries", "🌐", "#3d5c3d","RE considers the system in its context. Understanding what is inside and outside the system boundary is critical. External actors, regulations and assumptions about the environment must be captured.", "Az RE a rendszert annak környezetében értelmezi. Fontos tisztázni, mi esik a rendszer határain belül és kívül. A külső szereplők, szabályozások és a kontextusra vonatkozó feltételezések rögzítése kulcsfontosságú.")
        render_section("2.4 Managing change and fostering innovation", "♻️", "#3d5c3d", "Requirements evolve. RE must embrace change while maintaining traceability and consistency. Beyond fulfilling explicit needs, RE should strive to surprise and delight users through innovative solutions.", "A követelmények változnak. Az RE-nek fel kell készülnie a változások kezelésére, miközben biztosítja a nyomon követhetőséget és a konzisztenciát. Az RE célja nem csupán a kifejezett igények teljesítése, hanem az is, hogy innovatív megoldásokkal örömet szerezzen a felhasználóknak.")
        render_section("2.5 Disciplined and adaptive RE practices", "🛠️", "#3d5c3d", "RE requires systematic analysis and continuous validation.", "A RE módszeres elemzést és folyamatos validálást igényel.")
       
    elif view == "🎴 Tanulókártyák":
        st.subheader("📗 Modul 2 – Tanulókártyák")
        st.markdown("💡 Kérdés–válasz alapú segédlet a kilenc alapelvhez. (Ide jöhet majd a kártyalista.)")

    elif view == "✅ Kérdőíves Vizsga":
        st.subheader("📗 Modul 2 – Kérdőív")
        st.markdown("🧪 A második modulhoz tartozó kérdőív itt jelenik meg.")
        # Ide kerülhet a második kérdőív logikája később

    elif view == "🔙 Vissza Modul 1-re":
        st.info("🔄 Visszaváltottál az első modulra.")
        st.session_state["modul_state"] = 1
        st.rerun()
        


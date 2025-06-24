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
    view = st.radio("🔍 Nézetválasztó", options)

    if view == "📄 Elméleti áttekintés":
        st.subheader("📗 Modul 2 – Elméleti áttekintés")
        alapelvek = {
            "2.1 RE alapelvek áttekintése": "RE is governed by a set of nine fundamental principles...",
            "2.2 Értékorientáció": "Requirements are a means to an end, not an end in itself...",
            "2.3 Stakeholderek központúsága": "RE is about satisfying stakeholders’ desires and needs...",
            "2.4 Közös megértés": "RE fosters shared understanding between stakeholders...",
            "2.5 Kontextus-függőség": "Systems cannot be understood in isolation...",
            "2.6 Probléma–Követelmény–Megoldás": "Problem, requirement, and solution are intertwined...",
            "2.7 Validálás": "Non-validated requirements are useless...",
            "2.8 Evolúció": "Changing requirements are the normal case...",
            "2.9 Innováció és fegyelmezettség": "Good RE includes innovation and systematic discipline..."}
            selected = st.selectbox("📘 Alapelv kiválasztása:", list(alapelvek.keys()))
            render_section(selected, "📗", "#3d5c3d", alapelvek[selected], "🔄 A magyar változat itt lesz.")

    elif view == "🎴 Tanulókártyák":
        st.subheader("📗 Modul 2 – Tanulókártyák")
        flashcards = {
            "Mit jelent az értékorientáció?": "A követelmények eszközök a cél eléréséhez, nem öncélúak.",
            "Miért fontos a stakeholderek kezelése?": "RE célja a stakeholderek igényeinek kielégítése.",
            "Mi a közös megértés lényege?": "Dokumentált és implicit egyezés a résztvevők között.",
            "Mi a kontextus szerepe?": "A rendszert környezetében kell értelmezni, nem elszigetelten.",
            "Mi az RE három összefüggő fogalma?": "Probléma – Követelmény – Megoldás szétválasztása.",
            "Mit értünk validálás alatt?": "Az igények teljesülésének igazolása már a RE során.",
            "Miért természetes a követelmények evolúciója?": "Külső és belső tényezők miatt változnak az igények.",
            "Mit jelent az innováció az RE-ben?": "A stakeholderek elvárásait felülmúló megoldások keresése.",
            "Mi a rendszerszemlélet szerepe?": "Fegyelmezett és célhoz illesztett RE gyakorlat kialakítása."}
            for k, v in flashcards.items():
                with st.expander(f"❓ {k}"):
                    st.write(f"✅ {v}")

    elif view == "✅ Kérdőíves Vizsga":
        st.subheader("📗 Modul 2 – Kérdőíves vizsga")
        st.markdown("🧪 Ez a blokk még fejlesztés alatt áll – hamarosan ide kerül a második modul kérdéssora!")

    elif view == "🔙 Vissza Modul 1-re":
        st.info("🔄 Visszaváltottál az első modulra.")
        st.session_state["modul_state"] = 1
        st.rerun()

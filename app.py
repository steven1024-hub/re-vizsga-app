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
            "2.1 RE alapelvek áttekintése": "...",
            "2.2 Értékorientáció": "...",
            # ...
        }
        selected = st.selectbox("📘 Alapelv kiválasztása:", list(alapelvek.keys()))
        render_section(selected, "📗", "#3d5c3d", alapelvek[selected], "🔄 A magyar fordítás itt lesz.")

    elif view == "🎴 Tanulókártyák":
        st.subheader("📗 Modul 2 – Tanulókártyák")
        flashcards = {
            "Mi a közös megértés?": "Dokumentált és implicit egyezés a szereplők között.",
            # ...
        }
        for k, v in flashcards.items():
            with st.expander(f"❓ {k}"):
                st.write(f"✅ {v}")

    elif view == "✅ Kérdőíves Vizsga":
        st.subheader("📗 Modul 2 – Kérdőíves vizsga")
        st.markdown("🧪 Ez a blokk még fejlesztés alatt áll — hamarosan jönnek a kérdések!")

    elif view == "🔙 Vissza Modul 1-re":
        st.session_state["modul_state"] = 1
        st.rerun()


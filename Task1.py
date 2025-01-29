import streamlit as st
import pandas as pd

# Initialisation de la session pour stocker les tâches
if "taches" not in st.session_state:
    st.session_state["taches"] = pd.DataFrame(columns=["Nom", "Description", "Priorité", "Statut", "Responsable", "Date de début", "Date d'échéance", "Progrès (%)", "Commentaires"])

st.title("📋 Gestion Interactive des Tâches")

# Formulaire pour ajouter une tâche
with st.form("ajouter_tache"):
    st.subheader("Ajouter une Nouvelle Tâche")
    nom = st.text_input("Nom de la tâche", "")
    description = st.text_area("Description", "")
    priorite = st.selectbox("Priorité", ["Haute", "Moyenne", "Basse"])
    statut = st.selectbox("Statut", ["À faire", "En cours", "Terminé"])
    responsable = st.text_input("Responsable", "")
    date_debut = st.date_input("Date de début")
    date_echeance = st.date_input("Date d'échéance")
    progres = st.slider("Progrès (%)", 0, 100, 0)
    commentaires = st.text_area("Commentaires", "")
    submit = st.form_submit_button("Ajouter la Tâche")

if submit and nom:
    new_task = pd.DataFrame([[nom, description, priorite, statut, responsable, date_debut, date_echeance, progres, commentaires]],
                             columns=st.session_state["taches"].columns)
    st.session_state["taches"] = pd.concat([st.session_state["taches"], new_task], ignore_index=True)
    st.success("Tâche ajoutée avec succès !")

# Affichage des tâches
st.subheader("📊 Liste des Tâches")
if not st.session_state["taches"].empty:
    for index, row in st.session_state["taches"].iterrows():
        with st.expander(f"🔹 {row['Nom']} - {row['Statut']}"):
            st.write(f"**Description :** {row['Description']}")
            st.write(f"**Priorité :** {row['Priorité']}")
            st.write(f"**Responsable :** {row['Responsable']}")
            st.write(f"**Date de début :** {row['Date de début']}")
            st.write(f"**Date d'échéance :** {row['Date d'échéance']}")
            st.write(f"**Progrès :** {row['Progrès (%)']}%")
            st.write(f"**Commentaires :** {row['Commentaires']}")
            
            if st.button(f"🗑 Supprimer la tâche {index}", key=f"delete_{index}"):
                st.session_state["taches"] = st.session_state["taches"].drop(index).reset_index(drop=True)
                st.experimental_rerun()
else:
    st.info("Aucune tâche enregistrée.")

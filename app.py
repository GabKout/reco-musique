import streamlit as st
import math

# Donn\u00e9es de base (artistes et user_profiles, comme d\u00e9fini ci-dessus)
artists = ["Aya Nakamura", "Ang\u00e8le", "Orelsan", "Stromae",
           "Ed Sheeran", "Taylor Swift", "Jean-Jacques Goldman", "Johnny Hallyday"]
user_profiles = {
    "Alice":    [5, 4, 4, 3, 2, 1, 0, 0],
    "Benjamin": [0, 0, 1, 0, 0, 0, 5, 5],
    "Charlie":  [4, 4, 3, 4, 3, 2, 1, 1],
    "Dani":     [1, 0, 1, 0, 5, 5, 0, 0],
    "Élodie":   [0, 3, 0, 5, 0, 0, 4, 2],
    "Farid":    [2, 0, 5, 3, 0, 0, 3, 1]
}

def cosine_similarity(prof1, prof2):
    dot = 0; norm1 = 0; norm2 = 0
    for x, y in zip(prof1, prof2):
        dot += x*y; norm1 += x*x; norm2 += y*y
    return 0.0 if norm1==0 or norm2==0 else dot / math.sqrt(norm1*norm2)

def get_recommendations(target, threshold):
    target_prof = user_profiles[target]
    # Trouver le voisin le plus similaire
    best_user, best_sim = None, -1
    for other, prof in user_profiles.items():
        if other == target:
            continue
        sim = cosine_similarity(target_prof, prof)
        if sim > best_sim:
            best_sim = sim
            best_user = other
    # Calculer les recommandations
    recs = []
    for idx, score in enumerate(user_profiles[best_user]):
        if target_prof[idx] == 0 and score >= threshold:
            recs.append(artists[idx])
    return best_user, best_sim, recs

# Interface Streamlit
st.title("🎵 Recommandation musicale - mini Spotify")
st.markdown("Ce mini outil vous permet d'explorer les recommandations bas\u00e9es sur les go\u00fbts de 6 utilisateurs fictifs.")
user = st.selectbox("Choisissez un utilisateur :", list(user_profiles.keys()))
threshold = st.slider("Seuil d'appr\u00e9ciation (pour recommander un artiste)", 1, 5, 4)

if user:
    neighbor, sim, recs = get_recommendations(user, threshold)
    st.write(f"**Utilisateur le plus similaire \u00e0 {user}** : {neighbor} (score cosinus = {sim:.2f})")
    if recs:
        st.write("**Artistes recommand\u00e9s :** " + ", ".join(recs))
    else:
        st.write("*(Aucune recommandation suppl\u00e9mentaire \u00e0 proposer avec ces param\u00e8tres.)*")

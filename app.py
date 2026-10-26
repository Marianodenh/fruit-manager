import streamlit as st  
from fruit_manager import * 

def vendre(inventaire, fruit, quantite, tresorerie, prix):
    if inventaire.get(fruit, 0) >= quantite:
        inventaire[fruit] -= quantite
        tresorerie += prix.get(fruit, 0) * quantite
        st.success(f"\n💰 vendu {quantite} {fruit}")
        return (inventaire, tresorerie)
    else: 
        st.error(f"\n.❌ Pas assez de {fruit} pour vendre {quantite} unités.")
        return (inventaire, tresorerie)

def recolter(inventaire, fruit, quantite):
    inventaire[fruit] = inventaire.get(fruit, 0) + quantite
    st.info(f"✅ Récolté {quantite} {fruit} supplémentaire")
    return inventaire

st.title("🍇 Dashbord de la plantation")

if "inventaire" not in st.session_state:
    st.session_state.inventaire = ouvrir_inventaire()  
inventaire = ouvrir_inventaire()

if "prix" not in st.session_state:
    st.session_state.prix = ouvrir_prix()
prix = ouvrir_prix()

if "tresorerie" not in st.session_state:
    st.session_state.tresorerie = ouvrir_tresorerie()
tresorerie = ouvrir_tresorerie()

st.header("💰 Trésorerie")
st.metric(label="Montant disponible", value=f"{tresorerie:.2f} $")

st.header("🧺 Inventaire")
st.table(inventaire)

st.header("💲 Prix unitaire")
st.table(prix)

# Vendre un fruit
if "choix_fruit" not in st.session_state:
    st.session_state.choix_fruit = None
    
if "nbr_vendu" not in st.session_state:
    st.session_state.nbr_vendu = 1


st.sidebar.title("🛒 Vendre des fruits")
with st.sidebar.form("my vente"):
    choix = st.selectbox("Choisir un fruit", ["Bananes", "Mangues", "Ananas", "Noix de coco", "Papayes"], key="choix_fruit")
    quantite = st.number_input("Quantié à vendre", min_value=1, step=1, key="nbr_vendu")
    submit_button = st.form_submit_button("Vendre")
    
if submit_button:
    inventaire, tresorerie = vendre(inventaire, choix.lower(), quantite, tresorerie, prix)
    ecrire_inventaire(inventaire)
    ecrire_tresorerie(tresorerie)
    st.rerun()
    

# Récolter un fruit   
if "fruit_recolter" not in st.session_state:
    st.session_state.fruit_recolter = None
    
if "nbr_recolter" not in st.session_state:
    st.session_state.nbr_recolter = 0


st.sidebar.title("🌱 Récolter des fruits")
with st.sidebar.form("my recolte"):
    ch = st.selectbox("Choisir un fruit", ["Bananes", "Mangues", "Ananas", "Noix de coco", "Papayes"], key="fruit_recolter")
    quantite = st.number_input("Quantié à vendre", min_value=0, step=1, key="nbr_recolter")
    submit_button_recolte = st.form_submit_button("Récolter")
    
if submit_button_recolte:
    inventaire= recolter(inventaire, ch.lower(), quantite)
    ecrire_inventaire(inventaire)
    st.rerun()
    

    
    
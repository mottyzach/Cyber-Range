import streamlit as st
import json
from datetime import datetime

st.title("⚔️ Attack Simulator")

attack_mode = st.selectbox("Select Attack", ["BruteForce", "DoS", "PortScan"])

if st.button("Launch Attack"):
    attack = attack_mode.lower()

    try:
        with open("shared_state.json") as f:
            data = json.load(f)
    except:
        data = {"logs": []}

    data["attack_type"] = attack
    data["timestamp"] = str(datetime.now())

    with open("shared_state.json", "w") as f:
        json.dump(data, f)

    st.success(f"Attack sent: {attack}")

st.markdown("---")

st.info("This module only generates attacks.\nLogs are handled by Defense System.")
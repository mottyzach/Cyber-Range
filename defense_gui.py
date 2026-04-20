import streamlit as st
import json
import time
from datetime import datetime

st.title("🛡️ Defense System")

status_area = st.empty()
log_area = st.empty()

fail_count = 0

while True:
    try:
        with open("shared_state.json") as f:
            data = json.load(f)

        attack = data.get("attack_type", "none")

        if attack != "none":
            fail_count += 1

        blocked = False
        if fail_count >= 3:
            blocked = True

        # Create log entry
        log_entry = f"[{datetime.now()}] Detected {attack} | Attempts: {fail_count} | Blocked: {blocked}"

        if "logs" not in data:
            data["logs"] = []

        data["logs"].append(log_entry)

        # Write back logs
        with open("shared_state.json", "w") as f:
            json.dump(data, f)

        # UI update
        status_area.write(f"""
        **Attack:** {attack}  
        **Attempts:** {fail_count}  
        **Blocked:** {blocked}
        """)

        log_area.text("\n".join(data["logs"][-25:]))

    except:
        pass

    time.sleep(2)
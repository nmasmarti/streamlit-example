import streamlit as st
import time

progress_text = "Operació en progres. Espereu, si-us-plau."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1, text=progress_text)

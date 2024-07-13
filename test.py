import streamlit as st

# Initialize the session state to store text inputs
if "text_inputs" not in st.session_state:
    st.session_state.text_inputs = []

# Function to add a new text_input
def add_text_input():
    st.session_state.text_inputs.append("")

# Add button to add a new text_input widget
if st.button("Add Text Input"):
    add_text_input()

# Display all text_input widgets
for i, text_input in enumerate(st.session_state.text_inputs):
    st.session_state.text_inputs[i] = st.text_input(f"Input {i + 1}", value=text_input, key=f"text_input_{i}")

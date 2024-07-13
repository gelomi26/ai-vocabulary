import streamlit as st
import langchain_helper as lch

st.title("Voca Note")

# Function to add a new text_input for sentences
def add_sentence_input():
    if st.session_state.sentence_inputs[-1]:  # Only add if the last input is not empty
        st.session_state.sentence_inputs.append("")

# Initialize session state for sentence inputs
if "sentence_inputs" not in st.session_state:
    st.session_state.sentence_inputs = [""]  # Initialize with one empty input

# # Initialize session state for validation message
# if "validation_message" not in st.session_state:
#     st.session_state.validation_message = ""

# Form for word input and actions
with st.form(key='word_form'):
    col1, col2 = st.columns(2)

    with col1:
        input_word = st.text_input(
            label="Word",
            value="",
            max_chars=50,
            placeholder="Write the word here"
        )

    with col2:
        st.form_submit_button(label="Generate")

    input_pronunciation = st.text_input(
        label="Pronunciation",
        max_chars=75,
        placeholder="Write the pronunciation of the word"
    )

    input_meaning = st.text_area(
        label="Meaning",
        max_chars=500,
        placeholder="Write the meaning of the word"
    )

    st.file_uploader("Images", type=["png", "jpg", "heic", "pdf"], accept_multiple_files=True)

    for i, sentence in enumerate(st.session_state.sentence_inputs):
        st.session_state.sentence_inputs[i] = st.text_input(
            f"Sentence {i + 1}",
            value=sentence,
            placeholder="Write an example sentence of the word",
            key=f"sentence_input_{i}"
        )

    if st.form_submit_button(label="Add Another Sentence"):
        add_sentence_input()

    submitted = st.form_submit_button(label="Save")
    # Validation logic moved outside the form
    if submitted:
        if not input_word:
            st.warning("Word field cannot be empty.")
        elif not input_meaning:
            st.warning("Meaning field cannot be empty.")
        elif not all(sentence for sentence in st.session_state.sentence_inputs):
            st.warning("All sentence fields must be filled.")
        else:
            st.success("Form submitted successfully!")

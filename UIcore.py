
from langchain_mistralai import ChatMistralAI
import streamlit as st

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

st.title("🎬 CineSage")

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert AI assistant for information extraction.
"""
        ),

        (
            "human",
            """
Paragraph:
{text}
"""
        )
    ]
)

user_input = st.text_area(
    "Enter paragraph"
)

model = ChatMistralAI(
    model="mistral-small"
)

if st.button("Analyze"):

    final_prompt = prompt.invoke(
        {
            "text": user_input
        }
    )

    response = model.invoke(final_prompt)

    st.subheader("Extracted Information")

    st.write(response.content)

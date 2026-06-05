
import streamlit as st

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI

from pydantic import BaseModel
from typing import List, Optional

# ---------------- LOAD ENV ---------------- #

load_dotenv()

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="CineSage",
    page_icon="🎬",
    layout="centered"
)

# ---------------- TITLE ---------------- #

st.title("🎬 CineSage")
st.markdown("AI Powered Movie Information Extractor")

# ---------------- MODEL ---------------- #

model = ChatMistralAI(
    model="mistral-small-2506"
)

# ---------------- PYDANTIC MODEL ---------------- #

class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

# ---------------- OUTPUT PARSER ---------------- #

parser = PydanticOutputParser(
    pydantic_object=Movie
)

# ---------------- PROMPT ---------------- #

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
Extract movie information from the given paragraph.

{format_instructions}
"""
        ),

        (
            "human",
            "{paragraph}"
        )
    ]
)

# ---------------- INPUT ---------------- #

user_input = st.text_area(
    "Enter Movie Paragraph",
    height=250,
    placeholder="Paste movie description here..."
)

# ---------------- BUTTON ---------------- #

if st.button("Analyze"):

    if user_input.strip() == "":
        st.warning("Please enter a paragraph.")

    else:

        with st.spinner("Analyzing..."):

            final_prompt = prompt.invoke(
                {
                    "paragraph": user_input,
                    "format_instructions": parser.get_format_instructions()
                }
            )

            response = model.invoke(final_prompt)

            parsed_output = parser.parse(
                response.content
            )

        # ---------------- OUTPUT ---------------- #

        st.subheader("Extracted Movie Information")

        st.write(f"🎬 Title: {parsed_output.title}")

        st.write(
            f"📅 Release Year: {parsed_output.release_year}"
        )

        st.write(
            f"🎭 Genre: {', '.join(parsed_output.genre)}"
        )

        st.write(
            f"🎬 Director: {parsed_output.director}"
        )

        st.write(
            f"⭐ Rating: {parsed_output.rating}"
        )

        st.write(
            f"👥 Cast: {', '.join(parsed_output.cast)}"
        )

        st.write(
            f"📝 Summary: {parsed_output.summary}"
        )


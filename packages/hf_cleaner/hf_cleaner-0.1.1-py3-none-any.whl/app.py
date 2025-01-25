import streamlit as st
from hf_cleaner.templates.DefaultTemplate import DefaultTemplate


def main():
    st.set_page_config(
        page_title="HF Cache Cleaner",
        page_icon="🧹",
        layout="wide"
    )

    DefaultTemplate()

if __name__ == "__main__":
    main()
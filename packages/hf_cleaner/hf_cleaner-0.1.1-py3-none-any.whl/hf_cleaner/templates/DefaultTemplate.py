import time
from pathlib import Path
import streamlit as st
from hf_cleaner.utils.file_utils import hf_cache_loc, get_file_info, delete_item
from .BaseTemplate import BaseTemplate


class DefaultTemplate(BaseTemplate):
    def __init__(self):
        self.file_loc: str = hf_cache_loc()
        self.create_session_states()
        self.template_name = "Default Template"
        self.layout()


    def create_session_states(self):
        if 'delete_confirm' not in st.session_state:
            st.session_state.delete_confirm = {}

        if 'delete_message' not in st.session_state:
            st.session_state.delete_message = None


    def layout(self):

        diplay_cols = (5, 2, 1, 2, 2)

        with st.sidebar:
            st.write("File Viewer Options")
            show_models = st.checkbox(label="Show Models", value=True, key="show_models_checkbox")
            show_datasets = st.checkbox(label="Show Datasets", key="show_datasets_checkbox")

        st.write(f"**HF File Directory:** {self.file_loc}")

        files = self._get_file_list(self.file_loc, show_models, show_datasets)

        columns = st.columns(diplay_cols)

        fields = ["Name", 'Type', 'Size', 'Last Modified', "Action"]

        for col, field_name in zip(columns, fields):
            col.write(field_name)

        for file in files:
            col1, col2, col3, col4, col5 = st.columns(diplay_cols)
            info = get_file_info(file)
            col1.write(file.name)
            col2.write(info["type"])
            col3.write(info["size"])
            col4.write(info["modified"])
            col5.empty()
            key = f"delete_{file.name}"
            if key not in st.session_state.delete_confirm:
                st.session_state.delete_confirm[key] = False
            if not st.session_state.delete_confirm[key]:
                if col5.button("🗑️", key=f"del_{file.name}"):
                    st.session_state.delete_confirm[key] = True
            else:
                with col5:
                    col_confirm, col_cancel = st.columns(2)
                    with col_confirm:
                        if st.button("✓", key=f"confirm_{file.name}"):
                            if delete_item(file):
                                st.session_state.delete_message = f"Deleted {file.name}"
                                time.sleep(0.1)
                                st.rerun()
                            st.session_state.delete_confirm[key] = False
                    with col_cancel:
                        if st.button("✗", key=f"cancel_{file.name}"):
                            st.session_state.delete_confirm[key] = False
                            st.rerun()

            st.html("""<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """)

        if st.session_state.delete_message:
            st.success(st.session_state.delete_message)
            st.session_state.delete_message = None

    @staticmethod
    def _get_file_list(dir_path, is_list_models, is_list_datasets):
        items = list(Path(dir_path).glob('*'))
        model_list = []
        if is_list_models:
            model_list = [ path for path in items if "models--" in path.name]
        if is_list_datasets:
            datasets_list = [ path for path in items if "datasets--" in path.name]
            return model_list + datasets_list
        return model_list

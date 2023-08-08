import pandas as pd
import streamlit as st

import util

data_dir = 'data'
all_courses = util.load_json_in(data_dir, 'all_courses.json')

title = f'{util.get_title()}: All Courses'

st.set_page_config(page_title=title, page_icon=':computer:')

st.markdown(f'# :computer: {title}')
st.dataframe(pd.Series(all_courses, name='Course'), use_container_width=True, hide_index=True)

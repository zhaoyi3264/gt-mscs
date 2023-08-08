import pandas as pd
import streamlit as st

import util

map_dict_value = util.map_dict_value

data_dir = 'data'
track_overlap_courses = util.load_json_in(data_dir, 'track_overlap_courses.json')

title = f'{util.get_title()}: Overlapping Courses'

st.set_page_config(page_title=title, page_icon=':computer:')

st.markdown(f'# :computer: {title}')

track = st.selectbox(':bulb: Track', sorted(track_overlap_courses.keys()))

show_courses = st.checkbox('Show Courses')
map_func = (lambda v: [v]) if show_courses else len
df = pd.DataFrame(map_dict_value(track_overlap_courses[track], map_func), index=[track]).T
st.dataframe(df, use_container_width=True)

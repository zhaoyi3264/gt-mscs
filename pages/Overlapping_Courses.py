import pandas as pd
import streamlit as st

import data
import util

track_overlap_courses = data.track_overlap_courses

util.set_title('Overlapping Courses')

track = st.selectbox(':bulb: Track', sorted(track_overlap_courses.keys()))

st.markdown(':gear: Options')
show_courses = st.checkbox('Show Courses')
map_func = (lambda v: [v]) if show_courses else len

st.divider()

df = pd.DataFrame(util.map_dict_value(track_overlap_courses[track], map_func), index=[track]).T
st.dataframe(df, use_container_width=True)

import json

import streamlit as st

with open('data.json', 'r') as f:
    tracks = json.load(f)

st.markdown('# Georgia Tech MSCS Tracks')

track = st.selectbox('Track', tracks.keys())

tabs = st.tabs(tracks[track])
for tab, (course_type, course_subset) in zip(tabs, tracks[track].items()):
    with tab:
        # st.markdown(f'## {course_type}')
        for subset in course_subset:
            st.markdown(f'_Pick {subset["Pick"]} from:_')
            for i, course in enumerate(subset['Courses']):
                st.checkbox(course, key=f'{course}_{i}')

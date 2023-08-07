import json

import streamlit as st

with open('data.json', 'r') as f:
    tracks = json.load(f)

st.markdown('# Georgia Tech MSCS Tracks')

track = st.selectbox('Track', tracks.keys())

tabs = st.tabs(tracks[track])
for tab, (course_type, course_subset) in zip(tabs, tracks[track].items()):
    with tab:
        for subset in course_subset:
            selected = 0
            st.markdown(f'_Pick {subset["Pick"]} from:_')
            for i, course in enumerate(subset['Courses']):
                selected += st.checkbox(course, key=f'{course}_{i}')
            if selected > subset['Pick']:
                st.error('You could do that but it is not necessary.')

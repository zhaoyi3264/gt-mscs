import streamlit as st

from util import load_json

tracks = load_json('data.json')
track_type_course_count = load_json('track_type_course_count.json')

st.markdown('# Georgia Tech MSCS Tracks')

track = st.selectbox('Track', tracks.keys())

st.metric('Available Courses', track_type_course_count[track]['Total'])

tabs = st.tabs(tracks[track])
for tab, (course_type, course_subset) in zip(tabs, tracks[track].items()):
    with tab:
        # st.metric('Available Courses', track_type_course_count[track][course_type])
        for subset in course_subset:
            selected = 0
            st.markdown(f'_Pick {subset["Pick"]} from:_')
            for i, course in enumerate(subset['Courses']):
                selected += st.checkbox(course, key=f'{course_type}_{course}_{i}')
            if selected > subset['Pick']:
                st.error('You could do that but it is not necessary.')

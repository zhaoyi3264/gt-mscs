# References:
# - https://docs.streamlit.io/

import streamlit as st

from data import (
    tracks,
    track_type_course_count,
    track_to_courses,
    get_omscs_course_link,
    get_free_course_link,
    link_count,
)
from util import set_title

set_title('Tracks')
keys = list(sorted(tracks.keys()))
index = keys.index('Human-Computer Interaction')
track = st.selectbox(':bulb: Track', keys, index=index)

free_courses_count = link_count(track_to_courses[track])

left_col, right_col = st.columns(2)
with left_col:
    st.metric(':books: Available Courses', track_type_course_count[track]['Total'])
with right_col:
    st.metric(':free: Available Free Courses', free_courses_count)

tabs = st.tabs([f'{e} {t}' for e, t in zip([':lock:', ':thought_balloon:'], tracks[track])])
for tab, (course_type, course_subset) in zip(tabs, tracks[track].items()):
    with tab:
        for subset in course_subset:
            selected = 0
            st.markdown(f'_Pick {subset["Pick"]} from:_')
            for i, course in enumerate(subset['Courses']):
                left_col, right_col = st.columns([8, 2], gap='small')
                with left_col:
                    selected += st.checkbox(get_omscs_course_link(course), key=f'{course_type}_{course}_{i}')
                with right_col:
                    st.markdown(get_free_course_link(course), unsafe_allow_html=True)
            if selected > subset['Pick']:
                st.error(':worried: You could do that but it is not necessary.')

st.divider()

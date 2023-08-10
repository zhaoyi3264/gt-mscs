import streamlit as st

import data
import util

tracks = data.tracks
track_overlap_courses = data.track_overlap_courses
course_to_links = data.course_to_links

util.set_title('Compare Tracks')

left_col, right_col = st.columns(2)

keys = list(sorted(tracks.keys()))
index = keys.index('Human-Computer Interaction')
with left_col:
    track = st.selectbox(':bulb: Track', keys, index=index)

other_tracks = set(tracks.keys()) - set([track])
with right_col:
    other_track = st.selectbox(':bulb: Another Track', sorted(other_tracks))
overlap_courses = track_overlap_courses[track][other_track]

st.divider()

overlap_course_count = len(overlap_courses)
overlap_free_course_count = data.link_count(overlap_courses)
left_col, right_col = st.columns(2)
with left_col:
    util.emo_metric('Overlapping Courses', overlap_course_count)
with right_col:
    util.emo_metric('Overlapping Free Courses', overlap_free_course_count)

st.markdown(':memo: Course List')
for overlap_course in overlap_courses:
    left_col, right_col = st.columns([8, 2], gap='small')
    with left_col:
        st.markdown(f'- {data.get_omscs_course_link(overlap_course)}')
    with right_col:
        st.markdown(data.get_free_course_link(overlap_course), unsafe_allow_html=True)

st.divider()

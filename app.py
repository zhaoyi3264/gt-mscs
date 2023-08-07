import os

import streamlit as st

from util import load_json

data_dir = 'data'

def load_json_in(data_dir, file_name):
    return load_json(os.path.join(data_dir, file_name))

tracks = load_json_in(data_dir, 'tracks.json')
track_type_course_count = load_json_in(data_dir, 'track_type_course_count.json')
track_overlap_courses = load_json_in(data_dir, 'track_overlap_courses.json')

st.markdown('# :computer: Georgia Tech MSCS Tracks ')

track = st.selectbox(':bulb: Track', tracks.keys())

st.metric(':books: Available Courses', track_type_course_count[track]['Total'])

tabs = st.tabs([f'{e} {t}' for e, t in zip([':lock:', ':thought_balloon:'], tracks[track])])
for tab, (course_type, course_subset) in zip(tabs, tracks[track].items()):
    with tab:
        # st.metric('Available Courses', track_type_course_count[track][course_type])
        for subset in course_subset:
            selected = 0
            st.markdown(f'_Pick {subset["Pick"]} from:_')
            for i, course in enumerate(subset['Courses']):
                selected += st.checkbox(course, key=f'{course_type}_{course}_{i}')
            if selected > subset['Pick']:
                st.error(':worried: You could do that but it is not necessary.')

st.divider()

other_tracks = set(tracks.keys()) - set([track])
other_track = st.selectbox(':bulb: Another Track', sorted(other_tracks))
overlap_courses = track_overlap_courses[track][other_track]

# for other_track, overlap_courses in track_overlap_courses[track].items():
#     if other_track != track:

overlap_course_count = len(overlap_courses)

if overlap_course_count <= 0:
    emo = ':cry:'
elif overlap_course_count <= 3:
    emo = ':grinning:'
elif overlap_course_count <= 5:
    emo = ':smile:'
else:
    emo = ':satisfied:'

st.metric(f'{emo} Overlapping Courses', overlap_course_count)
for overlap_course in overlap_courses:
    st.markdown(f'- {overlap_course}')

# TODO
# For each track
# - Display if online is available, total online available
# - Display has the most overlap with what other tracks.
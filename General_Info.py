# References:
# - https://docs.streamlit.io/

import streamlit as st

from util import set_title, load_json_in, flatten, map_dict_value

data_dir = 'data'
tracks = load_json_in(data_dir, 'tracks.json')
track_type_course_count = load_json_in(data_dir, 'track_type_course_count.json')
track_overlap_courses = load_json_in(data_dir, 'track_overlap_courses.json')
course_to_links = load_json_in(data_dir, 'course_to_links.json')

track_to_courses = map_dict_value(tracks, lambda v: set(flatten([e['Courses'] for e in flatten(v.values())])))

set_title()

track = st.selectbox(':bulb: Track', sorted(tracks.keys()))

free_courses_count = sum(bool(course_to_links.get(course, {}).get('Free Course Link')) for course in track_to_courses[track])

left_col, right_col = st.columns(2)
with left_col:
    st.metric(':books: Available Courses', track_type_course_count[track]['Total'])
with right_col:
    st.metric(':free: Available Free Courses', free_courses_count)

tabs = st.tabs([f'{e} {t}' for e, t in zip([':lock:', ':thought_balloon:'], tracks[track])])
for tab, (course_type, course_subset) in zip(tabs, tracks[track].items()):
    with tab:
        # st.metric('Available Courses', track_type_course_count[track][course_type])
        for subset in course_subset:
            selected = 0
            st.markdown(f'_Pick {subset["Pick"]} from:_')
            for i, course in enumerate(subset['Courses']):
                links = course_to_links.get(course, {})
                
                if omscs_course_link := links.get('OMSCS Course Link', ''):
                    label = f'[{course}]({omscs_course_link})'
                else:
                    label = course
                left_col, right_col = st.columns([8, 2], gap='small')
                with left_col:
                    selected += st.checkbox(label, key=f'{course_type}_{course}_{i}')
                with right_col:
                    text = ''
                    if free_course_link := links.get('Free Course Link', ''):
                        text += f'Free Course'
                    st.markdown(f'<div style="text-align: right;"><a href={free_course_link}>{text}</a></div>', unsafe_allow_html=True)
            if selected > subset['Pick']:
                st.error(':worried: You could do that but it is not necessary.')

st.divider()

other_tracks = set(tracks.keys()) - set([track])
other_track = st.selectbox(':bulb: Another Track', sorted(other_tracks))
overlap_courses = track_overlap_courses[track][other_track]

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

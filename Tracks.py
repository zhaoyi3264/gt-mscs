# References:
# - https://docs.streamlit.io/

from itertools import zip_longest

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
            selected = {'': 0}
            prev_subarea = None
            subareas = subset.get('Sub-area', [None])
            xor = subset.get('XOR', {})
            # Show how many courses to pick
            if subarea_condition := subset.get('Sub-area Condition', ''):
                subarea_condition = f' ({subarea_condition})'
            st.markdown(f'_Pick {subset["Pick"]} from{subarea_condition}:_')
            for i, (course, subarea) in enumerate(zip_longest(subset['Courses'], subareas)):
                # Sub-area
                if subarea != prev_subarea:
                    st.markdown(f'__{subarea}__')
                prev_subarea = subarea
                # Course and free course links
                left_col, right_col = st.columns([8, 2], gap='small')
                with left_col:
                    # Course link
                    help = ''
                    if xor_courses := xor.get(course, []):
                        help = '\n'.join(['Can\'t be taken with:'] + xor_courses)
                    s = st.checkbox(get_omscs_course_link(course), key=f'{course_type}_{course}_{i}', help=help)
                    if subarea:
                        selected[subarea] = selected.get(subarea, 0) + s
                    selected[''] += s
                with right_col:
                    # Free course link
                    st.markdown(get_free_course_link(course), unsafe_allow_html=True)
            # Validate selected courses
            if selected[''] > subset['Pick']:
                st.error(':worried: You could do that but it is not necessary.')
            if subset.get('Sub-area Condition'):
                for k, v in selected.items():
                    if k and v < 1:
                        st.error(':worried: Please select at least one from each sub-area.')
                        break

st.divider()

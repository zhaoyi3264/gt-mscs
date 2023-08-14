import pandas as pd
import streamlit as st

import data
import util

all_courses = data.all_courses
course_to_links = data.course_to_links

util.set_title('All Courses')

course_to_links = pd.DataFrame(course_to_links).T.reset_index(names=['Course'])

st.markdown(':mag: Search')

search = st.text_input('Search', label_visibility='collapsed')

index = course_to_links['Course'].str.contains(search, case=False)
course_to_links = course_to_links[index]

st.markdown(':bookmark_tabs: Filters')
left_col, right_col = st.columns(2)
with left_col:
    omscs_filter = st.checkbox('OMSCS Available')
with right_col:
    free_filter = st.checkbox('Free Available')

subset = []
if omscs_filter:
    subset.append('OMSCS Course Link')
if free_filter:
    subset.append('Free Course Link')
course_to_links = course_to_links.dropna(subset=subset)

st.divider()

st.dataframe(
    course_to_links[['Course', 'OMSCS Course Link', 'Free Course Link']],
    use_container_width=True,
    hide_index=True,
    column_config={
        'OMSCS Course Link': st.column_config.LinkColumn(),
        'Free Course Link': st.column_config.LinkColumn()
    }
)

st.markdown(f'Total: {len(course_to_links)}')
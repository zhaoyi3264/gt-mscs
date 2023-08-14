from util import load_json_in

data_dir = 'data'

tracks = load_json_in(data_dir, 'tracks.json')
track_to_courses = load_json_in(data_dir, 'track_to_courses.json')
track_type_course_count = load_json_in(data_dir, 'track_type_course_count.json')
track_overlap_courses = load_json_in(data_dir, 'track_overlap_courses.json')
course_to_links = load_json_in(data_dir, 'course_to_links.json')
all_courses = load_json_in(data_dir, 'all_courses.json')

def get_link(course, link_type):
    return course_to_links.get(course, {}).get(link_type)

def get_omscs_course_link(course):
    if omscs_course_link := get_link(course, 'OMSCS Course Link'):
        return f'[{course}]({omscs_course_link})'
    else:
        return course

def get_free_course_link(course):
    if free_course_link := get_link(course, 'Free Course Link'):
        return f'<div style="text-align: right;"><a href={free_course_link}>Free Course</a></div>'
    else:
        return ''

def link_count(courses, link_type='Free Course Link'):
    return sum(bool(get_link(course, link_type)) for course in courses)

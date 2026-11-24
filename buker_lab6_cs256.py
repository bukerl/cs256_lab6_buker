# do I need to punch in the course strings/transcripts 
# and gen_ed_categories up here or in main??

def parse_course_record(course_string):
    """
    when given the course string:
    strip the whitespace, uppercase letters,
    split apart the string at commas, creating a list of strings
    make sure credits is stored as int.
    add each element of the list to a dict with keys 'code' 'name' 'credits' and 'status'
    """
    course = {}
    course_string.strip().upper().split(",")
    course["code"] = course_string(0)
    course["name"] = course_string(1)
    course["credits"] = int(course_string(2))
    course["status"] = course_string(3)

    return course
    
# find and seperate area code from phone number


message = "641-2314-225"


def extract_nums(text):
    import re
    ph_num_regex = re.compile(r'(\d\d\d)-(\d\d\d\d-\d\d\d)')
    match_object = ph_num_regex.search(text)
    print(match_object.group(1))
    print(match_object.group(2))
    return None



print(extract_nums(message))


# if the pattern itself includes paranthesis then:

message2 = "(641)-2314-225"
def extract_nums_with_brackets(text):
    import re
    ph_num_regex = re.compile(r"(\(\d\d\d\))-(\d\d\d\d-\d\d\d)")
    match_object = ph_num_regex.search(text)
    print(match_object.group(1))
    print(match_object.group(2))
    return None

print(extract_nums_with_brackets(message2))


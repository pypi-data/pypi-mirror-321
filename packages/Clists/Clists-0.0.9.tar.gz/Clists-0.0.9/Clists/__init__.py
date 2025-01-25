import os

def check_schema(obj):
    """Checks if the object element is not a schema type
    """
    schema_elements = []
    for element in obj:
        for char in element.strip('",\n ').lower():
            if not (ord(char) >= 97 and ord(char) <= 122):
                break
        else:
            schema_elements.append(element.strip('",\n ').lower())
    return schema_elements

def convert_lists(a, b):
    """Converts lists into a single schema (combining elementwise)
    """
    converted_list = a + b
    schema_sorted_set = sorted(list(set(converted_list)))
    return schema_sorted_set

def Cache_Lists(to_cache, file_path = 'default_schema.txt'):
    """Caches list for performance boost
    """
    path_init = os.path.realpath(__file__)
    path_dir = os.path.dirname(path_init)
    
    schema = []
    with open(f'{path_dir}/{file_path}', 'r') as file:
        schema = file.readlines()

    # schema = [x.strip() for x in schema]
    schema_cached = convert_lists(schema, to_cache)
    schema_checked_cached = check_schema(schema_cached)
    return schema_checked_cached
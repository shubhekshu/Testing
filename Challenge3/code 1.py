def get_value(nested_dict, key):
    keys = key.split('/')
    value = nested_dict
    for k in keys:
        value = value[k]
    return value



object1 = {"a": {"b": {"c": "d"}}}
key1 = "a/b/c"
value1 = get_value(object1, key1)
print(value1)  # Output: d

object2 = {"x": {"y": {"z": "a"}}}
key2 = "x/y/z"
value2 = get_value(object2, key2)
print(value2)  # Output: a

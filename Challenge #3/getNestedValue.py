def keyFunct(obj: dict):
    keys = list(obj)
    if len(keys) != 1:
        raise Exception('Either multiple keys are there or empty dict found')
    else:
        return keys[0]


def nestedValue(obj: dict, key: str):
    if type(obj) is not dict:
        return None
    if (key in obj.keys()) :
        if type(obj[key]) is dict:
            return nestedValue(obj[key], keyFunct(obj[key]))
        else:
            return obj[keyFunct(obj)]
    else:
        nestedKey = keyFunct(obj)
        return nestedValue(obj[nestedKey], key)

if __name__ == '__main__':
    obj = {"a": {"b": {"c": "d"}}}
    listValue = list(obj.keys())
    value = nestedValue(obj, listValue[0])
    print(value)

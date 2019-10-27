
import re

def phrase_search(object_list: list, search_string: str) -> int:
    for obj in object_list:
        if re.search(r'[{].*[}]',obj["phrase"]):
            if search_string in obj["phrase"].translate({ord(i): None for i in '{}'}):
                return obj["id"]
            for slot in obj["slots"]:
                if search_string in re.sub('[{].*[}]',slot,obj["phrase"]):
                    return obj["id"]
        elif search_string in obj["phrase"]:
            return obj["id"]
    return 0


if __name__ == "__main__":
    """ 
    len(object) != 0
    object["id"] > 0
    0 <= len(object["phrase"]) <= 120
    0 <= len(object["slots"]) <= 50
    """
    object = [
        {"id": 1, "phrase": "Hello world!", "slots": []},
        {"id": 2, "phrase": "I wanna {pizza}", "slots": ["pizza", "BBQ", "pasta"]},
        {"id": 3, "phrase": "Give me your power", "slots": ["money", "gun"]},
    ]

   
    

    
    assert phrase_search(object, 'I wanna pasta') == 2
    assert phrase_search(object, 'Give me your power') == 3
    assert phrase_search(object, 'Hello world!') == 1
    assert phrase_search(object, 'I wanna nothing') == 0
    assert phrase_search(object, 'Hello again world!') == 0
    assert phrase_search(object, 'I need your clothes, your boots & your motorcycle') == 0
    
    
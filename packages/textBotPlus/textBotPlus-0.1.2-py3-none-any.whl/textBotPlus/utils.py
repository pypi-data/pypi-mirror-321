# textBot/utils.py
from typing import Union, Any
from bs4 import BeautifulSoup

def process_json_list_to_dict(json_obj: list = None) -> Union[list, dict]:
    if isinstance(json_obj, list):
        for json_obj_value in json_obj:
            if isinstance(json_obj_value, dict):
                return json_obj_value
    else:
        return json_obj  

def get_json_text(json_obj: Union[list,dict] = None, keys: list = None) -> Any:
    if json_obj is not None and keys is not None:
        for key in keys:
            try:
                if isinstance(json_obj, dict):
                    json_obj = json_obj[key]
                elif isinstance(json_obj, list):
                    json_obj = process_json_list_to_dict(json_obj=json_obj)
                    if isinstance(json_obj, dict):
                        json_obj = json_obj[key]
            except Exception as error:
                print(error)
                
        return standardized_string(json_obj) if isinstance(json_obj, (int, float, str)) else json_obj if json_obj else ""
    else:
        return ""

def get_selector_text(soup_obj: BeautifulSoup = None, css_selectors: str = None, css_selector: str = None, css_selector_text: str = None, attr: str = None) -> Any:
    try:
        if soup_obj is not None:
            if css_selector_text is not None and attr is not None and css_selectors is None and css_selector is None:
                return standardized_string(f'''{soup_obj.select_one(css_selector_text).get(attr, "")}''')
            
            elif attr is not None and css_selectors is None and css_selector is None and css_selector_text is None:
                return standardized_string(f'''{soup_obj.get(attr, "")}''')
            
            elif css_selector_text is not None and css_selectors is None and css_selector is None and attr is None:
                return standardized_string(f'''{soup_obj.select_one(css_selector_text).text}''')

            elif css_selectors is None and css_selector is None and css_selector_text is None and attr is None:
                return standardized_string(f'''{soup_obj.text}''')
                
            elif css_selectors is not None and css_selector is None and css_selector_text is None and attr is None:
                return soup_obj.select(css_selectors)
            
            elif css_selector is not None and css_selectors is None and css_selector_text is None and attr is None:
                return soup_obj.select_one(css_selector)               
            else:
                return None
        else:
            print("Soup obj is None")
            return None
    except Exception as error:
        print(error)
        return None  # Optionally, log the error if needed

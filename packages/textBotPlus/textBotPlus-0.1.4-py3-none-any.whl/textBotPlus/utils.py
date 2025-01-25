# textBot/utils.py
from typing import Union, Optional, List, Any
from bs4 import BeautifulSoup
import re
import pandas as pd
import csv
import os


def create_directory(directory_name: str) -> None:
    """
    Creates a directory if it doesn't already exist.
    
    Args:
    - directory_name (str): The name of the directory to create.

    Returns:
    - None
    """
    try:
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
    except OSError as error:
        print(f"Error: {error}")


def standardized_string(string: str = None) -> str:
    """
    Standardizes a string by:
    - Replacing `\n`, `\t`, and `\r` with spaces.
    - Removing HTML tags.
    - Replacing multiple spaces with a single space.
    - Stripping leading/trailing spaces.

    Args:
    - string (str, optional): The string to be standardized. Defaults to None.

    Returns:
    - str: The standardized string, or an empty string if input is None.
    """
    if string is not None:
        string = str(string)
        string = string.replace("\\n", " ").replace("\\t", " ").replace("\\r", " ")
        string = re.sub(r"<.*?>", " ", string)  # Remove HTML tags
        string = re.sub(r"\s+", " ", string)  # Collapse multiple spaces into one
        string = string.strip()  # Strip leading/trailing spaces
        return string
    else:
        print("None value is passed")
        return ""



def remove_common_elements(remove_in: Union[list, tuple, set] = None, remove_by: Union[list, tuple, set] = None) -> list:
    """
    Removes elements from `remove_in` that are present in `remove_by`.

    Args:
    - remove_in (Union[list, tuple, set], optional): The collection from which elements will be removed. Defaults to None.
    - remove_by (Union[list, tuple, set], optional): The collection containing elements to remove from `remove_in`. Defaults to None.

    Returns:
    - list: A list containing elements from `remove_in` that are not in `remove_by`.
    """
    if remove_in is not None and remove_by is not None:
        # Ensure both collections are sets for efficient difference operation
        set_a = remove_in
        set_b = remove_by

        if not isinstance(set_a, set):
            set_a = set(set_a)
        if not isinstance(set_b, set):
            set_b = set(set_b)

        set_a.difference_update(set_b)  # Remove elements from set_a that are in set_b
        return list(set_a)  # Return the result as a list

    else:
        missing_args = []
        if remove_in is None:
            missing_args.append('remove_in')
        if remove_by is None:
            missing_args.append('remove_by')

        print(f"Value not passed for: {', '.join(missing_args)}")
        return []


def save_to_csv(list_data: Optional[List[list]] = None, column_header_list: Optional[List[str]] = None, output_file_path: Optional[str] = None, sep: str = ",") -> None:
                
    """
    Saves data to a CSV file. If the file exists, it appends the data; otherwise, it creates a new file.
    
    Args:
    - list_data (Optional[List[list]], optional): The data to be saved in the CSV file. Defaults to None.
    - column_header_list (Optional[List[str]], optional): The column headers for the CSV file. Defaults to None.
    - output_file_path (Optional[str], optional): The path to the output CSV file. Defaults to None.
    - sep (str, optional): The delimiter used in the CSV file. Defaults to "," (comma).

    Returns:
    - None: This function doesn't return anything. It performs a side effect (writing to a file).
    """
    if list_data and column_header_list and output_file_path:
        try:
            # Check if the file exists
            if os.path.exists(output_file_path):
                # Append data to the file if it exists
                pd.DataFrame(list_data, columns=column_header_list).to_csv(output_file_path, index=False, header=False, sep=sep,encoding="utf-8",quoting=csv.QUOTE_ALL,quotechar='"',mode="a")
                                                                            
            else:
                # Create a new file and write data
                pd.DataFrame(list_data, columns=column_header_list).to_csv(output_file_path, index=False,header=True,sep=sep,encoding="utf-8",quoting=csv.QUOTE_ALL,quotechar='"',mode="w")
                                                                            
        except Exception as e:
            print(f"save_to_csv: {e.__class__} - {str(e)}")
    else:
        missing_args = []
        if list_data is None:
            missing_args.append('list_data')
        if column_header_list is None:
            missing_args.append('column_header_list')
        if output_file_path is None:
            missing_args.append('output_file_path')

        print(f"Data not saved due to missing arguments: {', '.join(missing_args)}")



def read_csv(csv_file_path: str, get_value_by_col_name: Optional[str] = None, filter_col_name: Optional[str] = None, inculde_filter_col_values: Optional[List[str]] = None, exclude_filter_col_values: Optional[List[str]] = None, sep: str = ",") -> Union[List[str], pd.DataFrame]:
             
    """
    Reads a CSV file and returns values from a specific column based on various filters.
    
    Args:
    - csv_file_path (str): Path to the CSV file.
    - get_value_by_col_name (Optional[str]): The column name from which to fetch values.
    - filter_col_name (Optional[str]): The column name to apply filters.
    - inculde_filter_col_values (Optional[List[str]]): List of values to include in the filter.
    - exclude_filter_col_values (Optional[List[str]]): List of values to exclude from the filter.
    - sep (str, optional): The delimiter used in the CSV file. Defaults to "," (comma).
    
    Returns:
    - Union[List[str], pd.DataFrame]: A list of values if filtering, or the full DataFrame if no filtering.
    """
    
    if not os.path.exists(csv_file_path):
        print("read_csv: csv_file_path does not exist.")
        return []
    
    urls = []
    
    try:
        # Try to read CSV with error handling and the specified separator
        df = pd.read_csv(csv_file_path, header=0, sep=sep, encoding='utf-8', on_bad_lines='skip', dtype=object).fillna("")
        
        if get_value_by_col_name and filter_col_name:
            # If we are filtering by include values
            if inculde_filter_col_values:
                for value in inculde_filter_col_values:
                    filtered_df = df[df[filter_col_name] == str(value)]
                    urls.extend(filtered_df[get_value_by_col_name].tolist())
            
            # If we are filtering by exclude values
            elif exclude_filter_col_values:
                for value in exclude_filter_col_values:
                    filtered_df = df[df[filter_col_name] != str(value)]
                    urls.extend(filtered_df[get_value_by_col_name].tolist())
        
        elif get_value_by_col_name and not filter_col_name:
            # If just getting values from a single column without filters
            urls.extend(df[get_value_by_col_name].tolist())
        
        elif not get_value_by_col_name and not filter_col_name:
            # If no filters or specific column is provided, return the entire DataFrame
            return df
        
        else:
            print("========= Arguments are not proper =========")
            return []
    
    except Exception as e:
        print(f"Error reading CSV: {str(e)}")
        return []

    # Return unique values (set removes duplicates) as a list
    return list(set(urls))



def process_json_list_to_dict(json_obj: list = None) -> Union[list, dict]:
    if isinstance(json_obj, list):
        for json_obj_value in json_obj:
            if isinstance(json_obj_value, dict):
                return json_obj_value
    else:
        return json_obj  

def get_json_text(json_obj: Union[list,dict] = None, keys: list = None) -> Any:
    """
    Extract values from a JSON object (dict or list) using a list of keys.

    Args:
    - json_obj (Union[dict, list]): The JSON object (either a dictionary or a list).
    - keys (List[str]): A list of keys to access nested values.

    Returns:
    - Any: The extracted value, or an empty string if not found. 
    """

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


def get_selector_text(soup_obj: Optional[BeautifulSoup] = None, css_selectors: Optional[str] = None, css_selector: Optional[str] = None, css_selector_text: Optional[str] = None, attr: Optional[str] = None) -> Any:
                      
    """
    Extracts text or attribute from a BeautifulSoup object using CSS selectors or attributes.

    Args:
    - soup_obj (Optional[BeautifulSoup]): The BeautifulSoup object containing the HTML content.
    - css_selectors (Optional[str]): The CSS selectors to select multiple elements.
    - css_selector (Optional[str]): The CSS selector to select a single element.
    - css_selector_text (Optional[str]): CSS selector to extract the text from a selected element.
    - attr (Optional[str]): The attribute name to extract from the selected element.
    
    Returns:
    - Any: The extracted text or attribute value. Returns None in case of errors or missing input.
    """
    if soup_obj is None:
        print("Soup obj is None")
        return None
    
    try:
        # If `css_selector_text` and `attr` are provided, get the attribute from the first matching element
        if css_selector_text and attr:
            return standardized_string(soup_obj.select_one(css_selector_text).get(attr, "") if soup_obj.select_one(css_selector_text) else "")
        
        # If `attr` is provided but no selector, return the attribute from the `soup_obj` directly
        elif attr:
            return standardized_string(soup_obj.get(attr, "") if soup_obj else "")
        
        # If `css_selector_text` is provided without `attr`, return the text of the first matching element
        elif css_selector_text:
            return standardized_string(soup_obj.select_one(css_selector_text).text if soup_obj.select_one(css_selector_text) else "")
        
        # If no selectors or attributes are provided, return the text content of the entire `soup_obj`
        elif not css_selectors and not css_selector and not css_selector_text and not attr:
            return standardized_string(soup_obj.text)
        
        # If `css_selectors` is provided, return a list of matching elements
        elif css_selectors:
            return soup_obj.select(css_selectors)
        
        # If `css_selector` is provided, return the first matching element
        elif css_selector:
            return soup_obj.select_one(css_selector)
        
        else:
            return None

    except Exception as error:
        print(f"Error: {error}")
        return None  # Optionally, log the error if needed


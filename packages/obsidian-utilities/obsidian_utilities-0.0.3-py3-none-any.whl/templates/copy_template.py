"""
    Copy template file(s) to target directories. Users may utilize Obsidian 
    plugins to automatically populate fields within the note body, so make 
    sure to open notes within the Obsidian application to perform any updates 
    to a note as necessary. This module provides the functionality to copy 
    template files from a template directory location to a target location, 
    with the ability to copy in multiples.

    Author: Jason Boyd
    Date: January 3, 2025
    Modified: January 9, 2025
"""

# TODO:
# - [ ] add checks to copy ensuring target directory can handle expected filenames.

import pathlib
import datetime
import shutil


def compute_spread(string_list):
    """Compute the spread (range of lengths of elements) in string_list.

    Args:
        string_list (iterable): the iterable to compare lengths against.

    Returns:
        int: the spread of the supplied string_list.
    """

    if len(string_list) == 0:
        return 0

    element_lengths = [len(s) for s in string_list]
    return max(element_lengths) - min(element_lengths)


def find_common_position_characters(string_list):
    """Find all common characters that share the same position in string_list.

    Args:
        string_list (iterable): the iterable to find the common characters from.

    Returns:
        list: the unique list of sorted characters that all share the same position.
    """

    commonality = set()
    for comparer, *elements in zip(*string_list):
        if all(comparer == matcher for matcher in elements):
            commonality.add(comparer)
    return sorted(list(commonality))


def iso_proper_length_parts(iso_part_list):
    """Given an ISO-spearated parts list, determine if the lengths of its parts are 
        ISO-formatted worthy.

    Args:
        iso_part_list (list): the parts of an ISO string that the function checks 
            lengths against to determine ISO-formatted worthiness.

    Returns:
        bool: wether the parts list matches the ISO-formatted lengths required.
    """

    if len(iso_part_list) != 3:
        return False
    if len(iso_part_list[0]) != 4:
        return False
    if len(iso_part_list[1]) == 3:
        if len(iso_part_list[2]) != 1:
            return False
    if len(iso_part_list[1]) == 2:
        if len(iso_part_list[2]) != 2:
            return False
    return True


def process_template_location(template_object):
    """Given a template object (should be str), perform checks to ensure the supplied 
        path exists and is an actual file and not a directory to be copied from.

    Args:
        template_object (str or path-like object): the template path to analyze 
            and create a pathlib.Path from.

    Raises:
        FileNotFoundError: file location does not exist or is not a real file.
        IsADirectoryError: file location is actually a directory and not a file.

    Returns:
        pathlib.Path: the Path() created from processing the template object.
    """
    
    # grab the resolved path from the template_object location for processing
    path_instance = pathlib.Path(template_object).resolve()

    if path_instance.name == template_object: # caller just supplied a name of file
        # TODO: check to see if program has template path saved
        template_saved = False
        if not template_saved:
            raise FileNotFoundError(f"Template location not found: {template_object}")
        
    if not path_instance.exists():
        raise FileNotFoundError(f"Template object does not exist: {template_object}")
    if path_instance.is_dir():
        raise IsADirectoryError(f"Template object is a directory: {template_object}")
    if not path_instance.is_file():
        raise FileNotFoundError(f"Template object is not a valid file: {template_object}")
    
    # determined that template_object is a good file for copying from
    return path_instance


def process_directory_location(target_directory):
    """Given a target directory (should be str), perform checks to ensure the 
        supplied directory exists and can be used to copy to.

    Args:
        target_directory (str or path-like object): the target path to analayze 
            and create a pathlib.Path from.

    Raises:
        FileNotFoundError: directory location does not exist or is not a directory.
        NotADirectoryError: directory location is actually a file and not a directory.

    Returns:
        pathlib.Path: the Path() created from processing the target directory.
    """

    path_instance = pathlib.Path(target_directory).resolve()

    if path_instance.name == target_directory: # caller supplied a name of directory
        raise FileNotFoundError(f"Target directory should be directory path: {target_directory}")
    
    if not path_instance.exists():
        raise FileNotFoundError(f"Target directory does not exist: {target_directory}")
    if path_instance.is_file():
        raise NotADirectoryError(f"Target directory is a file: {target_directory}")
    if not path_instance.is_dir():
        raise FileNotFoundError(f"Target directory is not a valid directory: {target_directory}")
    
    # determined that target_directory is a good directory for copying to
    return path_instance


def iso_formatted_string(iso_string, common_characters):
    """Given a string, check if its ISO-formatted based on a list of common characters.

    Args:
        iso_string (str): the string to determine if its ISO-formatted.
        common_characters (iterable): the common characters to check formatting against.

    Returns:
        tuple: two elements, the first bool telling if iso_string is ISO-formatted, and 
            the second string denoting the character that separates the ISO elements.
    """

    
    use_iso_string = str(iso_string)
    iso_separated_char = None
    if len(use_iso_string) not in [8, 10]:
        return (False, None)
    
    if len(iso_string) == 10:
        for common_char in common_characters:
            split_iso = iso_string.split(common_char)
            if iso_proper_length_parts(split_iso):
                use_iso_string = iso_string.replace(common_char, "-")
                iso_separated_char = common_char
                break
    try:
        new_date = datetime.date.fromisoformat(use_iso_string)
        return (True, iso_separated_char)
    except:
        return (False, iso_separated_char)
    

def iso_formatted_list(string_list, common_characters):
    """Determine if a string list has all ISO-formatted elements based on a list of 
        common characters.


    Args:
        string_list (_type_): the string list to determine if elements are ISO-formatted.
        common_characters (iterable): the common characters to check formatting against.

    Returns:
        tuple: two elements, the first bool telling if all list elements are ISO-formatted, 
            and the second string denoting the character that separates the ISO elements.
    """

    iso_formatted_results = [iso_formatted_string(ifi, common_characters) for ifi in string_list]
    results = list(zip(*iso_formatted_results))
    if all(results[0]) and len(set(results[1])) <= 1:
        return (True, results[1][-1])
    return (False, None)
    

def copy_template_handler(template_path, target_file):
    """Handler function that actually does the copying of template_path using shutil.

    Args:
        template_path (pathlib.Path): the template path-like object to copy from.
        target_file (pathlib.Path): the target path-like object to copy to.

    Raises:
        FileExistsError: if the target_file already exists in the filesystem
        IsADirectoryError: if the target_file is a directory

    Returns:
        bool: wether the copy of template_path to target_file succeeded or not.
    """
    
    if target_file.is_file():
        raise FileExistsError(f"Target file already exists: {target_file}")
    elif target_file.is_dir():
        raise IsADirectoryError(f"Target file is a directory: {target_file}")
    
    try: # attempt to perform the actual copy of the template into target
        shutil.copy(template_path, target_file)
        return True
    except:
        return False


def copy_template_single(template_path, target_path, use_formatting=True):
    """Copy a single template file to the target path, optionally using existing formatting.

    Args:
        template_path (pathlib.Path): the template file path to copy from
        target_path (pathlib.Path): the target directory path to copy into
        use_formatting (bool, optional): optionally use potentially existing formatting 
        in the target directory. If ISO formatting is found, the copied file will 
        utilize today's date as its file name. Defaults to True.

    Returns:
        bool: wether the copy succeeded or not based on further function calls.
    """

    analyze_results = analyze_directory(target_path)
    # if caller doesn't want to use formatting or couldn't find formatting
    if not use_formatting or not analyze_results["detected_formatting"]:
        target_name = template_path.stem + "-copy" + template_path.suffix
        target_file = target_path.joinpath(target_name)
        return [copy_template_handler(template_path, target_file)]

    single_file = None
    match analyze_results["formatting_type"]:
        case "ISO":
            todays_date_iso = datetime.date.today().isoformat()
            todays_file_name = template_path.stem + "-copy" + template_path.suffix
            found_separator = analyze_results["formatting_separator"]
            todays_file_name = todays_date_iso.replace("-", found_separator if found_separator else "")
            todays_file_full = todays_file_name + template_path.suffix
            single_file = target_path.joinpath(todays_file_full)
        case _:
            pass
    return [copy_template_handler(template_path, single_file)]
        

def copy_template_multiple(template_path, target_path, number_copies=1):
    """Copy template file to the target path number_copies times.

    Args:
        template_path (pathlib.Path): the template file path to copy from
        target_path (pathlib.Path): the target directory path to copy into
        number_copies (int): the number of copies to make of template_path 
            into target_path.

    Returns:
        list: wether the copies succeeded or not based on further function calls.
    """

    results = []
    for index in range(0, number_copies):
        target_name = template_path.stem + f"-copy-{index}" + template_path.suffix
        target_file = target_path.joinpath(target_name)
        results.append(copy_template_handler(template_path, target_file))
    return results


def copy_template(template_object, target_directory, use_formatting=True, number_copies=1):
    """The top-level copy function that should be used by the caller.

    Args:
        template_object (str): the template file path that will be used to copy from
        target_directory (str): the target directory the copy will be copied into
        use_formatting (bool, optional): optionally follow formatting present in 
            target_directory, and defaults to True.
        number_copies (int, optional): the number of copies to make of the template_object 
            into target_directory, and defaults to 1.

    Raises:
        ValueError: if the number of copies is some un-copiable (less than zero) number.

    Returns:
        bool: wether the copy succeeded or not based on further function calls.
    """

    if number_copies < 0: # cannot copy less than zero times
        raise ValueError(f"Cannot copy notes {number_copies} of times")

    template_path = process_template_location(template_object)
    target_path = process_directory_location(target_directory)

    if number_copies == 1:
        return copy_template_single(template_path, target_path, use_formatting=use_formatting)
    return copy_template_multiple(template_path, target_path, number_copies=number_copies)


def analyze_directory(directory):
    """Given a directory, analyze the files within and determine if they match some 
        sort of formatting pattern.

    Args:
        directory (str): the directory to analyze against.

    Returns:
        dict: the information object that contains elements that include if formatting 
            was detected, the formatting type that was detected, and the separator 
            between formatted elements.
    """

    return_object = {
        "detected_formatting": False,
        "formatting_type": None,
        "formatting_separator": None,
    }
    
    path_directory = process_directory_location(directory)
    files = path_directory.iterdir()
    stem_names = [f.stem for f in files]

    # no file names were found in the directory, don't process for patterns
    if not stem_names:
        return return_object

    # file names have different lengths, don't process for patterns
    if compute_spread(stem_names) > 0:
        return return_object
    
    common_characters = find_common_position_characters(stem_names)

    # could be an ISO formatted date naming convention in directory
    iso_formatted_files, split_common_char = iso_formatted_list(stem_names, common_characters)
    if iso_formatted_files:
        return_object = {
            "detected_formatting": True,
            "formatting_type": "ISO",
            "formatting_separator": split_common_char,
        }

    return return_object
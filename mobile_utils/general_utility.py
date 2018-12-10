import array
import os
import random
import time
import json
import names
import fauxfactory

script_path = 'SCRIPT_PATH'


def firstname():
    return names.get_first_name(gender=None)


def lastname():
    return names.get_last_name()


def fullname():
    return names.get_full_name(gender=None)


def id_generator(size=8, utf8=True):
    """
    Generates a random character string (Letters + Digits)
    Default length of string generated is 8
    Only considers ascii letters and digits
    """
    if utf8:
        alphasize = random.randint(1, size - 1)
        utfsize = size - alphasize
        result = fauxfactory.gen_alphanumeric(alphasize) + fauxfactory.gen_utf8(utfsize)
    else:
        result = fauxfactory.gen_alphanumeric(size)
    return result


def email_generator(name=None, domain="moj", tlds="io"):
    """
    Generates random email address of random length
    """
    if not name:
        name = id_generator(utf8=False)
    result = fauxfactory.gen_email(name=name, domain=domain, tlds=tlds)
    return result.lower()


def num_string_generator(size=10):
    return fauxfactory.gen_numeric_string(size)


def num_generator(limit=1048576):
    """
    Generates a random number between 0 and limit
    Default limit is 1048578 (Mega number)
    """
    result = fauxfactory.gen_integer(min_value=2, max_value=limit)
    return result


def read_binary_file(filename):
    try:
        f = open(filename, 'rb')
        n = os.path.getsize(filename)
        data = array.array('B')
        data.read(f, n)
        f.close()
        fsize = data.__len__()
        return fsize, data

    except IOError:
        return -1, []


def create_folder(path, folder_name=None):
    """
    Create a folder with given name under given path
    """
    if folder_name is None:
        folder_name = time_stamp()

    os.makedirs(path + os.sep + folder_name)

    randfolder = path + os.sep + folder_name
    return randfolder


def delete_file(file_path):
    """
    Delete specified file
    """
    os.remove(file_path)


def search_string(search_string, file_path):
    """
    Search for SearchString in specified file
    Returns the line in which the string was found
    Returns nothing if no matching lines
    """
    result = []
    for line in open(file_path):
        if "" + search_string in line:
            result.append(line)
    return result


def time_stamp():
    """
        Create timestamp in the form of YYYYMMDDHHMM
        """
    time_object = time.time()
    time_tuple = time.localtime(time_object)
    time_str = ""
    count = 1

    for timeValue in time_tuple:
        time_str += str(timeValue)
        if count == 6:
            break
        count += 1
    return time_str


def current_timestamp_strf():
    import datetime
    now = datetime.datetime.now()
    return str(now.strftime("%Y-%m-%dT%H:%M:%SZ"))


def current_timestamp_ios():
    import datetime
    now = datetime.datetime.now()
    return str(now.isoformat())


def md5sum(file_name):
    from hashlib import md5
    hashobj = md5()
    with open(file_name, "rb") as f:
        for chunk in iter(lambda: f.read(128 * hashobj.block_size), b""):
            hashobj.update(chunk)
    return hashobj.hexdigest()


def save_contents_into_file(file_to_save, file_content=None, streaming_response=None):
    with open(file_to_save, 'wb') as f:
        if file_content is not None:
            for line in file_content:
                f.write(line.encode("utf-8"))
        elif streaming_response is not None:
            for chunk in streaming_response.iter_content(chunk_size=1024 * 1024 * 16):
                if chunk:
                    f.write(chunk.encode("utf-8"))
    return 1


def read_contents_from_file(file_name):
    with open(file_name) as in_file:
        return in_file.read()

# def unicode_to_str(data):
#     if isinstance(data, basestring):
#         return str(data)
#     elif isinstance(data, collections.Mapping):
#         return dict(map(unicode_to_str, data.iteritems()))
#     elif isinstance(data, collections.Iterable):
#         return type(data)(map(unicode_to_str, data))
#     else:
#         return data


def float_generator():
    fauxfactory.gen_numeric_string()


def mk_tmp_dir(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == os.errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def safe_open_w(path):
    ''' Open "path" for writing, creating any parent directories as needed.
    '''
    mk_tmp_dir(os.path.dirname(path))
    return open(path, 'w')


def save_data_to_json_file(json_data, json_file_name):
    # create a "tmp" directory if it doesn't exist
    script_dir = os.path.dirname(__file__)
    precondition_path = os.path.abspath(os.path.join(script_dir, '../tmp', json_file_name))

    with safe_open_w(precondition_path) as f:
        f.write(json.dumps(json_data, indent=4))
import array
import collections
import os
import random
import time
import json
import fauxfactory

from dateutil.parser import parse as parse_date
from datetime import datetime, timedelta

script_path = 'SCRIPT_PATH'


class GeneralUtility(object):
    """
    Python Module file containing necessary general functions that might be used across testing Sync
    General functions that are not related to Sync operations. Can be reused across other tools
    """

    @staticmethod
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

    @staticmethod
    def email_generator(name=None, domain="moj", tlds="io"):
        """
        Generates random email address of random length
        """
        if not name:
            name = GeneralUtility.id_generator(utf8=False)
        result = fauxfactory.gen_email(name=name, domain=domain, tlds=tlds)
        return result.lower()

    @staticmethod
    def num_string_generator(size=10):
        return fauxfactory.gen_numeric_string(size)

    @staticmethod
    def num_generator(min=2, limit=1048576):
        """
        Generates a random number between 0 and limit
        Default limit is 1048578 (Mega number)
        """
        result = fauxfactory.gen_integer(min_value=2, max_value=limit)
        return result

    @staticmethod
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

    def create_folder(self, path, folder_name=None):
        """
        Create a folder with given name under given path
        """
        if folder_name is None:
            folder_name = self.time_stamp()

        os.makedirs(path + os.sep + folder_name)

        randfolder = path + os.sep + folder_name
        return randfolder

    @staticmethod
    def delete_file(file_path):
        """
        Delete specified file
        """
        os.remove(file_path)

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def current_timestamp_strf():
        import datetime
        now = datetime.datetime.now()
        return str(now.strftime("%Y-%m-%dT%H:%M:%SZ"))

    @staticmethod
    def current_timestamp_ios():
        import datetime
        now = datetime.datetime.now()
        return str(now.isoformat())

    @staticmethod
    def current_timestamp_strf_without_symbols():
        import datetime
        now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ").replace("-", "").replace(".", "").replace(":", "")

        return now

    @staticmethod
    def md5sum(file_name):
        from hashlib import md5
        hashobj = md5()
        with open(file_name, "rb") as f:
            for chunk in iter(lambda: f.read(128 * hashobj.block_size), b""):
                hashobj.update(chunk)
        return hashobj.hexdigest()

    @staticmethod
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

    @staticmethod
    def read_contents_from_file(file_name):
        with open(file_name) as in_file:
            return in_file.read()

    def unicode_to_str(self, data):
        if isinstance(data, str):
            return str(data)
        elif isinstance(data, collections.Mapping):
            return dict(map(self.unicode_to_str, data.items()))
        elif isinstance(data, collections.Iterable):
            return type(data)(map(self.unicode_to_str, data))
        else:
            return data

    def float_generator(self):
        fauxfactory.gen_numeric_string()

    def mk_tmp_dir(self, path):
        try:
            os.makedirs(path)
        except OSError as exc:
            if exc.errno == os.errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise

    def safe_open_w(self, path):
        ''' Open "path" for writing, creating any parent directories as needed.
        '''
        self.mk_tmp_dir(os.path.dirname(path))
        return open(path, 'w')

    def save_data_to_json_file(self, json_data, json_file_name):
        # create a "tmp" directory if it doesn't exist
        script_dir = os.path.dirname(__file__)
        precondition_path = os.path.abspath(os.path.join(script_dir, '../tmp', json_file_name))

        with self.safe_open_w(precondition_path) as f:
            f.write(json.dumps(json_data, indent=4))

    @staticmethod
    def remove_metadata(json_data):
        try:
            if json_data['Metadata']:
                # print("Find metadata in %s"% json_data)
                del json_data['Metadata']
        except:
            # print("No Metadata in %s"% json_data)
            pass

        return json_data

    @staticmethod
    def check_time(time_str):
        if isinstance(time_str, str):
            time = parse_date(time_str).replace(tzinfo=None)
            today = datetime.utcnow()
            within = today + timedelta(minutes=30)
            if (time <= within):
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def check_time_in_json(json_data):
        time = parse_date(json_data).replace(tzinfo=None)
        today = datetime.utcnow()
        within = today + timedelta(minutes=30)
        if (time <= within):
            return True
        else:
            return False
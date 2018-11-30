import functools
import inspect
import gc


def test_case(id):
    def make_wrapper(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("Test case ID {}: {}()".format(id, func.__name__))
            return func(*args, **kwargs)

        func.__qa_motion_test_case_id__ = id
        return wrapper

    return make_wrapper


def find_current_test_case_id():
    all_objects = gc.get_objects()

    for frame in inspect.stack():
        for obj in all_objects:
            if inspect.isfunction(obj) and (obj.__code__ is frame[0].f_code):
                id = getattr(obj, "__qa_motion_test_case_id__", None)
                if id is not None:
                    return id
                break

    return None
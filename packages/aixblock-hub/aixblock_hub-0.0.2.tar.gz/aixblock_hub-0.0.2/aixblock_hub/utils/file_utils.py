# Copyright (c) AIxBlock, Inc. 

import inspect
import os
from pathlib import Path
from shutil import Error, copy2, copystat

from aixblock_hub.hub.constants import DEFAULT_HUB
# TODO: remove this api, unify to flattened args
def func_receive_dict_inputs(func):
    """to decide if a func could recieve dict inputs or not

    Args:
        func (class): the target function to be inspected

    Returns:
        bool: if func only has one arg ``input`` or ``inputs``, return True, else return False
    """
    full_args_spec = inspect.getfullargspec(func)
    varargs = full_args_spec.varargs
    varkw = full_args_spec.varkw
    if not (varargs is None and varkw is None):
        return False

    args = [] if not full_args_spec.args else full_args_spec.args
    args.pop(0) if (args and args[0] in ['self', 'cls']) else args

    if len(args) == 1 and args[0] in ['input', 'inputs']:
        return True

    return False


def get_default_aixblock_cache_dir():
    """
    default base dir: '~/.cache/aixblock'
    """
    default_cache_dir = Path.home().joinpath('.cache', DEFAULT_HUB)
    return default_cache_dir


def get_aixblock_cache_dir() -> str:
    """Get aixblock cache dir, default location or
       setting with AIXBLOCK_CACHE

    Returns:
        str: the aixblock cache root.
    """
    return os.getenv('AIXBLOCK_CACHE', get_default_aixblock_cache_dir())


def get_model_cache_root() -> str:
    """Get model cache root path.

    Returns:
        str: the aixblock model cache root.
    """
    return os.path.join(get_aixblock_cache_dir(), 'hub')


def get_dataset_cache_root() -> str:
    """Get dataset raw file cache root path.

    Returns:
        str: the aixblock dataset raw file cache root.
    """
    return os.path.join(get_aixblock_cache_dir(), 'datasets')


def get_dataset_cache_dir(dataset_id: str) -> str:
    """Get the dataset_id's path.
       dataset_cache_root/dataset_id.

    Args:
        dataset_id (str): The dataset id.

    Returns:
        str: The dataset_id's cache root path.
    """
    dataset_root = get_dataset_cache_root()
    return dataset_root if dataset_id is None else os.path.join(
        dataset_root, dataset_id + '/')


def get_model_cache_dir(model_id: str) -> str:
    """cache dir precedence:
        function parameter > environment > ~/.cache/aixblock/hub/model_id

    Args:
        model_id (str, optional): The model id.

    Returns:
        str: the model_id dir if model_id not None, otherwise cache root dir.
    """
    root_path = get_model_cache_root()
    return root_path if model_id is None else os.path.join(
        root_path, model_id + '/')


def read_file(path):

    with open(path, 'r') as f:
        text = f.read()
    return text


def copytree_py37(src,
                  dst,
                  symlinks=False,
                  ignore=None,
                  copy_function=copy2,
                  ignore_dangling_symlinks=False,
                  dirs_exist_ok=False):
    """copy from py37 shutil. add the parameter dirs_exist_ok."""
    names = os.listdir(src)
    if ignore is not None:
        ignored_names = ignore(src, names)
    else:
        ignored_names = set()

    os.makedirs(dst, exist_ok=dirs_exist_ok)
    errors = []
    for name in names:
        if name in ignored_names:
            continue
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if os.path.islink(srcname):
                linkto = os.readlink(srcname)
                if symlinks:
                    # We can't just leave it to `copy_function` because legacy
                    # code with a custom `copy_function` may rely on copytree
                    # doing the right thing.
                    os.symlink(linkto, dstname)
                    copystat(srcname, dstname, follow_symlinks=not symlinks)
                else:
                    # ignore dangling symlink if the flag is on
                    if not os.path.exists(linkto) and ignore_dangling_symlinks:
                        continue
                    # otherwise let the copy occurs. copy2 will raise an error
                    if os.path.isdir(srcname):
                        copytree_py37(
                            srcname,
                            dstname,
                            symlinks,
                            ignore,
                            copy_function,
                            dirs_exist_ok=dirs_exist_ok)
                    else:
                        copy_function(srcname, dstname)
            elif os.path.isdir(srcname):
                copytree_py37(
                    srcname,
                    dstname,
                    symlinks,
                    ignore,
                    copy_function,
                    dirs_exist_ok=dirs_exist_ok)
            else:
                # Will raise a SpecialFileError for unsupported file types
                copy_function(srcname, dstname)
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except Error as err:
            errors.extend(err.args[0])
        except OSError as why:
            errors.append((srcname, dstname, str(why)))
    try:
        copystat(src, dst)
    except OSError as why:
        # Copying file access times may fail on Windows
        if getattr(why, 'winerror', None) is None:
            errors.append((src, dst, str(why)))
    if errors:
        raise Error(errors)
    return dst

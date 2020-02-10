#!/usr/bin/env python3

flag_cache = list()


def load_flag():
    '''Read the ctf flag to cache.
    The flag seem as:
        1:flag{1234567890}
    '''

    global flag_cache
    try:
        with open('/etc/ctf_flag.txt', 'r') as fp:
            for flag in fp.readlines():
                flag_cache.append(flag.strip())
    except FileNotFoundError:
        return None


def clear_flag_cache():

    global flag_cache
    flag_cache.clear()


def check_flag(flag):
    '''Check the flag if right or not.

    Returns:
        True: correct.
        False: not correct.
    '''

    global flag_cache
    for c in flag_cache:
        if c == flag:
            return True

    return False

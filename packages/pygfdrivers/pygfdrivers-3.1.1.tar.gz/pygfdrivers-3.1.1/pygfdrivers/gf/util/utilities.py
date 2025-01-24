from typing import Union


def format_channel(channel: int) -> str:
    """
    Checks format of command input is of channel = xx, as required by digitizer
    i.e channel must be a number in range [1,10]
    """
    try:
        if (1 <= int(channel) <= 10) & (len(str(channel)) <= 2):
            return str(channel).zfill(2)
        else:
            raise ValueError("'channel' incorrect datatype, expected to be 'int' between [1, 10].")

    except Exception as e:
        raise e


def format_gain(gain: int) -> str:
    try:
        gain = int(gain)

        if 1 <= gain <= 16:
            return str(gain)
        else:
            raise ValueError("'gain' incorrect data type, expected to be 'int' between [1, 16].")

    except Exception as e:
        raise e


def format_trig_level(level: int) -> str:
    try:
        level = int(level)

        if 0 <= level <= 100:
            return str(level)
        else:
            raise ValueError("'level' incorrect data type, expected to be 'int' between [0, 100].")

    except Exception as e:
        raise e


def format_start(start: Union[int, str]):
    try:
        if (len(str(start)) <= 6) & (isinstance(start, (int, str))):
            return str(start).zfill(6)
        else:
            raise ValueError("'start' incorrect data format, expected 'zero-padded int-str of length 6' or an 'int'.")

    except Exception as e:
        raise e


def format_averages(avgs: Union[int, str]):
    try:
        if (len(str(avgs)) <= 3) & (isinstance(avgs, (int, str))):
            return str(avgs).zfill(3)
        else:
            raise ValueError("'avgs' incorrect data format, expected 'zero-padded int-str of length 3' or an 'int'.")

    except Exception as e:
        raise e


def format_num_points(points: int):
    try:
        points = int(32.0 * (int(points) // 32.0))
        if points >= 0:
            return str(points)
        else:
            raise TypeError("'points' incorrect data type, expected an 'int'.")

    except Exception as e:
        raise e


def format_coupling(coupling: str):
    """
    Checks format of command input is of state = ac or state = dc as required by digitizer
    """
    possible_states = {'ac', 'dc'}

    try:
        if coupling.lower() in possible_states:
            return coupling.lower()
        else:
            raise ValueError(f"Unrecognized 'coupling' arg, expected one of '{possible_states}'.")

    except Exception as e:
        raise e

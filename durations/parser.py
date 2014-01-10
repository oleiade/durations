from durations.scales import Scale
from durations.exceptions import ScaleFormatError
from durations.constants import *
from durations.exceptions import (
    ScaleFormatError,
    InvalidTokenError
)


def valid_token(token):
    """Asserts a provided string is a valid duration token representation

    :param  token: duration representation token
    :type   token: string
    """
    is_scale = False

    # Check if the token represents a scale
    # If it doesn't set a flag accordingly
    try:
        Scale(token)
        is_scale = True
    except ScaleFormatError:
        pass

    # If token either represents a numerical value, a
    # separator token, or a scale, it is considered valid
    if any([token.isdigit(), token in SEPARATOR_TOKENS, is_scale]):
        return True

    return False


def compute_char_token(c):
    if c.isdigit():
        return SCALE_TOKEN_DIGIT
    elif c.isalpha():
        return SCALE_TOKEN_ALPHA

    return None


def extract_tokens(representation, separators=SEPARATOR_CHARACTERS):
    """Extracts durations tokens from a duration representation.

    Parses the string representation incrementaly and raises
    on first error met.

    :param  representation: duration representation
    :type   representation: string
    """
    buff = ""
    elements = []
    last_index = 0
    last_token = None

    for index, c in enumerate(representation):
        # if separator character is found, push
        # the content of the buffer in the elements list
        if c in separators:
            if buff:
                # If the last found token is invalid,
                # raise and InvalidTokenError
                if not valid_token(buff):
                    raise InvalidTokenError(
                        "Duration representation {0} contains "
                        "an invalid token: {1}".format(representation, buff)
                    )

                # If buffer content is a separator word, for example
                # "and", just ignore it
                if not buff.strip() in SEPARATOR_TOKENS:
                    elements.append(buff)

            # Anyway, reset buffer and last token marker
            # to their zero value
            buff = ""
            last_token = None
        else:
            token = compute_char_token(c)
            if (token is not None and last_token is not None and token != last_token):
                elements.append(buff)
                buff = c
            else:
                buff += c

            last_token = token

    # push the content left in representation
    # in the elements list
    elements.append(buff)

    return list(zip(elements[::2], elements[1::2]))

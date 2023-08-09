import typing


class KeyParts(typing.NamedTuple):
    type_: str
    name: str
    file: typing.Optional[str]


def parse_key(key: str):
    pieces = key.split(":")

    if len(pieces) > 1:
        type_ = pieces[0]
        rest = pieces[1]
    else:
        type_ = "topic"
        rest = key

    rest_pieces = rest.split("/")
    name = rest_pieces[0]
    if len(rest_pieces) > 1:
        file = "/".join(rest_pieces[1:])
    else:
        file = None

    return KeyParts(type_=type_, name=name, file=file)

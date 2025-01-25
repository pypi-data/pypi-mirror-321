import os
import pickle
import zlib
from io import BufferedIOBase


def read_util(data: BufferedIOBase, util: int = 0x00) -> bytes:
    content = bytearray()
    while True:
        c = data.read(1)
        if c[0] == util:
            break
        content += c
    return content


def to_start(start: str | None | bytes) -> bytes:
    if not start:
        return b""
    if isinstance(start, bytes):
        return start
    return start.encode("latin-1")


def extract_rpa(r: BufferedIOBase, dir: str | None = None):
    magic = read_util(r, 0x20)
    if magic != b"RPA-3.0":
        print("Not a Ren'Py archive.")
        return
    index_offset = int(read_util(r, 0x20), 16)
    key = int(read_util(r, 0x0A).decode(), 16)

    # read index
    r.seek(index_offset)
    index = pickle.loads(zlib.decompress(r.read()))
    for k, v in index.items():
        index[k] = [
            (offset ^ key, dlen ^ key, b"" if len(left) == 0 else to_start(left[0]))
            for offset, dlen, *left in v
        ]

    if not dir:
        dir = os.path.splitext(r.name)[0]
    for filename, entries in index.items():
        data = bytearray()
        for offset, dlen, start in entries:
            r.seek(offset)
            block = r.read(dlen)
            if start:
                if block.startswith(start):
                    block = block[len(start) :]
                else:
                    print("Warning: %s does not start with %s" % (filename, start))
            data += block

        filename = os.path.join(dir, filename)
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "wb") as f:
            print("extracting: ", filename)
            f.write(data)

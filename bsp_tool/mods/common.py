class Base:
    __slots__ = []
    _format = ""
    _arrays = {}

    def __init__(self, _tuple):
        # _tuple comes from: struct.unpack(self._format, bytes)
        # usually from struct.iter_unpack(self._format, LUMP)
        i = 0
        for attr in self.__slots__:
            if attr in self._arrays:
                array_map = self._arrays[attr]
                if isinstance(array_map, dict):
                    length = 0  # total size of all parts of the dict
                    for part in array_map.values():
                        if isinstance(part, list):
                            length += len(part)
                        elif isinstance(part, int):
                            length += part
                    array = _tuple[i:i + length]
                    value = MappedArray(array, mapping=array_map)
                elif isinstance(array_map, list):
                    length = len(array_map)
                    array = _tuple[i:i + length]
                    value = MappedArray(array, mapping=array_map)
                else:  # integer denoting array length
                    length = array_map
                    value = _tuple[i:i + length]
            else:  # this attribute is of length 1
                value = _tuple[i]
                length = 1
            setattr(self, attr, value)
            i += length

    def __repr__(self):
        components = {s: getattr(self, s) for s in self.__slots__}
        return f"<{self.__class__.__name__} {components}>"

    def flat(self):
        """recreate the iterable this instance was initialised from"""
        _tuple = []
        for slot in self.__slots__:
            value = getattr(self, slot)
            if not isinstance(value, (list, tuple, MappedArray)):
                _tuple.append(value)
            else:
                for x in value:
                    _tuple.append(x)
        return _tuple


class MappedArray:
    """Uses self.__dict__ to map objects to names. A basic Namespace"""
    _mapping = [*"xyz"]

    def __init__(self, array, mapping=_mapping):
        if isinstance(mapping, dict):
            self._mapping = list(mapping.keys())
            i = 0
            for segment_key, segment_map in mapping.items():
                segment = array[i:i + len(segment_map)]
                segment_array = MappedArray(segment, mapping=segment_map)
                setattr(self, segment_key, segment_array)
                i += len(segment_map)
        else:  # list of strings
            for attr, value in zip(mapping, array):
                setattr(self, attr, value)
            self._mapping = mapping

    def __eq__(self, other):
        return all([(a == b) for a, b in zip(self, other)])

    def __getitem__(self, index):
        return getattr(self, self._mapping[index])

    def __iter__(self):
        return iter([getattr(self, a) for a in self._mapping])

    def __repr__(self):
        out = []
        for attr, value in zip(self._mapping, self):
            out.append(f"{attr}: {value}")
        return f"<MappedArray ({', '.join(out)})>"

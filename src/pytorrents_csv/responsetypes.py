from typing import Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Torrent:
    rowid: int
    infohash: str
    name: str
    size_bytes: int
    created_unix: int
    seeders: int
    leechers: int
    completed: int
    scraped_date: int

    def __init__(self, rowid: int, infohash: str, name: str, size_bytes: int, created_unix: int, seeders: int, leechers: int, completed: int, scraped_date: int) -> None:
        self.rowid = rowid
        self.infohash = infohash
        self.name = name
        self.size_bytes = size_bytes
        self.created_unix = created_unix
        self.seeders = seeders
        self.leechers = leechers
        self.completed = completed
        self.scraped_date = scraped_date

    @staticmethod
    def from_dict(obj: Any) -> 'Torrent':
        assert isinstance(obj, dict)
        rowid = from_int(obj.get("rowid"))
        infohash = from_str(obj.get("infohash"))
        name = from_str(obj.get("name"))
        size_bytes = from_int(obj.get("size_bytes"))
        created_unix = from_int(obj.get("created_unix"))
        seeders = from_int(obj.get("seeders"))
        leechers = from_int(obj.get("leechers"))
        completed = from_int(obj.get("completed"))
        scraped_date = from_int(obj.get("scraped_date"))
        return Torrent(rowid, infohash, name, size_bytes, created_unix, seeders, leechers, completed, scraped_date)

    def to_dict(self) -> dict:
        result: dict = {}
        result["rowid"] = from_int(self.rowid)
        result["infohash"] = from_str(self.infohash)
        result["name"] = from_str(self.name)
        result["size_bytes"] = from_int(self.size_bytes)
        result["created_unix"] = from_int(self.created_unix)
        result["seeders"] = from_int(self.seeders)
        result["leechers"] = from_int(self.leechers)
        result["completed"] = from_int(self.completed)
        result["scraped_date"] = from_int(self.scraped_date)
        return result


class Pytorrent:
    torrents: List[Torrent]
    next: int

    def __init__(self, torrents: List[Torrent], next: int) -> None:
        self.torrents = torrents
        self.next = next

    @staticmethod
    def from_dict(obj: Any) -> 'Pytorrent':
        assert isinstance(obj, dict)
        torrents = from_list(Torrent.from_dict, obj.get("torrents"))
        next = from_int(obj.get("next"))
        return Pytorrent(torrents, next)

    def to_dict(self) -> dict:
        result: dict = {}
        result["torrents"] = from_list(lambda x: to_class(Torrent, x), self.torrents)
        result["next"] = from_int(self.next)
        return result


def pytorrent_from_dict(s: Any) -> Pytorrent:
    return Pytorrent.from_dict(s)


def pytorrent_to_dict(x: Pytorrent) -> Any:
    return to_class(Pytorrent, x)

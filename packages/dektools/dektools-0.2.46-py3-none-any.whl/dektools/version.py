import re
import functools
import semver


def version_to_tuple(version):
    return semver.Version.parse(version, True).to_tuple()


def version_is_release(version):
    ver = semver.Version.parse(version, True)
    return not ver.prerelease and not ver.build


def version_cmp(x, y, cache=None):
    def sure(v):
        if isinstance(v, str):
            if cache:
                if v not in cache:
                    cache[v] = semver.Version.parse(v, True)
                return cache[v]
            else:
                return semver.Version.parse(v, True)
        return v

    return sure(x).compare(sure(y))


class VersionCmpKey:
    def __init__(self):
        cache = {}
        self.key = functools.cmp_to_key(lambda x, y: version_cmp(x, y, cache))

    def __call__(self, x, y):
        return self.key(x, y)

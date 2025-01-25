import re
import functools
import semver


def version_to_tuple(version):
    return semver.Version.parse(version, True).to_tuple()


def version_is_release(version):
    ver = semver.Version.parse(version, True)
    return not ver.prerelease and not ver.build


def version_sorted(versions, reverse=False):
    return sorted(versions, key=functools.cmp_to_key(version_cmp), reverse=reverse)


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

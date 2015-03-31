#
# markdown/__version__.py
#
# version_info should conform to PEP 386
# (major, minor, micro, alpha/beta/rc/final, #, optional local identifier)
# (1, 1, 2, 'alpha', 0) => "1.1.2.dev"
# (1, 2, 0, 'beta', 2) => "1.2b2"
# (2, 6, 1, 'final', 0) => "2.6.1"
# (2, 6, 1, 'final', 0, 'dd.1') => "2.6.1+dd.1"
version_info = (2, 6, 1, 'final', 0, 'dd.1')


def _get_version():
    " Returns a PEP 386-compliant version number from version_info. "
    assert len(version_info) in [5, 6]
    assert version_info[3] in ('alpha', 'beta', 'rc', 'final')

    parts = 2 if version_info[2] == 0 else 3
    main = '.'.join(map(str, version_info[:parts]))

    sub = ''
    if version_info[3] == 'alpha' and version_info[4] == 0:
        # TODO: maybe append some sort of git info here??
        sub = '.dev'
    elif version_info[3] != 'final':
        mapping = {'alpha': 'a', 'beta': 'b', 'rc': 'c'}
        sub = mapping[version_info[3]] + str(version_info[4])

    if len(version_info) == 6 and version_info[5]:
        sub += "+" + str(version_info[5])

    return str(main + sub)

version = _get_version()

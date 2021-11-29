"""
In a galaxy far, far away, on a planet different from ours, each computer username uses the following format:

1. It must begin with either an underscore '_', or a period '.'.
2. The first character must be immediately followed by one or more digits in the range 0 through 9.
3. After some number of digits, there must be [0 or more English letters (uppercase and/or lowercase)].
4. It may be terminated with an optional '_'. 
5. Note that if it's not terminated with an underscore, then there should be no characters after the sequence of [0 or more English letters].


Examples:
_0898989811abced_ => Valid
_abce => INVALID
_09090909abcD0 => INVALID


RE = (_|\.)[0-9]+([A-z]+|0|[0-9A-z]*_)$
"""

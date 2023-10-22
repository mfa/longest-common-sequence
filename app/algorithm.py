from copy import copy
from difflib import SequenceMatcher
from itertools import combinations


def get_matches(items):
    for a, b in combinations(items, 2):
        s = SequenceMatcher(a=a, b=b)
        yield s.get_matching_blocks()


def filter_substrings(matches):
    # find substrings and don't return them
    matches = list(matches)
    for match in matches:
        _matches = copy(matches)
        _matches.remove(match)
        # return everything with spaces -- otherwise this is too aggressive
        if " " in match:
            yield match
        elif all(map(lambda x: match not in x, _matches)):
            yield match


def gen_match_strings(examples, matches, cutoff=3):
    for s, ms in zip(examples, matches):
        for m in ms:
            if m.size >= cutoff:
                yield s[m.a : m.a + m.size]


def check_match_strings(examples, mstrings, op):
    for mstr in set(mstrings):
        if op(map(lambda x: mstr in x, examples)):
            yield mstr


def get_longest_common_sequence(positives, negatives, cutoff=3):
    ms = gen_match_strings(positives, get_matches(positives), cutoff=cutoff)

    # find positive matches
    positive_matches = set(
        check_match_strings(positives, filter_substrings(ms), op=all)
    )

    # check against the negative examples
    negative_matches = set(check_match_strings(negatives, positive_matches, op=any))
    return positive_matches - negative_matches

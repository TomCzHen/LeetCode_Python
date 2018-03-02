#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/reverse-string/
Write a function that takes a string as input and returns the string reversed.
Example:
Given s = "hello", return "olleh".
"""


class Solution(object):

    def reverse_with_index(self, s: str) -> str:

        return s[::-1]

    def reverse_with_stack(self, s: str) -> str:

        stack = list(s)

        return ''.join(list(map(lambda x: stack.pop(), range(len(s)))))

    def reverse_with_loop(self, s: str) -> str:

        j = len(s) - 1
        r = []

        for i in range(len(s)):
            r.append(s[j])
            j -= 1

        return ''.join(r)

    def reverse_with_recursive(self, s: str) -> str:
        if len(s) == 1 or len(s) == 0:
            return s
        else:
            return self.reverse_with_recursive(s[1:]) + s[0]


def run_test_case(*args):
    try:
        for arg in args:
            assert Solution().reverse_with_index(arg[0]) == arg[1]
            assert Solution().reverse_with_stack(arg[0]) == arg[1]
            assert Solution().reverse_with_loop(arg[0]) == arg[1]
            assert Solution().reverse_with_recursive(arg[0]) == arg[1]
    except AssertionError as err:
        return "Wrong Answer - Input: {} Expected: {}".format(arg[0], arg[1])
    else:
        return "Run Code Status: Finished"


if __name__ == '__main__':
    test_case = [["", ""], ["A", "A"], ["ab", "ba"], ["AB", "BA"], ["abc", "cba"], ["ABC", "CBA"], ["Abc", "cbA"],
                 ["aBc", "cBa"], ["abC", "Cba"], ["a b", "b a"]]

    print(run_test_case(*test_case))

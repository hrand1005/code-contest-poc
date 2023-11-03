from typing import List, Tuple

"""
You're a dutiful NASA security guard honourably defending the esteemed
Moffet Field from evildoers. You have the vitally important task of
enforcing the NASA Moffet Field's newly implemented badge-swiping policy,
wherein each CMU Student is provided a badge to swipe in and out of
Moffet Field. But these wily youngsters rarely follow the rules, and you must
keep them in check.

To assess their compliance with the new badging policy, you've been provided
a list of 'badge-events' -- a day-long log of students using their badge to
enter and leave Moffet Field. The badge events are in order, i.e. for any i
badge_events[i] occurred before badge_events[i+1]. You also know that no
students were in Moffet Field at the beginning of the day or at the end
of the day.

Your goal is to return a list of students who are known to have violated
the badging policy, and firmly reprimand them.

The badge-swiping policy is comprised of the following rules:
- You may badge IN and OUT as many times as you'd like throughout the day
- You must badge IN when you enter Moffet Field
- You must badge OUT when you leave Moffet Field

It is only possible to badge IN when you enter Moffet Field, and badge OUT when
you leave Moffet Field.

Example 1:

input:
[
    ("John", "IN"),
    ("Mary", "IN"),
    ("Mary", "OUT"),
    ("Mary", "IN"),
    ("John", "OUT"),
    ("John", "IN"),
    ("John", "OUT"),
]
output:
[ "Mary" ]

Explanation:
Mary badged in, then out, then back into Moffet Field. Since we know that
Mary wasn't in Moffet Field at the end of the day, she must have forgot to
badge out when she left. Therefore mary violated the badging policy.

Example 2:
input:
[
    ("George", "OUT"),
    ("George", "IN"),
    ("George", "OUT"),
    ("James", "IN"),
    ("James", "IN"),
    ("James", "OUT"),
]
output:
[ "George", "James" ]

Explanation:
Both George and James are in violation of the badging policy; George starts the
day by badging OUT, which should not be possible since no students are in
Moffet Field at the start of the day. James badges IN twice in a row, which
means he must have left Moffet Field at some point without badging out.
"""


def report_badge_violations(badge_events: List[Tuple[str, str]]) -> List[str]:
    pass


if __name__ == '__main__':
    test1 = [
        ("John", "IN"),
        ("Mary", "IN"),
        ("Mary", "OUT"),
        ("Mary", "IN"),
        ("John", "OUT"),
        ("John", "IN"),
        ("John", "OUT"),
    ]

    test2 = [
        ("George", "OUT"),
        ("George", "IN"),
        ("George", "OUT"),
        ("James", "IN"),
        ("James", "IN"),
        ("James", "OUT"),
    ]

    print(f"test1 results: {report_badge_violations(test1)}")
    print(f"test2 results: {report_badge_violations(test2)}")

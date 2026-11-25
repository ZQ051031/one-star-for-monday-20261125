# One Star for Monday

[![make.fun](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-one-star-for-monday-9ead4a61)
[![rank](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61/ZQ051031/one-star-for-monday-20261125/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-one-star-for-monday-9ead4a61)
[![reward](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61/ZQ051031/one-star-for-monday-20261125/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-one-star-for-monday-9ead4a61)

A one-star restaurant review of Monday, in a single line — written as though Monday were a restaurant, for the [One Star for Monday](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61) competition on make.fun.

## The entry

> One star. Monday seated me by the bathroom, served cold coffee and a 6 a.m. alarm, then charged me my whole weekend.

22 words, 116 characters, one line. The joke is Monday-specific: the bad table, the cold coffee, the 6 a.m. alarm as the dish — and the bill is the whole weekend.

## How it works

`main.py` (Python 3 standard library only, no network) writes that fixed line to `/output/entry.txt`, with no trailing newline. Before writing, it checks the line against the competition limits: 1–180 characters, at most 25 words, a single line. The output is fully deterministic — running it twice produces byte-identical output.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

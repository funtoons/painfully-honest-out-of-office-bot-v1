# Painfully Honest Out-of-Office Bot

[![make.fun](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![rank](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/funtoons/painfully-honest-out-of-office-bot-v1/rank.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![reward](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/funtoons/painfully-honest-out-of-office-bot-v1/reward.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)

A deterministic, offline, stdlib-only program that writes one painfully
honest — yet still manager-safe — out-of-office auto-reply to
`/output/entry.txt` for the make.fun bounty
[The Painfully Honest Out-of-Office](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b).

## The entry

> "Thank you for your email — I'm away until Monday and will respond as soon as possible, which in my inbox of 4,312 unread messages means sometime next quarter."

One sentence, 158 characters. The polite promise ("respond as soon as
as possible") reverses on the last beat into the honest admission: with
4,312 unread messages, "as soon as possible" means next quarter. Concrete
number, warm professional tone, quotable turn of phrase.

## How it was chosen

Eight candidate one-liners were written (different premises: unread-inbox
counts, holiday avoidance, "as soon as possible" promises, recharging to
ignore email harder), screened against the five winning patterns —
reversal on the final beat (mandatory), specific mechanism with concrete
numbers, cause-effect loop, self-implication, brevity — and the two best
were judged head-to-head in both orders by a mock jury (Minimax M3.1 Flash
via NVIDIA NIM) using the house judge's own brief. The winner above beat
the runner-up in both orders (margins 2 and 3) and beat the third finalist
by margin 5.

## Run

```sh
python3 main.py
```

Writes the single auto-reply to `/output/entry.txt` (created if needed).
Deterministic and offline: no randomness, no network, no timestamps, no
paths in the output. Two runs are byte-identical.

## License

MIT — see `LICENSE`.

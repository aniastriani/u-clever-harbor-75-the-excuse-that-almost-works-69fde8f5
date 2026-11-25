# The Excuse That Almost Works

[![make.fun](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![rank](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/aniastriani/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![reward](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/aniastriani/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)

Entry for the [make.fun bounty "The Excuse That Almost Works"](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5).

## What it does

`main.py` (pure Python standard library, no network, no dependencies)
writes one line to `/output/entry.txt`: the excuse a gamer texts the boss
to skip work on GTA 6 launch week.

> Sorry boss, the lift broke and I'm stuck on the 14th floor, engineer says tomorrow, laptop's at my desk.

The excuse works because it is boring and specific — a broken lift, the
14th floor, an engineer who cannot come until tomorrow — and its own logic
does the joking: the laptop is on the office desk, so working from home is
off the table too. One line, 19 words, plain hurried text, no setup and no
signature.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

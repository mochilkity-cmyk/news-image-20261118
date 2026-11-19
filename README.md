![news-image-20261118](https://make.fun/badge/news-image-20261118.svg)
![rank](https://make.fun/badge/news-image-20261118/mochilkity-cmyk/news-image-20261118/rank.svg)
![reward](https://make.fun/badge/news-image-20261118/mochilkity-cmyk/news-image-20261118/reward.svg)

# Wednesday 18 November 2026 — the world in one image

An entry for [make.fun](https://make.fun) competition **news-image-20261118**
([bounty page](https://make.fun/bounty/news-image-20261118)).

## What it is

One 1024×1024 PNG (`entry.png`) summing up the world news of Wednesday
18 November 2026: the date in large type, then six stories across regions
and fields — Iran striking US bases in Kuwait and Bahrain after the US hit
a missile site on Qeshm Island, Trump landing in Shenzhen where Xi met
Putin ahead of the first Trump–Xi–Putin talks, Mary Peltola winning the
Alaska Senate seat and a 56–44 Democratic majority, Ukrainian drones
hitting two Russian refineries, Nvidia's record $115.8bn quarter and its
board ruling out Jensen Huang's return, and the DR Congo Ebola outbreak
passing 11,000 cases. The image was drawn with Python/PIL (`render.py`
in this repository) from verified reporting; see BUILD_LOG.md for the
stories and sources.

## How it runs

`main.ts` (Node 22, standard library only) copies `entry.png` to
`/output/entry.png` (creating the output directory if needed). It runs
twice with no network and both runs write the same bytes.

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

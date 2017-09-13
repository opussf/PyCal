# PyCal

This will be a rewrite of a very old project of mine.

The original created a 2-3 week calendar, using today as the first day to create a calendar of up coming events.
The idea came back recently when I was using a calendar display to organize my todo list.

Another idea of giving small tasks an amount of time, and then doing them when you have an amount of time available.

```
                            ┌────────────────────────────┐
                            │          January           │
┌───┬──┬───────────┬──┬─────┴─────┬──┬───────────┬──┬────┴──────┬──┬───────────┐
│   │ 2│           │ 3│           │ 4│           │ 5│           │ 6│           │
│   ├──┘           ├──┘           ├──┘           ├──┘           ├──┘           │
│ 0 │              │              │              │              │              │
│ 1 │              │              │              │              │              │
│   │              │              │              │              │              │
│   │              │              │              │              │              │
├───┼──┬───────────┼──┬───────────┼──┬───────────┼──┬───────────┼──┬───────────┤
│   │ 9│           │10│           │11│           │12│           │13│           │
│   ├──┘           ├──┘           ├──┘           ├──┘           ├──┘           │
│ 0 │              │              │              │              │              │
│ 2 │              │              │              │              │              │
│   │              │              │              │              │              │
│   │              │              │              │              │              │
└───┴──────────────┴──────────────┴──────────────┴──────────────┴──────────────┘
```


# interface:

-n, --new	      : create a new item
-2, --todo        : todo items (filter or flag for what to create)
-b, --birthday    : birthday items (filter or flag for what to create)
-p, --port        : start an HTTP server on the given port on the local machine.
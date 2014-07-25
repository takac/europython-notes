Fun with cPython Memory allocator
=================================
Tomasz Paczkowski
[@oinopion](https://twitter.com/oinopion)
[Europython Page](https://ep2014.europython.eu/en/schedule/sessions/9/)

Long lived webprocesses, periodically allocates boatloads of memory

    # lots of strings
    big = alloc(100000)
    report('After alloc')
    small = alloc(1)
    del big
    report('After del')
    import gc;
    gc.gc()
    report('After gc')

    $ python frag.py
    After alloc: 502244 kb used
    After del:   501484 kb used
    After gc: 501496 kb

#### Guppy
TraceAlloc - python 3 - well doc'd alternative

Usable and useful for memory leaks
Lacking docs... but self explanatory

    from guppy import hpy
    print hpy().heap()[:3]
    ...
    print hpy().heap()[:3]

Reports that only small amount used. Yet python still owns chunk on system.

#### Memory Fragmentation

    [     Big     ]
    [     Big     ][ Small ]
    [             ][ Small ]
    [             ][       ]

However removing the small chunk still doesn't clean up the big fragment

Python doesn't use stand malloc directly, too costly for small objects.
Has a more sophisticated allocator on top of malloc.
Improvements include 'Free lists'

#### Free lists
- For a handful of common types python keeps unused objects of similar size in so called free lists
- Those are most significantly lists, dicts, frames
- speeds up code execution immensely bu not hitting malloc and staying in userspace
- Capped sizes

Solutions to memory load
- Make better usage of memory
- Subprocesses
- jemalloc via LD_PREOAD (This overrides malloc system call, LD_PREOAD sets precedence to exported lib)

Conclusion
- malloc from glib is not best of breed
- do memory intensive work in subprocesses
- be mindful of C extensions

Everything you wanted to know about memory in Python
====================================================
Piotr Przymus
[Europython](https://ep2014.europython.eu/en/schedule/sessions/28/)

Types   32bit   64bit
int     12      24
long    14      30
    +2 bytes for each digit
float   16      24
complex 24      32
str     24      40
    +2 bytes for length
unicode

Call to check size

    sys.getsizeof(obj)

Object interning, pointers to objects, reuse pointers
Preallocated interned objects, instead of 'costly' alloc
Caveat: implementation specific
May change in future and therefore not documented

Interned
ints: -5 to 257
strs: empty and 1 length strings
unicode same
empty tuples

Use `intern` builtin (sys in py3) call to manually intern objects such as strings
Intern gives a reference to an interned string. 

#### Benefits
Performance gains on dictionary lookups
Reduce memory usage

Mutable Containers
Good strategies will slightly over allocate memory needed
Occasionally shrink for over allocated memory
Cheap to add at end of arrays, expensive to put in middle

Dictionarys and Sets
2/3 cap overallocation
if elements < 50000, quadruple cap

Memory allocation
best memory allocation for new classes with slots, listadata, tupledata, namedtule, 

python GC
Referencing counting with cycle dectecton
overloading `__del__()` can be dangerous 

psutil - inspecing sys utils
get process information 
psutil.Process(os.getpid('thing'))

memory_profiler
line by line profiler

    @profile 
    def mything(...):
        ...
    
    python -m memory_profiler

Can use as threshold trigger. When a memory target is hit, launch debugger.
mprof to give graph mem usage and functions run


objectgraph. Plots object graphs, find object cycles

heapy/meliae - Heap analysis tools
Heapy - used to find info about the objects in the heap

    from guppy import hpy
    hp = hpy()
    h1 = hp.heap()
    ...
    h2 = hp.heap()
    print h1 - h2

runsnakerun

Malloc alternatives, libjemalloc, libtcmalloc

procs- in some cases using different malloc impls may help to retrieve mem
from Cpthon back to system but may work against you



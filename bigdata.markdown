Big Data in Python
==================
Travis Oliphant
[Europython Page](https://ep2014.europython.eu/en/schedule/sessions/119/)
[@teoliphant](https://twitter.com/teoliphant)

- Data analysis
- Using C extensions in Python
- Need to use reference counting to use c ext properly
- Numpy based on Numarray and before that Numeric
- 2005 release of NumPy

### Keys to success
- Hard work - especially upfront
- It will be lonely, especially when more complicated
- Do whats "right"
    - Timing
    - Are you the right person
    - Strive for excellence
    - Do good
- Build a community
    - You will need others help
    - Listening to other people
    - Nuture empathy
- Patience
    - Good things take time
    - Influence of other factors

### NumPy
- Basis as computations on arrays
- NumPy arrays have to be same time
- Array scalars
- Vectorize your numpy
- Array orientated computations
- Hides for looping under the covers
- APL father of array orientated computations

### Pandas
- Structures of Arrays
- Labels on dimensions (indexes)
- Time series handling
- Familiar

### Why Python for Technical Computing
- Syntax gets out of your way
- White space perserves visual real estate
- Overloadable operators
- complex numbers built in

### Issues with Numpy
- Dtype diffcult to extend
- Almost an immemory database comparable to sql-lite
- Minimal support for multi-core/GPU

### PEP 3118
- Getting Numpy into Python
- Try to get use buffer protocol into python using numpy arrays
- Makes it possible for a heterogeneous world of array-like objects outside numpy to communicate
- Dual Encapsulation

### Future
- Data has mass
- Data is growing
- Keeping data where it is. Not pulling it from GPU/Hardware/Cache
- Data gravity!
- Contracts/Protocols
- Using Numba for high level code optimization
- Blaze for data adaptation


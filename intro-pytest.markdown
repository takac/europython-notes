Intro to pytest
===============
Andreas Pelme  
[@andreaspelme](https://twitter.com/andreaspelme)  
[speakerdeck.com/pelme](speakerdeck.com/pelme)  
[Europython Page](https://ep2014.europython.eu/en/schedule/sessions/100/)  
[Talk Recording](https://www.youtube.com/watch?v=LdVJj65ikRY)

py.test runs python unittest tests

### Less boilerplate code

    def x():
        x = 10
        assert x == 10

Uses built in assert statements
No subclasses of unittests


### Plugins
Parallelized
Twisted
Django
log capture
coverage

### Discovery

Recursive
Keywords

    py.test -k test_my_thing

Modules
Default uses `*_test.py` or `test_*.py`

Marking tests

    @pytest.mark.slow
    def test...

    pytest -m "slow"
    pytest" -m "not slow"

### Fixtures

Can inject arguments into test by name.

    @pytest.fixture
    def webdriver(..):
        ...

    def mytest(webdriver):
        # webdriver injected
        ...

Can adjust scope/lifespan of injected variables

    @pytest.fixture(scope='session')

    @pytest.fixture

### Extras

Run parallel with 2 processes

    py.test -n 2

?
    pip install pytest-xdist

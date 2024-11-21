import pytest
from valami.accu import Accumulator

@pytest.fixture
def accu(scope="function"):
    return Accumulator()

#accu2
@pytest.fixture
def accu2():
    yield Accumulator()
    print("DONE")
    
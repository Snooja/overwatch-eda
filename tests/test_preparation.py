
# Public modules
import pytest

# Internal modules
from src.preparation import DataGetter 

# Fixtures

@pytest.fixture
def myDataGetter():
    return DataGetter()

@pytest.mark.parametrize(
    "parameter",
    [
        "website",
        "downloadLinksList",
        "dataFolder"
    ]

)
def test_DataGetter_has_attributes(myDataGetter,parameter):
    assert getattr(myDataGetter,parameter) is not None

def test_DataGetter_runs(myDataGetter):
    myDataGetter.run()
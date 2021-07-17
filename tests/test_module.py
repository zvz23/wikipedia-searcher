import sys
import os
import pytest
sys.path.append(os.path.dirname(sys.path[0]))
from src.wikisearch.wikisearcher import WikiSearcher

@pytest.fixture
def searcher():
    return WikiSearcher()

def test_method1(searcher):
    result = searcher.search('React.js')
    assert "React (also known as React.js or ReactJS) is a free and open-source front-end JavaScript library" in result

def test_method2(searcher):
    result = searcher.search('The Hills')
    assert type(result) == dict

def test_method3(searcher):
    result = searcher.search('The Hills')
    assert len(result.keys()) == 3

def test_method4(searcher):
    result = searcher.search('Spark')
    assert len(result.keys()) == 9

def test_method5(searcher):
    result = searcher.search('Python')
    assert type(result) == dict

def test_method6(searcher):
    result = searcher.search('Python')
    assert len(result.keys()) == 8

def test_method7(searcher):
    result = searcher.search('adasdasdasdasd')
    assert result == False

def test_method8(searcher):
    result = searcher.search('2001')
    assert '2001 (MMI) was a common year starting on Monday' in result

def test_method9(searcher):
    result = searcher.search('Philippines', verbose=True)
    assert len(result) > 80





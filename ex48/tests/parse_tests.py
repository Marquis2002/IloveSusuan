from re import sub
from unittest import result
from nose.tools import*
from ex48 import parse
import operator



class EqualError(Exception):
    pass

def assert_equal(a, b):
    if operator.eq(a, b):
        pass
    else:
        raise EqualError("Something went wrong.")
# def assert_equal(a, b):
#     if a == b:
#         pass
#     else:
#         print(f"{a} <not equals> {b}")


def test_peek():
    word_list = [('noun', 'bear')]
    word_type = parse.peek(word_list)
    assert_equal(word_type, 'noun')



def test_match():
    word_list = [('noun', 'bear')]
    matched_word = parse.match(word_list, 'noun')
    assert_equal(matched_word, ('noun', 'bear'))
    assert_equal(parse.match(word_list, 'verb'), None)

def test_skip():
    word_list = [('noun', 'bear'), ('noun', 'princess'), ('verb', 'eat')]
    parse.skip(word_list, 'noun')
    assert_equal(word_list, [('verb', 'eat')])

def test_parse_verb():
    word_list = [('stop', 'the'), ('stop', 'at'), ('verb', 'eat')]
    verb = parse.parse_verb(word_list)
    assert_equal(verb, ('verb', 'eat'))

def test_parse_object():
    word_list = [('noun', 'bear'), ('noun', 'princess'), ('verb', 'eat')]
    object = parse.parse_object(word_list)
    assert_equal(object, ('noun', 'bear'))
    word_list = [('direction', 'west')]
    object = parse.parse_object(word_list)
    assert_equal(object, ('direction', 'west'))

def test_parse_subject():
    word_list = [('stop', 'the'), ('noun', 'princess')]
    subject = parse.parse_subject(word_list)
    assert_equal(subject, ('noun', 'princess'))

def test_parse_sentence():
    word_list = [('stop', 'the'), ('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'princess')]
    ans = parse.parse_sentence(word_list)
    target = parse.Sentence(('noun', 'bear'), ('verb', 'eat'), ('noun', 'princess'))
    assert_equal(ans.subj, target.subj)
    assert_equal(ans.verb, target.verb)
    assert_equal(ans.obj, target.obj)

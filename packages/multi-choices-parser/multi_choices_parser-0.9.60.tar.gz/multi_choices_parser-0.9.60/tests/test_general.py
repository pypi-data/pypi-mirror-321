import os.path as osp
import itertools
import json
import re
from typing import Iterator
from parser import MultiChoicesParser, DEFAULT_END_SYMB
import pytest
import random

TEST_END_SYMBS = [DEFAULT_END_SYMB, "ezaoijoir", 2168721468721]

def appleorange_grammars():
    yield [
        ['the', 'an', "a"],
        ['orange', 'apple', 'banana']
    ], None
    yield [
        ['the', 'an', "a", ""],
        ['orange', 'apple', 'banana']
    ], None
    yield [
        ['the', 'an', "a", ""],
        ['orange', 'apple', 'banana', '']
    ], None

def integer_grammars():
    for grammar, _ in grammars():
        alphabet = set()
        for l in grammar:
            for c in l:
                for a in c:
                    alphabet.add(a)
        alphabet = {k:i for i,k in enumerate(alphabet)}
        int_grammar = []
        for l in grammar:
            nl = []
            for c in l:
                nc = []
                for a in c:
                    nc.append((alphabet[a],))
                nl.append(nc)
            int_grammar.append(nl)
        yield int_grammar, None

def grammars() -> Iterator[list[list[str]]]:
    yield from appleorange_grammars()
    yield [[' '],
    ['France', 'Paris', 'Madrid', 'Montréal', 'Berlin'],
    ['.']], None

    yield [[' '],
    ['France', 'Paris', 'Madrid', 'Montréal', 'Berlin', 'U.S. Open Cup', 'Manchester United F.C.', "Box Office U.S."],
    ['.']], None


def all_grammars() -> Iterator[list[list[str]]]:
    yield from grammars()
    yield from integer_grammars()
    yield from alphabet_constrained_grammars()

def grammar_expected_next():
    to_parse = 'theorange'
    nexts = [
        'oabt',
        'h',
        'e',
        'oab',
        'r',
        'a',
        'n',
        'g',
        'e',
    ]
    yield list(appleorange_grammars())[1], to_parse, [tuple(x) for x in nexts if not isinstance(x, tuple)]
    grammar = [
        ['the', 'an', "a"],
        ['orange', 'apple', 'banana']
    ]
    alphabet = tuple('theanorgpbl') + ('anapp', 'le')
    to_parse = ('anapp',) + tuple('le')
    nexts = [
        tuple('ta') + ('anapp',),
        ('le','l'),
        ('e',),
    ]
    yield (grammar, alphabet), to_parse, nexts

def alphabet_constrained_grammars():
    yield [
        ['the', 'an', "a"],
        ['orange', 'apple', 'banana']
    ], 'theanorgplb'
    yield [
        ['the', 'an', "a"],
        ['orange', 'apple', 'banana']
    ], tuple('theanorglbp') + ('pp',)   
    yield [
        ['the', 'an', "a"],
        ['orange', 'apple', 'banana']
    ], tuple('theanorglb') + ('pp',)


    # Real world grammars (the alphabet is from the GPT2 tokenizer 
    # and the entities are the first entities from Wikidata)
    root = osp.dirname(__file__)
    entities = json.load(open(osp.join(root, 'choices.json')))
    alphabet = json.load(open(osp.join(root, 'alphabet.json')))
    
    yield [[' '],
    entities,
    ['.']], None

    yield [[' '],
    entities,
    ['.']], alphabet

    # yield [[' '],
    # entities,
    # ['.']], ["Ġ" + x for x in alphabet]

def split_according_to_alphabet(text : str | list[int], alphabet : str | tuple[str | tuple[int]]) -> tuple[list, bool]:
    res = []
    alphaset = set(alphabet)
    buf = []
    all_str = True
    for ch in text:
        buf.append(ch)
        all_str &= isinstance(ch, str)
        if all_str:
            letter = ''.join(itertools.chain(*buf))
        else:
            letter = tuple(itertools.chain(*buf))
        if letter in alphaset:
            res.append(letter)
            buf.clear()
            all_str = True
    return res, len(buf) == 0

def correct_test(to_parse : str, parser : MultiChoicesParser, reset=True, test_accept=True) -> None:
    random.seed(42112)
    if reset:
        parser.reset()
    initial_parser = parser.copy()
    to_parse2 = list(to_parse)
    to_parse, success = split_according_to_alphabet(to_parse2, parser.alphabet)
    to_parse += [parser.end_symb]
    if not success:
        return
    for c in to_parse:
        # Verify that parser is not finished while the parsing did not end
        assert not parser.finished and not parser.success
        parser.step(c)

        # Verify that initial parser and post-step parsers are different
        assert initial_parser != parser and hash(initial_parser) != hash(parser)
    else:
        print(to_parse)
        # Verify that the parser accepted the string to parse
        assert parser.finished and parser.success
    if test_accept:
        # Test .accepts method
        parser.reset()
        assert parser.accepts(to_parse)

        # Test a random substring of the string to parse
        assert parser.accepts(to_parse[:random.randint(0, len(to_parse)-1)])

def incorrect_test(to_parse : str, parser : MultiChoicesParser) -> None:
    parser.reset()
    to_parse = tuple(to_parse) + (parser.end_symb, )
    for c in to_parse:
        assert not parser.success
        parser.step(c)
    assert not parser.success and parser.finished
    parser.reset()
    assert not parser.accepts(to_parse)

@pytest.mark.parametrize(["grammar_alphabet", "to_parse", "nexts"],
                         grammar_expected_next())
@pytest.mark.parametrize('end_symb', TEST_END_SYMBS)
def test_next(grammar_alphabet, to_parse, nexts, end_symb) -> None:
    grammar, alphabet = grammar_alphabet
    parser = MultiChoicesParser(grammar, alphabet, end_symb)
    nexts = nexts + [(end_symb, )]
    for c, n in zip(split_according_to_alphabet(to_parse, parser.alphabet)[0] + [end_symb], nexts):
        assert sorted(parser.next()) == sorted(n)
        parser.step(c)
    

@pytest.mark.parametrize("grammar_alphabet",
                         all_grammars())
@pytest.mark.parametrize('end_symb', TEST_END_SYMBS)
def test_alphabet(grammar_alphabet, end_symb) -> None:    
    grammar, alphabet = grammar_alphabet
    parser = MultiChoicesParser(grammar, alphabet, end_symb)
    if alphabet is None:
        assert set(parser.alphabet) == set(c for y in grammar for x in y for c in x)

@pytest.mark.parametrize("grammar_alphabet", all_grammars())
@pytest.mark.parametrize('end_symb', TEST_END_SYMBS)
def test_parse_incorrect(grammar_alphabet, end_symb) -> None:
    grammar, alphabet = grammar_alphabet
    parser = MultiChoicesParser(grammar, alphabet, end_symb)
    to_parse_incorrect = [
        ('z'),
        ("them"),
        ("appl"),
        ("ana"),
        ("tzeorange")
    ]

    for p in to_parse_incorrect:
        incorrect_test(p, parser)

@pytest.mark.parametrize('grammar_alphabet', all_grammars())
@pytest.mark.parametrize('end_symb', TEST_END_SYMBS)
def test_parse_correct(grammar_alphabet, end_symb):

    grammar, alphabet = grammar_alphabet
    parser = MultiChoicesParser(grammar, alphabet, end_symb)
    to_parse_correct = [
        itertools.chain(*x) for x in itertools.product(*grammar)
    ]
    for p in to_parse_correct:
        correct_test(p, parser)

@pytest.mark.parametrize('grammar_alphabet', appleorange_grammars())
@pytest.mark.parametrize('end_symb', TEST_END_SYMBS)
def test_copy(grammar_alphabet, end_symb):
    grammar, alphabet = grammar_alphabet
    parser = MultiChoicesParser(grammar, alphabet, end_symb)

    parser.step('a')
    tests = grammar[1] + ['n'+x for x in grammar[1]]
    copies = [parser.copy(stateful=True) for _ in range(len(tests))]
    assert all(x == parser and hash(x) == hash(parser) for x in copies)
    for test, c in zip(tests, copies):
        correct_test(test, c, reset=False, test_accept=False)

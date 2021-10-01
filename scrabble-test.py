import time
import random
from base1 import get_display_output,set_keyboard_input
import new_word_list as test1

def test_scrabble_score_COUNT():


    set_keyboard_input(["Cabbage","CABBAGE","CAbbage","cabbage"])
    y=14
    result_1=test1.scrabble_score_COUNT()
    RESULT2=get_display_output()
    assert RESULT2
        #,"Test case function for test_scrabble_score_COUNT ... Passes

def test_scrabble_score_COUNT2():



    y=14
    result_1=test1.scrabble_score_COUNT()
    assert result_1 == y
        #,"Test case function for test_scrabble_score_COUNT ... Passes"
def test_scrabble_score_COUNT3():


    expected=14

    result_1=test1.scrabble_score_COUNT()
    assert result_1
        #,"Test case function for test_scrabble_score_COUNT ... Passes"
def test_scrabble_score_COUNT4():



    y=14
    result_1=test1.scrabble_score_COUNT()
    assert result_1
from ch04_glob.glob_any import Any
from ch04_glob.glob_either import Either
from ch04_glob.glob_lit import Lit
from ch04_glob.glob_null import Null
from ch05_text_parsing.parser import Parser

def test_parse_either_two_lit():
    assert Parser().parse("{abc,def}") == Either(
        [Lit("abc"), Lit("def")]
    )
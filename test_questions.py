# questions.py tests can be found here
# ------------------------------------

import questions

# Test if conversion to integer works as expected

def test_ask_user_integer(monkeypatch): # argumenttina monkeypatch-moduli (venv - pytest - monkeypatch.py)
    user_input = '100'
    monkeypatch.setattr('builtins.input', lambda _: user_input) # korvataan järjestelmän input() muuttujalla syote
    question = questions.Question('Anna kokonaisluku')
    assert question.ask_user_integer(False) == (100, 'OK', 0, 'Conversion successful')

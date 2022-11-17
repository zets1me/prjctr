from lesson19_Rona import *


def test_new_acc():
    bank = Bank(list())
    bank.open_account(123)
    acc = bank.bank_account[-1]
    assert bank.bank_account
    assert acc.get_balance()
    assert acc.get_account_number() == 123

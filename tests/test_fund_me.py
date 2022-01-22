from scripts.helpful_scripts import get_account
from scripts.deploy import deploy_fund_me


def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee()
    fund_txn = fund_me.fund({"from": account, "value": entrance_fee})
    fund_txn.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee

    withdraw_txn = fund_me.withdraw({"from": account})
    withdraw_txn.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0

from brownie import network, accounts, exceptions
import pytest
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fund_me


def test_fund():
    # Arrange
    account = get_account()
    fund_me = deploy_fund_me()
    minimum_fee = fund_me.getEntranceFee() + 100
    # Act
    tx = fund_me.fund({"from": account, "value": minimum_fee})
    tx.wait(1)
    # Assert
    assert fund_me.addressToAmountFunded(account.address) == minimum_fee


def test_withdraw():
    # Arrange
    account = get_account()
    fund_me = deploy_fund_me()
    minimum_fee = fund_me.getEntranceFee() + 100
    fund_me.fund({"from": account, "value": minimum_fee})
    # Act
    tx = fund_me.withdraw({"from": account})
    tx.wait(1)
    # Assert
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_withdraw_only_owner():
    # Only run this test in local environments
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only tested in local environments")
    # Arrange
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    # Act & Assert --> Setting up assert using 'with'.
    # It runs the following code checking for exception virtualmachineerror.
    # If exception is detected then the code exits and the test passes.
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})

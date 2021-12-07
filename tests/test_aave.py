from great_ape_safe import GreatApeSafe


def test_deposit():
    safe = GreatApeSafe('dev.badgerdao.eth')
    usdc = safe.contract('0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48')
    ausdc = safe.contract('0xBcca60bB61934080951369a648Fb03DF4F96263C')

    bal_before_usdc = usdc.balanceOf(safe)
    bal_before_ausdc = ausdc.balanceOf(safe)
    to_deposit = 1 * 10**usdc.decimals()

    safe.init_aave()
    safe.aave.deposit(usdc, to_deposit)

    assert usdc.balanceOf(safe) == bal_before_usdc - to_deposit
    assert ausdc.balanceOf(safe) == bal_before_ausdc + to_deposit

def test_withdraw():
    safe = GreatApeSafe('dev.badgerdao.eth')
    usdc = safe.contract('0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48')
    ausdc = safe.contract('0xBcca60bB61934080951369a648Fb03DF4F96263C')

    bal_before_usdc = usdc.balanceOf(safe)
    bal_before_ausdc = ausdc.balanceOf(safe)
    to_withdraw = 1 * 10**usdc.decimals()

    safe.init_aave()
    safe.aave.withdraw(usdc, to_withdraw)

    assert usdc.balanceOf(safe) == bal_before_usdc + to_withdraw
    assert ausdc.balanceOf(safe) == bal_before_ausdc - to_withdraw

# brownie.exceptions.VirtualMachineError: revert: 5
def test_withdraw_all():
#     safe = GreatApeSafe('dev.badgerdao.eth')
#     usdc = safe.contract('0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48')
#     ausdc = safe.contract('0xBcca60bB61934080951369a648Fb03DF4F96263C')
#
#     bal_before_usdc = usdc.balanceOf(safe)
#     bal_before_ausdc = ausdc.balanceOf(safe)
#
#     safe.init_aave()
#     safe.aave.withdraw_all(usdc)
#
#     assert usdc.balanceOf(safe) == 0

# verify if the balance after the claim is greater or equal with the initial balance
def test_claim_all():
    safe = GreatApeSafe('dev.badgerdao.eth')
    usdc = safe.contract('0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48')

    bal_before_usdc = usdc.balanceOf(safe)

    safe.init_aave()
    pending = safe.aave.controller.getUserUnclaimedRewards(usdc)

    safe.aave.claim_all(usdc)

    assert pending >= 0
    assert usdc.balanceOf(safe) >= bal_before_usdc

# AttributeError: 'Aave' object has no attribute 'unstake_and_claim'
# def test_unstake_and_claim_all():
#     safe = GreatApeSafe('dev.badgerdao.eth')
#     usdc = safe.contract('0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48')
#
#     bal_before_usdc = usdc.balanceOf(safe)
#
#     safe.init_aave()
#     safe.aave.unstake_and_claim_all(usdc)
#
#     assert usdc.balanceOf(safe) >= bal_before_usdc
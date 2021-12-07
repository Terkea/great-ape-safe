## Aave
- the `withdraw_all` throws an exception when you run it ```brownie.exceptions.VirtualMachineError: revert: 5```
- the `unstake_and_claim_all` has inside two deprecated functions, the deprecated versions are displayed to the left 
  side and to the right are the suggested replacements
    - blockNumber -> block_number
    - getBlock -> get_block
- at the bottom of the file the function tries to call a function that has yet not been defined `unstake_and_claim`
    


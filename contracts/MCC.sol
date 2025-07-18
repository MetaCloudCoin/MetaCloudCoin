// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MCC {
    string public name = "MetaCloudCoin";
    string public symbol = "MCC";
    uint8 public decimals = 18;
    uint public totalSupply = 1000000000 * 10 ** uint(decimals);
    mapping(address => uint) public balanceOf;

    constructor() {
        balanceOf[msg.sender] = totalSupply;
    }
}
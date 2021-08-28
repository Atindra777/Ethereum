pragma solidity ^0.6.0;

contract MyContract {
    int public myInt = 1;
    uint public myUint = 1;
    uint256 public myUint256 = 1;
    uint8 public myUint8 = 1;
    string public myString = "Hello, World!";
    bytes32 public myBytes32 = "Hello, World!";
    address public myAddress = 0xCB121CBb70aD7b8f567f7fBDdb19A7423d0E0cB6;
    
    struct MyStruct {
        uint myUint;
        string myString;
    }
    
    MyStruct public mystruct = MyStruct(1, "Hello, World!");
    
    function getValue() public pure returns(uint){
        uint value = 1;
        return value;
    }
}

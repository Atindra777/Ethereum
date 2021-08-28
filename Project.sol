pragma solidity ^0.6.0;

contract Project {
    string Random;
    string Timestamp;
    
    function setProject(string memory _Random, string memory _Timestamp) public {
        Random = _Random;
        Timestamp = _Timestamp;
    }
    
    function getProject() public view returns (string memory, string memory){
        return (Random, Timestamp);
    }
}

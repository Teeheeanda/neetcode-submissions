class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += f'{s}\0'

        return encoded_str
    def decode(self, s: str) -> List[str]:

        return s.split('\0')[:-1]
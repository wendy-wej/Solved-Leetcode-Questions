class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dict ={}
        for i in ransomNote:
            if i in magazine:
                if i not in mag_dict:
                    mag_dict[i] = magazine.count(i) - 1
                else:
                    if mag_dict[i] <= 0:
                        return False
                    mag_dict[i] = mag_dict[i]- 1
            else:
                return False
        return True
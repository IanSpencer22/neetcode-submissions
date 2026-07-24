class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in range(len(details)):
            info = details[i]
            age_str = int(info[11:13])
            if age_str > 60:
                count += 1

        return count
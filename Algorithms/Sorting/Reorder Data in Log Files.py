'''

Problem 937 | Reorder Data in Log Files
https://leetcode.com/problems/reorder-data-in-log-files/

'''

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        logs_list = [i.split() for i in logs]
        print(logs_list)
        letter_logs, digit_logs = [], []
        for log in logs_list:
            if log[1].isnumeric():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        return [" ".join(i) for i in sorted(letter_logs, key = lambda x: (x[1:], x[0])) + digit_logs]
                

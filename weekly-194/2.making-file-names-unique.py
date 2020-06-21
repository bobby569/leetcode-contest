"""
https://leetcode.com/contest/weekly-contest-194/problems/making-file-names-unique/
"""


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        res, dic = [], {}
        for n in names:
            if n not in dic:
                res.append(n)
                dic[n] = 0
            else:
                dic[n] += 1
                i = dic[n]
                while True:
                    tmp = '{}({})'.format(n, i)
                    if tmp not in dic:
                        res.append(tmp)
                        dic[tmp] = 0
                        break
                    i += 1
        return res

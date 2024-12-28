class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def get_combination(candidates, target):
            res_list = []
            for j in range(len(candidates)-1,-1,-1):
                if candidates[j]>target:
                    continue

                elif candidates[j]==target:
                    res_list.append([target])
                     
                else: # candidates[j]<target:
                    tmp_list = get_combination(candidates[:j], target)
                    tmp_list = [x for x in tmp_list if x]
                    res_list += tmp_list
                     
                    cur_candidate = candidates[j]
                    base_list = [cur_candidate]
                    cur_target = target - cur_candidate
                    while cur_target>0:
                        tmp_list = get_combination(candidates[:j], cur_target) 
                        tmp_list = [x+base_list for x in tmp_list if x]
                        res_list += tmp_list
                        cur_target = cur_target - cur_candidate
                        base_list.append(cur_candidate)

                    if cur_target==0:
                        res_list.append(base_list)

                    return res_list

            return res_list
 

        res_list = get_combination(candidates, target)
        return res_list
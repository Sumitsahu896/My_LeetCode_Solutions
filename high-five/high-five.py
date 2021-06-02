class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
#         mapping = {}
#         result = []
        
#         for item in items:
#             if item[0] in mapping:
#                 mapping[item[0]].append(item[1])
#             else:
#                 mapping[item[0]] = [item[1]]
                
#         for x, y in mapping.items():
#             y.sort(reverse=True)
#             i = 0
#             total = 0
#             while i < 5 and i < len(y):
#                 total += y[i]
#                 i += 1
                
#             result.append([x, total//i])
        
#         result.sort()    
    
#         return result
#         mapping = defaultdict(list)
        
#         for id, item in items:
#             mapping[id].append(item)
            
#         result = []
        
#         for i in sorted(mapping.keys()):
#             heapq.heapify(mapping[i])
#             result.append([i, sum(heapq.nlargest(5, mapping[i])) // 5])
            
#         return result
    
    
        mapping = {}
        result = []
        
        # Adding all the values in the array
        for item in items:
            if item[0] in mapping:
                mapping[item[0]].append(item[1])
            else:
                mapping[item[0]] = [item[1]]
                
        for x, y in mapping.items():
            y.sort(reverse = True)
            i = 0
            total = 0
            while i < 5 and i < len(y):
                total += y[i]
                i += 1
                
            result.append([x, total//i])
            
        return sorted(result)
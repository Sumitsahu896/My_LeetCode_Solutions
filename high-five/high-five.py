class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        mapping = {}
        result = []
        for x in items:                        # For every student, create a list of their scores using dictionary
            if x[0] in mapping:
                mapping[x[0]].append(x[1])
            else:
                mapping[x[0]] = [x[1]]

        for x, y in mapping.items():            # Traverse through the dictionary elements and take average of sorted scores.
            y.sort(reverse=True)
            total = 0
            i = 0
            while i < 5 and i < len(y):         # Since the problem statement doesn't say there will be at least 5 scores for each student, 
                total += y[i]                   # instead of using sum() and dividing by 5, I used loop and divided by i.
                i += 1
            result.append([x, total//i])        # Store the average for every student id in result
            result.sort()
            

        return result
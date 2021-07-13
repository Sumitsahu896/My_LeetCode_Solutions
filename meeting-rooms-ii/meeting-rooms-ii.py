class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # If there is no meeting to schedule then no room needs to be allocated
        if not intervals:
            return 0
        
        # The heap initialization
        free_room = []
        
        # Sort the meetings in the increasing order of their start time
        intervals.sort(key = lambda x:x[0])
        
        heapq.heappush(free_room, intervals[0][1])
        
        for i in intervals[1:]:
            if free_room[0] <= i[0]:
                heapq.heappop(free_room)
                
            heapq.heappush(free_room, i[1])
            
        return len(free_room)
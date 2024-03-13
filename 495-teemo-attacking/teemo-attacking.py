class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # result = []

        # for time in timeSeries:
        #     result += [i for i in range(time, time + duration)]

        # return len(set(result))

        time_poison = 0
        last_time = timeSeries[0]

        for time in timeSeries[1:]:
            if last_time + duration - 1 < time:
                time_poison += duration
            else:
                time_poison += time - last_time
            last_time = time
        
        time_poison += duration
        return time_poison
        
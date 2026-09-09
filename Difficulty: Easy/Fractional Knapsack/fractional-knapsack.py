class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        #code here
        items = []

        for i in range(len(val)):
            ratio = val[i] / wt[i]
            items.append((ratio, val[i], wt[i]))

        items.sort(reverse=True)

        to_value = 0

        for ratio, val, wt in items:
            if capacity >= wt:
                to_value += val
                capacity -= wt
            else:
                to_value = to_value + ratio * capacity
                break

        return to_value
# Uses python3
import sys
def get_optimal_value(capacity, weights, values):
    value = 0
    rank=[0]*n
    new_values=[0]*n
    new_weights=[0]*n
    # sorting
    for j in range(n):
        div=values[j]/weights[j]
        rank[j]=div
    for i in range(n):
        new_values[i]=values[rank.index(max(rank))]
        new_weights[i]=weights[rank.index(max(rank))]
        rank[rank.index(max(rank))]=0
    #packing
    for i in range(n):
        if (capacity==0):
            return value
        a=min(new_weights[i],capacity)
        value=value+a*(new_values[i]/new_weights[i])
        new_weights[i]=new_weights[i]-a
        capacity=capacity-a
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))

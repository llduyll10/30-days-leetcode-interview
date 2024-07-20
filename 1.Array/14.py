def canCompleteCircuit(gas, cost):
    totalTank = 0 #Tổng lượng xăng hiện có.
    currentTank = 0 # Lượng xăng hiện có để đi từ một trạm đến trạm tiếp theo.
    startPosition = 0 #Chỉ số của trạm bắt đầu mà ta xét.

    for i in range(len(gas)):
        totalTank += gas[i] - cost[i]
        currentTank += gas[i] - cost[i] # Cộng dồn lượng xăng từ trạm i để đi đến trạm i+1.

        if currentTank < 0:
            startPosition = i + 1 #Cập nhật trạm bắt đầu mới.
            currentTank = 0 #Reset lượng xăng hiện có về 0.
    return startPosition if totalTank  >= 0 else -1

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

print(canCompleteCircuit(gas, cost))
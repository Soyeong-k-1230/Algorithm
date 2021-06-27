from collections import deque
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
# tickets = [["ICN","AAA"], ["ICN","BBB"], ["BBB","ICN"]]
# tickets = [["ICN", "A"], ["A", "B"], ["B", "A"], ["A", "ICN"], ["ICN", "A"]]
tickets = [["INC", "A"],["INC", "A"],["INC", "A"],["A", "INC"],["A", "INC"]]
# tickets = [["ICN", "A"], ["ICN", "A"], ["A", "ICN"]]

from collections import deque

def solution(tickets):
    answer = []
    path = ["ICN"]
    visited = [0] * len(tickets)
    new = []
    Q = deque()

    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            new.append(tickets[i][1])
    new.sort()

    for i in range(len(new)):
        for j in range(len(tickets)):
            if 0 in visited:
                visited = [0] * len(tickets)
                path = ["ICN"]
            else:
                answer = path
                break
            if new[i] == tickets[j][1] and tickets[j][0] == "ICN":
                Q.append((tickets[j][0], tickets[j][1]))

                while Q:
                    check = []
                    st, ed = Q.popleft()
                    if st == path[-1]:
                        path.append(ed)
                    else:
                        continue

                    for k in range(len(tickets)):
                        if tickets[k][0] == st and tickets[k][1] == ed and visited[k] == 0:
                            visited[k] = 1
                            temp = k
                            break

                    if not 0 in visited:
                        break

                    for k in range(len(tickets)):
                        if tickets[k][0] == ed and visited[k] == 0:
                            check.append(tickets[k][1])
                    if check:
                        check.sort()
                    else:
                        path.pop()
                        visited[temp] = 0
                        continue

                    for k in range(len(check)):
                        for j in range(len(tickets)):
                            if check[k] == tickets[j][1] and tickets[j][0] == ed:
                                Q.append((tickets[j][0], tickets[j][1]))

    return answer

print(solution(tickets))

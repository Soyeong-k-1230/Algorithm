def solution(n, t, m, timetable):
    answer = ''
    bus = []; people = []
    start = 900
    for i in range(n):
        tmp = t * i
        bus.append(start + (tmp // 60) * 100 + (tmp % 60))
    last = max(bus)

    for time in timetable:
        hour, minute = time.split(':')
        people.append(int(hour) * 100 + int(minute))
    people.sort()
    bus_people = [[] for _ in range(n)]

    for p_time in people:
        for i in range(n):
            if p_time <= bus[i]:
                if len(bus_people[i]) < m:
                    bus_people[i].append(p_time)
                    break
    bus_people.reverse()

    if len(bus_people[0]) < m:
        result = last
    else:
        result = max(bus_people[0]) - 1
        if result % 100 > 60:
            result -= 40

    result_h = '0' + str(result // 100) if result // 100 < 10 else str(result // 100)
    result_m = '0' + str(result % 100) if result % 100 < 10 else str(result % 100)

    answer = result_h + ":" + result_m
    return answer

# n회 t분 간격 하나의 셔틀에는 최대 m명의 승객
# 1회 1분 간격 하나의 셔틀에는 최대 5명

print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(10, 60, 45, ["23:59", "23:59", "23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59"]))


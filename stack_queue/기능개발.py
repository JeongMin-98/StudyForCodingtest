"""
    프로그래머스 > 코딩테스트 연습 > 스택/큐 > 기능개발

    각 기능은 진도가 100프로일때 서비스에 반영가능

    각 기능의 개발 속도는 모두 다름

    뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발되었을 시
    뒤에 있는 기능은 앞에 있는 기능이 완료 하였을 때 배포됨

    각 배포 별로 몇 개의 기능이 배포되었는지
"""
def solution(progress, speeds):
    answer = []
    workdone = []
    while len(progress) > 0:
        work = progress.pop(0)
        speed = speeds.pop(0)

        remain = (100 - work) % speed
        if remain:
            days = (100-work) // speed + 1
        else:
            days = (100-work) // speed

        workdone.append(days)
    release_day = workdone.pop(0)
    release_work = 1
    while len(workdone) > 0:
        new_release = workdone.pop(0)
        if release_day >= new_release:
            release_work += 1
        else:
            answer.append(release_work)
            release_day = new_release
            release_work = 1
    answer.append(release_work)
    return answer

print(solution([93,30,55],[1,30,5]))
# def solution(progresses, speeds):
#     answer = []
#     n = len(progresses)
#     work_done = [0] * n
#     end_progress = []
#     day = 1
#     # progresses[i] >= 100=> work_done[i] = 1
#     while len(progresses) > 0:
#         if day == 1:
#             day_progresses = [num + day * speed if work_done_bool == 0 else num
#                               for num, speed, work_done_bool in
#                               zip(progresses, speeds, work_done)]
#         else:
#             day_progresses = [num + day * speed if work_done_bool == 0 else cur_progress
#                               for cur_progress, num, speed, work_done_bool in
#                               zip(day_progresses, progresses, speeds, work_done)]
#         work_done = [1 if progress >= 100 else 0 for progress in day_progresses]
#
#
#         while 1 in work_done:
#             if work_done[0] == 1:
#                 work_done.pop(0)
#                 speeds.pop(0)
#                 end_progress.append(progresses.pop(0))
#             else:
#
#                 break
#         if len(end_progress) > 0:
#             answer.append(len(end_progress))
#             end_progress = []
#         day += 1
#
#
#     return answer#


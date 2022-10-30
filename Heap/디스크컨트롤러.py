import heapq
import math
def solution(jobs):
    answer = 0
    heapq.heapify(jobs)
    arrive_job = []
    jobs_load_time = []
    time = 0
    i = 0
    while not (i > len(jobs)-1 and len(arrive_job) < 1):
        # while len(jobs) != 0:
        #     job = heapq.heappop(jobs)
        #     if job[0] == time:
        #         heapq.heappush(arrive_job, (job[1], job[0], i))
        #         i += 1
        #     else:
        #         heapq.heappush(jobs, job)
        #         break

        while len(jobs) != 0:
            job = heapq.heappop(jobs)
            if job[0] == time:
                heapq.heappush(arrive_job, [job[1], job[0]])
            else:
                heapq.heappush(jobs, job)
                break

        if len(arrive_job) >= 1:
            job_info = heapq.heappop(arrive_job)
            job_work_time = job_info[0]
            job_start_time = job_info[1]
            if len(jobs) >= 1:
                next_job_info = heapq.heappop(jobs)
                if (job_work_time + time) >= next_job_info[0]:
                    job_work_time -= (next_job_info[0]-time)
                    time += (next_job_info[0]-time)
                    heapq.heappush(arrive_job, [next_job_info[1], next_job_info[0]])
                else:
                    time += 1
                    job_work_time -=1
                    # time += job_work_time
                    # job_work_time = 0
                    heapq.heappush(jobs, next_job_info)
            else:
                time += job_work_time
                job_work_time = 0

            if job_work_time == 0:
                jobs_load_time.append(time - job_start_time)
            else:
                heapq.heappush(arrive_job, [job_work_time, job_start_time])
        else:
            time = job[0]
            # time += 1
    print(jobs_load_time)
    answer = sum(jobs_load_time) / len(jobs_load_time)
    answer = math.floor(answer)
    return answer


# print(solution([[0,1],[1,10],[2,6],[3,4]]))
# print(solution([[1, 10],[1,5], [2, 3], [15, 2], [5, 11]]))
# print(solution([[0, 3], [1, 9], [2, 6]]))
# print(solution(	[[0, 3], [4, 4], [5, 3], [4, 1]]))

# print(solution([[24, 10], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))
print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))
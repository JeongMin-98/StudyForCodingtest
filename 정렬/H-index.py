def solution(citations):
    answer = 0
    hindex = [0] * len(citations)
    for i in range(min(citations), len(citations)):
        h = i
        upper_h = []

        for cite in citations:
            if h <= cite:
                upper_h.append(cite)

        upper_h_papers = len(upper_h)

        no_h_papers = len(citations) - upper_h_papers

        if upper_h_papers >= h >= no_h_papers:
            hindex.append(h)
    answer = max(hindex)
    return answer


print(solution([3,0,6,1,5]))
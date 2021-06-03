class Solution:
    def scheduleCourse(self, courses):
        # Sory courses by finish time
        courses.sort(key=lambda x: (x[1], x[0]))
        # Track a few things
        tot_time = 0 # Increment each time a course is added
        course_cnt = 0
        cm = 0
        durations = []
        for c in courses:
            course_len = c[0]
            # If the current course can be complete before its deadline then take it
            if tot_time + course_len <= c[1]:
                if course_len > cm:
                    cm = course_len
                tot_time += course_len
                durations.append(course_len)
                course_cnt += 1
            # If not, take it instead of the longest duration course already taking (if there's a longer one)
            # Need a good way to order course lengths
            else:
                if len(durations) > 0:
                    if course_len < cm:
                        tot_time = tot_time - cm + course_len
                        durations.remove(cm)
                        durations.append(course_len)
                        cm = max(durations)
        return course_cnt
                
# Could rewrite this as a Heap since I only care about the current max value. That's very cool!
# There's a python import heapq


if __name__ == "__main__":
    courses = [[5,5],[4,6],[2,6]]
    sol = Solution()
    print(sol.scheduleCourse(courses))
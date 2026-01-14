class Solution(object):
    def separateSquares(self, squares):
        events = []

        for x, y, l in squares:
            events.append((y, 1, x, x + l))      # start
            events.append((y + l, -1, x, x + l)) # end

        events.sort()

        # merge active x-intervals
        def merged_width(intervals):
            if not intervals:
                return 0
            intervals.sort()
            total = 0
            cur_l, cur_r = intervals[0]

            for l, r in intervals[1:]:
                if l > cur_r:
                    total += cur_r - cur_l
                    cur_l, cur_r = l, r
                else:
                    cur_r = max(cur_r, r)

            total += cur_r - cur_l
            return total

        active = []
        prev_y = events[0][0]
        total_area = 0

        # First pass → compute total union area
        for y, typ, x1, x2 in events:
            dy = y - prev_y
            if dy > 0:
                total_area += merged_width(active) * dy

            if typ == 1:
                active.append((x1, x2))
            else:
                active.remove((x1, x2))

            prev_y = y

        half = total_area / 2.0

        # Second pass → find split y
        active = []
        prev_y = events[0][0]
        area_so_far = 0

        for y, typ, x1, x2 in events:
            dy = y - prev_y
            if dy > 0:
                width = merged_width(active)
                area_here = width * dy

                if area_so_far + area_here >= half:
                    return prev_y + (half - area_so_far) / width

                area_so_far += area_here

            if typ == 1:
                active.append((x1, x2))
            else:
                active.remove((x1, x2))

            prev_y = y

        return prev_y

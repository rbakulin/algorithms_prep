import unittest


class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        """
        Method adds a new request (with request's time "t" in milliseconds) in the requests list and returns the count
        of requests within past 3000 milliseconds (including the new request)
        """
        count_requests_last_3000 = 0
        self.requests.append(t)
        for r in self.requests:
            if t - 3000 <= r <= t:
                count_requests_last_3000 += 1
        return count_requests_last_3000

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


class TestRecentCounter(unittest.TestCase):
    def test_ping(self):
        """
        [], [1], [100], [3001], [3002]
        [null, 1, 2, 3, 3]
        RecentCounter recentCounter = new RecentCounter();
        recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
        recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
        recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
        recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3
        """
        # self.assertEqual(decode_string(s="3[a]2[bc]"), "aaabcbc")
        requests_example = [[], [1], [100], [3001], [3002]]
        answers_valid = [None, 1, 2, 3, 3]
        answers_real = []
        obj = RecentCounter()
        for request in requests_example:
            if not request:
                answers_real.append(None)
            else:
                last_request = request[0]
                last_3000_requests = obj.ping(last_request)
                answers_real.append(last_3000_requests)

        for i in range(len(answers_valid)):
            self.assertEqual(answers_valid[i], answers_real[i])


if __name__ == "__main__":
    unittest.main()

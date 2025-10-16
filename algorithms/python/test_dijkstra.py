import unittest
from dijkstra import dijkstra

class TestDijkstra(unittest.TestCase):
    def test_simple_graph(self):
        graph = {
            0: [(1, 4), (2, 1)],
            1: [(3, 1)],
            2: [(1, 2), (3, 5)],
            3: []
        }
        dist = dijkstra(graph, 0)
        self.assertEqual(dist[0], 0)
        self.assertEqual(dist[1], 3)  # 0 → 2 → 1 cost 1 + 2
        self.assertEqual(dist[2], 1)
        self.assertEqual(dist[3], 4)  # via 0 → 2 → 1 → 3 or 0→1→3 whichever minimal

if __name__ == "__main__":
    unittest.main()

import unittest
from chord import  get_fingers, get_key_loc, get_query_path
class TestDHTChord(unittest.TestCase):
    def test_get_fingers(self):
        nodes = [112, 96, 80, 16, 32, 45]
        m = 7
        expected_finger_table = {
            16: [32, 32, 32, 32, 32, 80, 80],
            32: [45, 45, 45, 45, 80, 80, 96],
            45: [80, 80, 80, 80, 80, 80, 112],
            80: [96, 96, 96, 96, 96, 112, 16],
            96: [112, 112, 112, 112, 112, 16, 32],
            112: [16, 16, 16, 16, 16, 16, 80]
        }
        finger_table = get_fingers(nodes, m)
        for node in nodes:
            self.assertEqual(finger_table[node], expected_finger_table[node], f"Finger table for node {node} is incorrect.")
    
    def test_get_key_loc(self):
        nodes = [112, 96, 80, 16, 32, 45]
        m = 7
        file_key = 42
        expected_location = 45
        location = get_key_loc(nodes, file_key, m)
        self.assertEqual(location, expected_location, f"Expected key location to be {expected_location}, but got {location}.")

    def test_get_query_path(self):
        nodes = [112, 96, 80, 16, 32, 45]
        m = 7
        file_key = 42

        # Đường đi truy vấn khi node xuất phát là 80
        query_node = 80
        expected_query_path_80 = [80, 16, 32, 45]
        query_path_80 = get_query_path(nodes, file_key, query_node, m)
        self.assertEqual(query_path_80, expected_query_path_80, f"Expected query path for node {query_node} to be {expected_query_path_80}, but got {query_path_80}")

        # Đường đi truy vấn khi node xuất phát là 96
        query_node = 96
        expected_query_path_96 = [96, 32, 45]
        query_path_96 = get_query_path(nodes, file_key, query_node, m)
        self.assertEqual(query_path_96, expected_query_path_96, f"Expected query path for node {query_node} to be {expected_query_path_96}, but got {query_path_96}")

        # Đường đi truy vấn khi node xuất phát là 45
        query_node = 45
        expected_query_path_45 = [45]
        query_path_45 = get_query_path(nodes, file_key, query_node, m)
        self.assertEqual(query_path_45, expected_query_path_45, f"Expected query path for node {query_node} to be {expected_query_path_45}, but got {query_path_45}")

if __name__ == "__main__":
    unittest.main()
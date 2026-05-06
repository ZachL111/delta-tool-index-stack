import unittest

from src.delta_tool_index_stack.domain_review import DomainReview, review_lane, review_score


class DomainReviewTests(unittest.TestCase):
    def test_review_lane(self) -> None:
        item = DomainReview(79, 48, 29, 69)
        self.assertEqual(review_score(item), 188)
        self.assertEqual(review_lane(item), "ship")


if __name__ == "__main__":
    unittest.main()

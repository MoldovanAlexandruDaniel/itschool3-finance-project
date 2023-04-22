import unittest
from Domain.users.factory import UserFactory
from Domain.users.repo import UserRepo


class UserRepositoryTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.users_file = "test_users.json"
        cls.repo = UserRepo(cls.users_file)

    def test_it_adds_a_user(self):
        expected_username = "a-username"
        new_user = UserFactory().make_new(expected_username)

        self.repo.add(new_user)

        actual_users = self.repo.get_all()

        self.assertEqual(1, len(self.repo.get_all()))
        self.assertEqual(expected_username, actual_users[0].username)

    def test_it_reads_a_user_from_the_system(self):
        repo = UserRepo(self.users_file)

        actual_users = repo.get_all()

        self.assertEqual(1, len(actual_users))


if __name__ == "__main__":
    unittest.main()

from Classes import User, Server

class TestUser:

    def test__init__(self):
        tests = [
            ((1, 1), (1, 1)),
            (("name", Server), ("name", Server))
        ]

        for test in tests:
            user = User(*test[0])
            if (user.nick_name, user.server) == test[i]:
                print("Test pass")
            else:
                print("Test error: {}".format(test))

a = TestUser()
a
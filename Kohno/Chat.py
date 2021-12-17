from Classes import User, Server

server = Server()


user_list = []
for i in range(5):
    user_list.append(User(str(i), server))

for user in user_list:
    user.send_message("sdfsf" + user.nick_name)
    user.get_message_list(is_print=True)
    print()
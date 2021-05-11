import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message})


# API-ключ
token = "dcf135b178e1d74953d62133e6c8d72cb3c38facbb3e99d0761dca753732700c04d16be8dd7c128a6e3d6"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)
vk.auth()

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            request = event.text

            # Каменная логика ответа
            if request == "/start":
                write_msg(event.user_id, "Приветствую вас в нашем сообществе, для того что бы получить дополнительную "
                                         "информацию и/или узнать ответы на часто задаваемые вопросы")
            elif request == "F.A.Q.":
                write_msg(event.user_id, "...")  # TODO:Добавить F.A.Q.
            else:
                write_msg(event.user_id, "Упс, кажется вы где-то ошиблись")

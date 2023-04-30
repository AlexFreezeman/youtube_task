from utils.channel import Channel
from utils.video import Video, PLVideo


def main():
    #    channel_id = 'UCMCgOm8GZkHp8zJ6l7_hIuA'  # вДудь
    #    channel_id = 'UC1eFXmJNkjITxPFWTy6RsWg'  # Редакция

    #    channel = Channel(channel_id)
    #    channel.print_info()

    #   task 2:
#    vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
#    redact = Channel('UC1eFXmJNkjITxPFWTy6RsWg')
#    vdud.print_info()
#    print(vdud.title)
#    print(vdud.video_count)
#    print(vdud.url)
#    print(vdud.sub_count)

    # менять не можем
    #    vdud.channel_id = 'Новое название'
    #    print(vdud.channel_id)

    # можем получить объект для работы с API вне класса
    # print(Channel.get_service())
    # print(vdud.get_service())

    # создать файл 'vdud.json' в данными по каналу
#    vdud.save_json('vdud.json')

#    print(redact.title)
#    print(redact.video_count)
#    print(redact.url)
#    redact.save_json('redact.json')
#    print(redact.sub_count)

    #   task 3:
#    print(vdud)
#    print(redact)
#    print(vdud == redact)
#    print(vdud > redact)
#    print(vdud < redact)
#    print(vdud + redact)

    # task 4:
    video1 = Video('9lO06Zxhu88')
    print(video1)

    video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
    print(video2)


if __name__ == "__main__":
    main()

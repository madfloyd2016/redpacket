import pytest
import wxpy as wx


def get_me(bot):
    name = "哦兜狗"
    me = bot.friends().search(name)

    if len(me) < 1:
        raise "not found me"

    return me[0]


def debug_share(msg):
    pytest.set_trace()

    print(msg)


def register_share(bot, func):
    register = bot.register(except_self=False)
    register(func)


def main():
    bot = wx.Bot()

    # search me
    me = get_me(bot)

    # register func
    register_share(bot, debug_share)

    bot.join()


if __name__ == "__main__":
    main()

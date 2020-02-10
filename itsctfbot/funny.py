#!/usr/bin/env python3

import random


def get_random_pink_quotes():

    pink_quotes_list = [
        '你行你上啊！',
        '如果你觉得这个国家黑暗，那你就去当公务员改变这个国家啊！',
        'GFW是为了保护我们中国人的思维不受你们西方宣传机构洗脑才存在的！',
        '我和我的祖国一刻也不能分离！',
        '你就是个牧羊犬！',
        '要相信政府相信党！',
        '多难兴邦！',
        '厉害了我的国！',
        '打倒美帝国主义！',
    ]

    return random.choice(pink_quotes_list)


def get_random_name():

    name_list = [
        '屁',
        'XX',
        'shi',
        # '爸爸',
        # '妹妹'
    ]

    return random.choice(name_list)


def check_verb(text):

    verb_list = [
        # a
        '按',
        # b
        '抱',
        '播',
        '披',
        # c
        '察',
        '搀',
        '抽',
        '捶',
        '持',
        '擦',
        '吃',
        '猜',
        # d
        '盯',
        '瞪',
        '打',
        '睹',
        '捣',
        '读',
        # e
        # f
        '飞',
        '扶',
        # g
        '顾',
        '观',
        # h
        '喝',
        # i
        # j
        '击',
        '拣',
        '捡',
        '举',
        '掘',
        # k
        '看',
        '窥',
        '瞰'
        '考',
        # l
        '落',
        '搂',
        '拉',
        '来',
        # m
        '瞄',
        # n
        '凝',
        '拿',
        '捏',
        '扭',
        # o
        # p
        '瞥',
        '盼',
        '抛',
        '嫖',
        # q
        '瞧',
        '瞅',
        '觑',
        '擒',
        '敲',
        '掐',
        # r
        # s
        '视',
        '撕',
        '撒',
        '搜',
        '睡',
        '是',
        '说',
        # t
        '眺',
        '推',
        '弹',
        '提',
        '托',
        '拖',
        # u
        # v
        # w
        '望',
        '挖',
        '玩',
        # x
        '笑',
        '写',
        '学',
        # y
        '有',
        '用',
        # z
        '走',
        '在',
        '转',
        '捉',
        '摘',
        '撞',
        '揍',
        '做',
        # sp
        '404',
    ]

    for c in verb_list:
        if c in text:
            return c

    return None

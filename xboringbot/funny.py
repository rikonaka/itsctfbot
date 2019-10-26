#!/usr/bin/env python3

import random


def get_random_name():

    name_list = [
        '屁',
        'XX',
        '爸爸',
        '妹妹'
    ]

    return random.choice(name_list)


def check_verb(message):

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
        # z
        '走',
        '在',
        '转',
        '捉',
        '摘',
        '撞',
        '揍',
        '做',
    ]

    for c in verb_list:
        if c in message:
            return c

    return None

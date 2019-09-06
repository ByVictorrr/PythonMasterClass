#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 victor <victor@archlinux>
#
# Distributed under terms of the MIT license.

"""
"""
text = "what have the romands ever done for us"

capitals = [char.upper() for char in text]

print(capitals)


words = [word.upper() for word in text.split(' ')]
print(words)

# stupid versoin of comprehension
lc_word = [word for word in text.split(' ')]

# how it should be done
lc_word = text.split(' ')








# Generated by Grammarinator 19.3

from itertools import chain
from grammarinator.runtime import *

charset_0 = list(chain(range(49, 58)))
charset_1 = list(chain(range(48, 58)))


class pet_storeUnlexer(Grammarinator):

    def __init__(self, *, max_depth=float('inf'), weights=None, cooldown=1.0):
        super(pet_storeUnlexer, self).__init__()
        self.unlexer = self
        self.max_depth = max_depth
        self.weights = weights or dict()
        self.cooldown = cooldown

    def EOF(self, *args, **kwargs):
        pass

    @depthcontrol
    def BASE_URL(self):
        current = self.create_node(UnlexerRule(name='BASE_URL'))
        current += self.create_node(UnlexerRule(src='https://petstore.swagger.io/v2'))
        return current
    BASE_URL.min_depth = 0

    @depthcontrol
    def INTEGER(self):
        current = self.create_node(UnlexerRule(name='INTEGER'))
        choice = self.choice([0 if [1, 0][i] > self.unlexer.max_depth else w * self.unlexer.weights.get(('alt_1', i), 1) for i, w in enumerate([1, 1])])
        self.unlexer.weights[('alt_1', choice)] = self.unlexer.weights.get(('alt_1', choice), 1) * self.unlexer.cooldown
        if choice == 0:
            current += self.unlexer.NON_ZERO_DIGIT()
            if self.unlexer.max_depth >= 1:
                for _ in self.zero_or_more():
                    current += self.unlexer.DIGIT()

        elif choice == 1:
            current += self.create_node(UnlexerRule(src='0'))
        return current
    INTEGER.min_depth = 0

    @depthcontrol
    def NON_ZERO_DIGIT(self):
        current = self.create_node(UnlexerRule(name='NON_ZERO_DIGIT'))
        current += self.create_node(UnlexerRule(src=self.char_from_list(charset_0)))
        return current
    NON_ZERO_DIGIT.min_depth = 0

    @depthcontrol
    def DIGIT(self):
        current = self.create_node(UnlexerRule(name='DIGIT'))
        current += self.create_node(UnlexerRule(src=self.char_from_list(charset_1)))
        return current
    DIGIT.min_depth = 0


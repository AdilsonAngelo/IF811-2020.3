# Generated by Grammarinator 19.3

from itertools import chain
from grammarinator.runtime import *

import pet_storeUnlexer


class pet_storeUnparser(Grammarinator):

    def __init__(self, unlexer):
        super(pet_storeUnparser, self).__init__()
        self.unlexer = unlexer
    @depthcontrol
    def valid_url(self):
        current = self.create_node(UnparserRule(name='valid_url'))
        current += self.unlexer.BASE_URL()
        current += self.endpoint()
        return current
    valid_url.min_depth = 3

    @depthcontrol
    def endpoint(self):
        current = self.create_node(UnparserRule(name='endpoint'))
        choice = self.choice([0 if [3, 2][i] > self.unlexer.max_depth else w * self.unlexer.weights.get(('alt_6', i), 1) for i, w in enumerate([1, 1])])
        self.unlexer.weights[('alt_6', choice)] = self.unlexer.weights.get(('alt_6', choice), 1) * self.unlexer.cooldown
        if choice == 0:
            current += self.pet_endpoint()
        elif choice == 1:
            current += self.store_endpoint()
        return current
    endpoint.min_depth = 2

    @depthcontrol
    def pet_endpoint(self):
        current = self.create_node(UnparserRule(name='pet_endpoint'))
        current += self.create_node(UnlexerRule(src='/pet'))
        current += self.pet_path()
        return current
    pet_endpoint.min_depth = 2

    @depthcontrol
    def store_endpoint(self):
        current = self.create_node(UnparserRule(name='store_endpoint'))
        current += self.create_node(UnlexerRule(src='/store'))
        current += self.store_path()
        return current
    store_endpoint.min_depth = 1

    @depthcontrol
    def pet_path(self):
        current = self.create_node(UnparserRule(name='pet_path'))
        current += self.create_node(UnlexerRule(src='/'))
        choice = self.choice([0 if [2, 1][i] > self.unlexer.max_depth else w * self.unlexer.weights.get(('alt_12', i), 1) for i, w in enumerate([1, 1])])
        self.unlexer.weights[('alt_12', choice)] = self.unlexer.weights.get(('alt_12', choice), 1) * self.unlexer.cooldown
        if choice == 0:
            current += self.pet_id()
        elif choice == 1:
            current += self.create_node(UnlexerRule(src='findByStatus?status='))
            current += self.pet_status()
        return current
    pet_path.min_depth = 1

    @depthcontrol
    def pet_id(self):
        current = self.create_node(UnparserRule(name='pet_id'))
        current += self.unlexer.INTEGER()
        return current
    pet_id.min_depth = 1

    @depthcontrol
    def pet_status(self):
        current = self.create_node(UnparserRule(name='pet_status'))
        choice = self.choice([0 if [0, 0, 0][i] > self.unlexer.max_depth else w * self.unlexer.weights.get(('alt_16', i), 1) for i, w in enumerate([1, 1, 1])])
        self.unlexer.weights[('alt_16', choice)] = self.unlexer.weights.get(('alt_16', choice), 1) * self.unlexer.cooldown
        if choice == 0:
            current += self.create_node(UnlexerRule(src='available'))
        elif choice == 1:
            current += self.create_node(UnlexerRule(src='pending'))
        elif choice == 2:
            current += self.create_node(UnlexerRule(src='sold'))
        return current
    pet_status.min_depth = 0

    @depthcontrol
    def store_path(self):
        current = self.create_node(UnparserRule(name='store_path'))
        current += self.create_node(UnlexerRule(src='/'))
        choice = self.choice([0 if [2, 0][i] > self.unlexer.max_depth else w * self.unlexer.weights.get(('alt_24', i), 1) for i, w in enumerate([1, 1])])
        self.unlexer.weights[('alt_24', choice)] = self.unlexer.weights.get(('alt_24', choice), 1) * self.unlexer.cooldown
        if choice == 0:
            current += self.create_node(UnlexerRule(src='order/'))
            current += self.order_id()
        elif choice == 1:
            current += self.create_node(UnlexerRule(src='inventory'))
        return current
    store_path.min_depth = 0

    @depthcontrol
    def order_id(self):
        current = self.create_node(UnparserRule(name='order_id'))
        current += self.unlexer.INTEGER()
        return current
    order_id.min_depth = 1

    default_rule = valid_url


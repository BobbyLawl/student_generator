import pandas as pd
import numpy as np
import random

'''
PART 2 - functions
'''

Adjectives = ['blue', 'large', 'grainy', 'substantial',
              'potent', 'thermonuclear']

Nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']


def random_phrase():
    adj = random.choice(Adjectives)
    noun = random.choice(Nouns)

    return adj + " " + noun


def random_float(min_val, max_val):
    return random.uniform(min_val, max_val)


def random_bowling_score():
    return random.randint(0, 300)


def silly_tuple():
    return (random_phrase(), round(random_float(1,5), 1), random_bowling_score())


def silly_tuple_list(num_tuples):
    tuple_list = []
    for item in range(num_tuples):
        tuple_list.append(silly_tuple())


'''
PART 3 functions
'''

test_df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


def null_count(df):
    return df.isnull().sum().sum()

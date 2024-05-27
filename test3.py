from eca import *
import random

root_content_path = 'test3_static'

def clip(lower, value, upper):
    return max(lower, min (value, upper))

@event('init')
def setup(ctx, e):
    ctx.count = 0
    fire('sample', {'previous': 0.0})

@event('sample')
@condition(lambda c, e: c.count < 100)
def generate_sample(ctx, e):
    ctx.count += 1

    sample = clip(-100, e.get('previous') + random.uniform(5.0, -5.0), 100)
    emit('sample', {
            'action':'add', 
            'value':sample
            })
    fire('sample', {'previous': sample}, delay=0.05)
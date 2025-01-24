import json
from pathlib import Path
from typing import Literal

import matplotlib.pyplot as plt
import pandas as pd


from seolpyo_mplchart import Chart


_name = {'samsung', 'apple'}
def sample(name: Literal['samsung', 'apple']='samsung'):
    if name not in _name:
        print('name should be either samsung or apple.')
        return
    file = Path(__file__).parent / f'data/{name}.txt'
    with open(file, 'r', encoding='utf-8') as txt:
        data = json.load(txt)
    data = data
    df = pd.DataFrame(data)

    c = Chart()
    if name == 'apple':
        c.unit_price = '$'
        c.unit_volume = 'vol'
        c.digit_price = 3
        c.label_ma = 'ma{}'
        c.candleformat = '{}\n\nclose:   {}\nrate:    {}\ncompare: {}\nopen:    {}({})\nhigh:    {}({})\nlow:     {}({})\nvolume:  {}({})'
        c.volumeformat = '{}\n\nvolume:      {}\nvolume rate: {}'
    c.set_data(df)
    plt.show()

    return


if __name__ == '__main__':
    sample('apple')
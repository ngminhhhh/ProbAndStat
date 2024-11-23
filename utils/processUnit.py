import pandas as pd

def split_resolution(data, resolution):
    '''
        data: pandas data need to split 'resolution type'
    '''
    data[[resolution + '_width', resolution + '_height']] = data[resolution].str.extract(r'(\d+)\s*x\s*(\d+)', expand=True)

    data[resolution + '_width'] = pd.to_numeric(data[resolution + '_width'], errors='coerce')
    data[resolution + '_height'] = pd.to_numeric(data[resolution + '_height'], errors='coerce')

    index = data.columns.get_loc(resolution)
     
    data.insert(index, resolution + '_width', data.pop(resolution + '_width'))
    data.insert(index + 1, resolution + '_height', data.pop(resolution + '_height'))

    data.pop(resolution)


def erase_unit(data, column):
    '''
        data: pandas data need to delete unit in column
    '''
    data[column] = data[column].replace(r'[^\d.]','',regex=True)
    data[column] = pd.to_numeric(data[column], errors='coerce')


def split_cores(data, column, name):
    '''
        data: split cache to 2 column, cache_per_core, cores
    '''
    data[[name + '_Per_Core', name + '_Cores']] = data[column].str.extract(r'(\d+)\s*(?:KB)?\s*(?:\(\s*x\s*(\d+)\s*\))?', expand=True)
    data[name + '_Per_Core'] = pd.to_numeric(data[name + '_Per_Core'], errors='coerce')
    data[name + '_Cores'] = data[name + '_Cores'].where(data[name + '_Cores'].notna(), other=1).where(data[name + '_Per_Core'].notna())

    index = data.columns.get_loc(column)
     
    data.insert(index, name + '_Per_Core', data.pop(name + '_Per_Core'))
    data.insert(index + 1, name + '_Cores', data.pop(name + '_Cores'))

    data.pop(column)


def split_PSU(data, column):
    data[[column + '_Watt', column + '_Amps']] = data[column].str.extract(r'(\d+)\s*Watt(?:\s*&\s*(\d+)\s*Amps)?', expand=True)

    data[column + '_Watt'] = pd.to_numeric(data[column + '_Watt'], errors='coerce')
    data[column + '_Amps'] = pd.to_numeric(data[column + '_Amps'], errors='coerce')

    index = data.columns.get_loc(column)
     
    data.insert(index, column + '_Watt', data.pop(column + '_Watt'))
    data.insert(index + 1, column + '_Amps', data.pop(column + '_Amps'))

    data.pop(column)


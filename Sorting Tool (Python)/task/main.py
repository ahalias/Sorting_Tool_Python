import math
import argparse
from collections import Counter
import re

request = []
lines = []

parser = argparse.ArgumentParser()
parser.add_argument('-dataType', const="error", nargs='?')
parser.add_argument('-sortingType', const="error", nargs='?')
parser.add_argument('-inputFile')
parser.add_argument('-outputFile')
args, unknown = parser.parse_known_args()

if args.dataType == 'error':
    print('No data type defined!')
elif args.sortingType == 'error':
    print('No sorting type defined!')
    exit()
elif unknown:
    [print(f'"-{x}" is not a valid parameter. It will be skipped.') for x in unknown]

if args.inputFile:
    file = args.inputFile
    with open(file, 'r') as f:
        for string in f:
            line = string.replace('\n', '')
            data = line.split()
            lines.append(data)
            request += data


def nsort_line():
    sorted_data = sorted(x for x in lines)
    if args.outputFile:
        file = args.outputFile
        with open(file, 'w') as f:
            print(f'Total lines: {len(lines)}.\nSorted data: ', file=f)
            print(*sorted_data, sep='\n', file=f)
    else:
        print(f'Total lines: {len(lines)}.\nSorted data: ')
        print(*sorted_data, sep='\n')


def process_nsort(request, items):
    sorted_data = sorted(int(x) for x in request)
    sorted_data_str = ' '.join(str(x) for x in sorted_data)
    if args.outputFile:
        file = args.outputFile
        with open(file, 'w') as f:
            print(f'Total {items}: {len(request)}.\nSorted data: {sorted_data_str}', file=f)
    else:
        print(f'Total {items}: {len(request)}.\nSorted data: {sorted_data_str}')


def process_bcsorting(items, data):
    count_items = Counter(items)
    res1 = sorted(count_items.items(), key=lambda x: x[0], reverse=False)
    res = sorted(res1, key=lambda x: x[1], reverse=False)
    print_bcdata(items, res, data)


def print_bcdata(request, res, items):
    if args.outputFile:
        file = args.outputFile
        with open(file, 'w') as f:
            print(f'Total {items}: {len(request)}.', file=f)
            [print(f'{x}: {y} times, {math.floor(100 * y / len(request))}%', file=f) for x, y in res]
    else:
        print(f'Total {items}: {len(request)}.')
        [print(f'{x}: {y} times, {math.floor(100 * y / len(request))}%') for x, y in res]


while True:
    try:
        line = input()
        lines.append(line)
        data = line.split()
        request += data
    except EOFError:
        break


if args.dataType == 'long':
    [print(f'"{x}" is not a long. It will be skipped.') for x in request if x.isalpha()]
    request = [int(x) for x in request if re.search(r'[-?\d+]$', x)]
    if args.sortingType == 'byCount':
        process_bcsorting(request, 'numbers')
    else:
        process_nsort(request, 'numbers')
if args.dataType == 'word':
    if args.sortingType == 'byCount':
        process_bcsorting(request, 'words')
    else:
        process_nsort(request, 'words')
if args.dataType == 'line':
    if args.sortingType == 'byCount':
        process_bcsorting(lines, 'lines')
    else:
        nsort_line()
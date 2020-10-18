import os
import time
import sys


def remove_lines(f_in):
    with open(f_in, 'r', encoding='utf-8') as fin,\
            open("scrapped.txt", 'w', encoding='utf-8') as fout:
        for lines in fin:
            if lines.strip():
                fout.write(lines)


def generate(f_out):
    rin = open("scrapped.txt", 'r', encoding='utf-8', errors='ignore')
    rout = open(f_out, 'w', encoding='utf-8', errors='ignore')

    for line in rin:
        if "BEGIN:" in line:
            rout.write(line.replace("\n", " ").replace("  ", " "))
            try:
                while "END:" not in line:
                    line = next(rin)
                    rout.write(line.replace("\n", " ").replace("  ", " "))
            except StopIteration:
                pass
            rout.write("\n" * 2)

    rin.close()
    rout.close()


if len(sys.argv) <= 2 or len(sys.argv) > 3:
    print("Usage: \n\tpTest.py <input_file.txt> <output_file.txt> \n\tExit!")
else:
    file_in = sys.argv[1]
    file_out = sys.argv[2]

    remove_lines(file_in)
    time.sleep(1)
    generate(file_out)

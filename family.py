from logic_program import get_outer_arguments
import re
def read(filename, asstring=False):
    """
    Reads filename and returns either a list (asstring = True) or a string.
    """
    if asstring:
        lines = ''
    else:
        lines = []
    try:
        file = open(filename, 'r')
        for line in file:
            nline = re.sub(r'(?<!not)\s', '', line)
            if asstring:
                lines += nline + '\n'
            else:
                lines.append(nline)
        file.close()
    except IOError:
        print("The file does not exist")
    return lines


def main():
    filetext = read("/Users/kritisapra/Desktop/Imperial/Fourth_Year/prob_aspal/experiments/family.data")
    pfs = []
    all_names = set()
    background = ''
    for line in filetext:
        print("line: {}".format(line))
        if line.startswith("mode"):
            continue
        elif line.startswith("base"):
            continue
        elif line.startswith("0."):
            splits = line.split("::")
            pf = "pf(" + splits[1][:-1] + ", " + splits[0] + "). \n"
            pfs.append(pf)
            names = get_outer_arguments(splits[1])
            for n in names:
                all_names.add(n)
        elif line.startswith("mother"):
            names = get_outer_arguments(line)
            for n in names:
                all_names.add(n)
            background = background + line + '\n'
        elif line.startswith("parent"):
            names = get_outer_arguments(line)
            for n in names:
                all_names.add(n)
            background = background + line + '\n'
        elif line.startswith("female"):
            names = get_outer_arguments(line)
            for n in names:
                all_names.add(n)
            background = background + line + '\n'
        elif line.startswith("male"):
            names = get_outer_arguments(line)
            for n in names:
                all_names.add(n)
            background = background + line + '\n'
        elif line.startswith("male_ancestor"):
            names = get_outer_arguments(line)
            for n in names:
                all_names.add(n)
            # all_names.add(names)
            background = background + line + '\n'
        elif line.startswith("female_ancestor"):
            names = get_outer_arguments(line)
            for n in names:
                all_names.add(n)
            background = background + line + '\n'
        elif line.startswith("grandmother"):
            names = get_outer_arguments(line)
            for n in names:
                all_names.add(n)
            background = background + line + '\n'
        elif not line.startswith("%"):
            background = background + line + '\n'
    print(len(all_names))

    f = open("/Users/kritisapra/Desktop/Imperial/Fourth_Year/prob_aspal/experiments/family.lp", "w")

    for pf in pfs:
        background += pf

    for n in all_names:
        background += "person({}).\n".format(n)

    f.write(background)


if __name__ == "__main__":
    main()

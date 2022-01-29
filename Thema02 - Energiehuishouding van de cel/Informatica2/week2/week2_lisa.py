#!usr/bin/env python3"""program reads fasta input and gives information about file"""__author__ = "Lisa Hu"import sysdef reading_file(file_):    """    reads file    :param file_: opened file    :return: header and sequence that's in the file    """    seq = ""    for line in file_:        if line.startswith(">"):            header = line        else:            seq += line.strip()    return header, seqdef dna_check(seq):    """    checking if the file contains DNA or amino acids    :param seq: sequence of the file    :return: boolean True/False    """    dna_nuc = "ACGT"    if dna_nuc not in seq:        print("file contains amino acids" + "\n")        return False    else:        return Truedef making_dict(seq):    """    making dictionary that counts the occurrence of each letter in sequence    :param seq: sequence from file    :return: filled dictionary    """    seq_dict = {}    for char in seq:        if char not in seq_dict:            seq_dict[char] = 1        else:            seq_dict[char] += 1    return seq_dictdef calc_comp(seq_dict):    """    calculate the percentage of the content    :param seq_dict: dictionary of sequence    :return: dictionary with percentage for each key    """    comp_dict = {}    for key in seq_dict:        perc = seq_dict[key]/sum(seq_dict.values()) * 100        if key not in comp_dict:            comp_dict[key] = perc    return comp_dictdef calc_gc(seq_dict):    """    calculate the GC percentage of the sequence    :param seq_dict: dictionary of sequence    :return: GC percentage    """    gc_perc = (seq_dict["G"] + seq_dict["C"]) / sum(seq_dict.values()) * 100    return gc_percdef main(argv):    """    main function    :param argv: input command in terminal    """    files = argv[1:]    for file_ in files:  # loop through each file name        opened = open(file_, "r")        header, seq = reading_file(opened)        seq_dict = making_dict(seq)        print(header)        print(seq_dict)        if dna_check(seq):  # only executes if file contains DNA            print("file contains nucleotides" + "\n")            comp_dict = calc_comp(seq_dict)            for key in comp_dict:                print(key, ":", comp_dict[key], "%")            gc = calc_gc(seq_dict)            print("GC percentage: ", gc, "%" + "\n")        opened.close()# running mainif __name__ == "__main__":    sys.exit(main(sys.argv))
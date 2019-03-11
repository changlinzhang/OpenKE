def preprocess(data_part):
    data_path = "benchmarks/GDELT/" + data_part + ".txt"
    write_path = "benchmarks/GDELT/" + data_part + "2id.txt"
    fw = open(write_path, "w")
    with open(data_path, "r") as fp:
        for i, line in enumerate(fp):
            if i == 0:  # stat for first line
                info = line.strip().split("\t")
                fw.write("%ld\n" % (int(info[0])))
                continue
            info = line.strip().split("\t")
            fw.write("%ld %ld %ld\n" % (int(info[0]), int(info[2]), int(info[1])))
    fw.close()


if __name__ == "__main__":
    preprocess("train")
    preprocess("test")
    preprocess("valid")

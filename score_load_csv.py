with open("scores.csv", "r") as f:
    next(f)
    print("CSVから読み込んだデータ:")
    for line in f:
        split_line = line.strip().split(",")
        print(f"{split_line[0]}さん: 合計{split_line[1]}点、平均{split_line[2]}点")
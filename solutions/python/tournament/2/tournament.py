"""tally"""
def tally(rows):
    """tally"""
    def add_entry_if_new(results_dict, key):
        if key not in results_dict:
            results_dict[key] = {"played":0,"won":0,"drawn":0,"lost":0,"points":0}

    def record_win(results_dict, key):
        results_dict[key]["played"] += 1
        results_dict[key]["won"] += 1
        results_dict[key]["points"] += 3

    def record_draw(results_dict, key):
        results_dict[key]["played"] += 1
        results_dict[key]["drawn"] += 1
        results_dict[key]["points"] += 1

    def record_loss(results_dict, key):
        results_dict[key]["played"] += 1
        results_dict[key]["lost"] += 1

    results = {
        "Team                          ": {"played":"MP","won":"W","drawn":"D","lost":"L","points":"P"} #table header row
    }

    for row in rows:
        record = row.split(";")
        add_entry_if_new(results, record[0])
        add_entry_if_new(results, record[1])
        if record[2] == "win":
            record_win(results, record[0])
            record_loss(results, record[1])
        elif record[2] == "draw":
            record_draw(results, record[0])
            record_draw(results, record[1])
        elif record[2] == "loss":
            record_loss(results, record[0])
            record_win(results, record[1])

    col_one_width = max(len(k) for k in results.keys())
    col_width = 2
    separator = " | "
    result = []
    header = list(results.items())[0]
    teams = sorted(list(results.items())[1:], key=lambda x: (-x[1]["points"], x[0]))
    for team, stats in [header] + teams:
        temp = [team.ljust(col_one_width)]
        for value in stats.values():
            temp.append(str(value).rjust(col_width))
        result.append(separator.join(temp))
        
    return result
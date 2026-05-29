"""tally"""
def tally(rows):
    """tally"""
    def add_entry_if_new(results_dict, key):
        if key not in results_dict:
            results_dict[key] = {"played":0,"won":0,"drawn":0,"lost":0,"points":0}

    def record_result(results_dict, key, won=0, drawn=0, lost=0):
        results_dict[key]["played"] += 1
        results_dict[key]["won"] += won
        results_dict[key]["drawn"] += drawn
        results_dict[key]["lost"] += lost
        results_dict[key]["points"] += won * 3 + drawn

    results = {
        "Team                          ": {"played":"MP","won":"W","drawn":"D","lost":"L","points":"P"} #table header row
    }

    for row in rows:
        record = row.split(";")
        add_entry_if_new(results, record[0])
        add_entry_if_new(results, record[1])
        record_result(results, record[0], won=record[2] == "win", drawn=record[2] == "draw", lost=record[2] == "loss")
        record_result(results, record[1], won=record[2] == "loss", drawn=record[2] == "draw", lost=record[2] == "win")

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
import re 


def parse_log_line(line: str):
    parts = line.split()
    logs = {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": " ".join(parts[3:])
    }
    return logs






def load_logs(file_path: str):
    logs = [] 
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    logs.append(parse_log_line(line.strip()))
    except FileNotFoundError:
        print("Такого файлу не існує")
    return logs 

    
    
    





def filter_logs_by_level(logs: list, level: str):
    Level = level.upper()
    return [log for log in logs if log['level'] == Level]

    





def count_logs_by_level(logs: list):
    counts = {}
    for log in logs:
        level = log['level']
        if level not in counts:
            counts[level] = 1
        else:
            counts[level] += 1
    return counts
        




def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level: <17}| {count}")


if __name__ == "__main__":
    file_path = "file_path.txt" 
    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)
import json

class logAnalyzer:
    def read_logs(self):
        with open("app.log", "r") as log_file:
            logs = log_file.readlines()
        return logs
    
    def analyze_logs(self, log_count, data):
        
        for line in data:
            if "ERROR" in line:
                log_count.update({"ERROR": log_count["ERROR"] + 1})
            elif "INFO" in line:
                log_count.update({"INFO": log_count["INFO"] + 1})
            elif "WARNING" in line:
                log_count.update({"WARNING": log_count["WARNING"] + 1})
            else :
                pass
        return log_count
    
    def write_json(self, log_count):
        with open("log_summary.json", "w+") as json_file:
            json.dump(log_count, json_file, indent=4)

def main():
    log_count = {
        "ERROR": 0,
        "INFO": 0,
        "WARNING": 0
    }
    
    analyzer = logAnalyzer()
    data = analyzer.read_logs()
    log_count = analyzer.analyze_logs(log_count, data)
    analyzer.write_json(log_count)

if __name__ == "__main__":
    main()
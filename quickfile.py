import csv
import json

def load_binary(filename):
    with open(filename,"rb") as file:
        data = file.read()
    return data

def save_binary(filename, data):
    with open(filename,"wb") as file:
        file.truncate(0)
        file.write(data)

def load_string(filename):
    with open(filename,"r",encoding="utf-8") as file:
        data = file.read()
    return data

def save_string(filename, data):
    with open(filename,"w",encoding="utf-8") as file:
        file.truncate(0)
        file.write(data)

def load_csv(filename, **fmtparams):
    output = []
    with open(filename,"r",encoding="utf-8") as file:
        reader = csv.reader(file,**fmtparams)
        for row in reader:
            output.append(row)
    return output

def save_csv(filename, data, **fmtparams):
    with open(filename,"w",encoding="utf-8") as file:
        file.truncate(0)
        writer = csv.writer(file,**fmtparams)
        writer.writerows(data)

def load_json(filename):
    raw = load_string(filename)
    data = json.loads(raw)
    return data

def save_json(filename, data, compact = True):
    if compact:
        raw = json.dumps(data,separators=(",",":"),ensure_ascii=False)
    else:
        raw = json.dumps(data,ensure_ascii=False)
    save_string(filename,raw)

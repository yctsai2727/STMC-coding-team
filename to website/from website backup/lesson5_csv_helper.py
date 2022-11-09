def cast(cast_type,val,fallback_val = -1):
    try:
        return cast_type(val)
    except:
        return fallback_val

def format_line(line,sep=','):
    cast_type = [int,int,int,float,str]
    itm = line.strip().split(sep)
    return [cast(type,it) for it,type in zip(itm,cast_type)]


def read_hko_csv(path):
    with open(path,'r') as csv:
        lines = csv.readlines() # Not a good way to read large file
        lines = lines[3:-3] # Dirty way to trim off header and footer
        data = [format_line(line) for line in lines]
        return data

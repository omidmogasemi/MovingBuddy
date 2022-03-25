import json

def rows_to_dict(rows): 
    res = [] 

    for row in rows: 
        res.append(row_to_dict(row)) 

    return json.dumps(res, default=str) 

def row_to_dict(row): 
    res = {} 
    cols = list(row.keys()) 
    
    for i, j in enumerate(row): 
        res[cols[i]] = j 
    
    return res 

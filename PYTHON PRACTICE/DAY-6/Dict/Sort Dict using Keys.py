d1 = {'CSK':'1', 'MI':'2', 'RR':'3','RCB':'4','LSG':'5','GT':'6'}
sort_keys = sorted(d1.keys())
sort_dict = {key:dict[key] for key in sort_keys}
print(sort_dict)
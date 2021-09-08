import yaml

target_dict = dict()
last_element = target_dict
with open("data.txt") as source:
    for line in source.readlines():
        for level in line.split('.'):
            if ":" in level:
                level, value = level.split(":")
                value = value.strip().rstrip('"').lstrip('"')
                last_element[level] = value
            else:
                if level not in last_element:
                    last_element[level] = dict()
            last_element = last_element[level]
        last_element = target_dict

with open('data.yml', 'w') as outfile:
    yaml.dump(target_dict, outfile, default_flow_style=False)
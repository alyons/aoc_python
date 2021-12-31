def run_program(instructions: list[str], input: list[int], variables: dict[str, int] = { 'w': 0, 'x': 0, 'y': 0, 'z': 0 }, print_debug: bool = False):
    index = 0

    for inst in instructions:
        match inst.split(' '):
            case ['inp', key]:
                variables[key] = input[index]
                index += 1
            case ['add', key, other]:
                variables[key] += variables[other] if other in variables else int(other)
            case ['mul', key, other]:
                variables[key] *= variables[other] if other in variables else int(other)
            case ['mod', key, other]:
                variables[key] %= variables[other] if other in variables else int(other)
            case ['eql', key, other]:
                var = variables[other] if other in variables else int(other)
                variables[key] = int(variables[key] == var)
            case ['div', key, other]:
                var = variables[other] if other in variables else int(other)
                variables[key] = int(variables[key] / var)
    
        if print_debug: print(f"{inst:8} {variables['w']} {variables['x']} {variables['y']} {variables['z']}")

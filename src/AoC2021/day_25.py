from reprint import output

def next_space_east(position: tuple[int, int], x_max) -> tuple[int, int]:
    return (position[0] + 1 if position[0] < x_max else 0, position[1])


def next_space_south(position: tuple[int, int], y_max) -> tuple[int, int]:
    return (position[0], position[1] + 1 if position[1] < y_max else 0)


def landing_step(east, south, x_max, y_max) -> int:
    steps = 0

    moves_found = True

    with output('dict') as output_dict:
        while moves_found:
            output_dict['Current Step'] = steps
            moves_found = False
            
            east_to_move = [e for e in east if not next_space_east(e, x_max) in east and not next_space_east(e, x_max) in south]
            moves_found |= bool(east_to_move)
            output_dict['East Moves'] = len(east_to_move)

            for e in east_to_move:
                n = next_space_east(e, x_max)
                i = next(i for i, a in enumerate(east) if a == e)
                east[i] = n

            south_to_move = [s for s in south if not next_space_south(s, y_max) in east and not next_space_south(s, y_max) in south]
            moves_found |= bool(south_to_move)
            output_dict['South Moves'] = len(south_to_move)

            for s in south_to_move:
                n = next_space_south(s, y_max)
                i = next(i for i, a in enumerate(south) if a == s)
                south[i] = n
            
            steps += 1

    return steps

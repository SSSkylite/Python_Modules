# Couldn't really be bothered to do global variables or funky things with
# classes so this might not work in some weirdly scoped systems.

def debug(locals: dict, var_string: str, num: int = 0) -> None:
    # Example use: debug(locals(), "[var1,var2]")
    # Gathers debug data to be passed onto debug_table
    # Seperate data streams should be designated different nums
    vars = {var.strip(): locals[var.strip()]
            for var in var_string.strip('][').split(',')}
    try:
        debug.rows[num].append([locals[var] for var in vars])

        debug.lens[num] = [max(len(str(locals[var])), debug.lens[num][i], 6)
                           for i, var in enumerate(vars)]
    except AttributeError:
        # Runs on first debug call
        debug.rows = []
        debug.header = []
        debug.lens = []
        debug(locals, var_string, num)
    except IndexError:
        # Runs on first debug call for each num
        debug.rows.append([])
        debug.header.append([var for var in vars])
        debug.lens.append([len(var) for var in vars])
        debug(locals, var_string, num)


def debug_table(num: int = 0) -> list:
    # Tabulates debug data
    try:
        formatting = '\t'.join(["{:>%i}" % i for i in debug.lens[num]])
        print(formatting)
        sep = ["-"*i for i in debug.lens[num]]
        return [formatting.format(*i) for i in [debug.header[num], sep, *debug.rows[num]]]
    except AttributeError:
        print(f"No debug set for num {num}")

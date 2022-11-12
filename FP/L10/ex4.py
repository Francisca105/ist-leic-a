def cria_time_stamp(data, relogio):
    return {'dt': data, 'rel': relogio}


def data(ts):
    return ts[0]


def relógio(ts):
    return ts[1]


def eh_time_stamp(arg):
    return type(arg) == tuple and len(arg) == 2 and 'dt' in arg and 'rel' in arg


def mesmo_time_stamp(ts1, ts2):
    if not eh_time_stamp(ts1) or not eh_time_stamp(ts2):
        raise ValueError("Argumentos inválidos")

    return len(ts1) == len(ts2) and ts1[0] == ts2[0] and ts1[1] == ts2[1] and type(ts1) == type(ts2)
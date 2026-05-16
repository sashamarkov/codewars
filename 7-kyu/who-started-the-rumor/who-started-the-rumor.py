def rumor_starter(record):
    told = {p for v in record.values() for p in v}
    return sorted(record.keys() - told)
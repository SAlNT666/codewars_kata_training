# https://www.codewars.com/kata/52742f58faf5485cae000b9a

def format_duration(seconds):
    if not seconds: return 'now'

    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    years, days = divmod(days, 365)

    bs, bm, bh, bd, by = bool(seconds), bool(minutes), bool(hours), bool(days), bool(years)

    return f"{(str(years) + ' year'+'s' * (years > 1) + (', ', ' and ')[sum((bs, bm, bh, bd)) == 1] * any((bs, bm, bh, bd))) * by}" \
           f"{(str(days) + ' day'+'s' * (days > 1) + (', ', ' and ')[sum((bs, bm, bh)) == 1] * any((bs, bm, bh))) * bd}" \
           f"{(str(hours) + ' hour'+'s' * (hours > 1) + (', ', ' and ')[sum((bs, bm)) == 1] * any((bs, bm))) * bh}" \
           f"{(str(minutes) + ' minute'+'s' * (minutes > 1) + (', ', ' and ')[bs] * bs) * bm}" \
           f"{(str(seconds) + ' second'+'s' * (seconds > 1)) * bs}"


print(format_duration(367457300))

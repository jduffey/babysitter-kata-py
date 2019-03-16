'''
The babysitter 
- starts no earlier than 5:00PM
- leaves no later than 4:00AM
- gets paid $12/hour from start-time to bedtime
- gets paid $8/hour from bedtime to midnight
- gets paid $16/hour from midnight to end of job
- gets paid for full hours (no fractional hours)
'''

PAYRATE_REGULAR = 12
PAYRATE_BEDTIME = 8
PAYRATE_MIDNIGHT = 16

def paycalc(start_time, end_time, bed_time):
    if start_time == 12:
        end_time = end_time + 12
        return PAYRATE_MIDNIGHT * (end_time - start_time)

    if bed_time < end_time:
        return (end_time - bed_time) * PAYRATE_BEDTIME + \
        (bed_time - start_time) * PAYRATE_REGULAR

    if bed_time == start_time:
        return (end_time - start_time) * PAYRATE_BEDTIME

    return (end_time - start_time) * PAYRATE_REGULAR
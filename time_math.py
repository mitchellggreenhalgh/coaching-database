class time_addition:

    def add_time(str_list:list or tuple):
        minutes = sum([int(time[0]) for time in str_list])
        seconds = sum([float(sec[2:]) for sec in str_list])

        minutes += int(seconds // 60)
        remaining_seconds = seconds % 60

        return f'{minutes}:{remaining_seconds:02}'
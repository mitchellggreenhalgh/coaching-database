class time_addition:

    def add_time(str_list:list or tuple):
        minutes = sum([int(time[0]) for time in str_list])
        seconds = sum([int(sec[2:4]) for sec in str_list])
        partial_seconds = sum([int(hundredth[-2:]) for hundredth in str_list])

        minutes += seconds // 60
        remaining_seconds = seconds % 60
        seconds += partial_seconds // 100
        remaining_partial_seconds = partial_seconds % 100

        return f'{minutes}:{remaining_seconds:02}.{remaining_partial_seconds:02}'
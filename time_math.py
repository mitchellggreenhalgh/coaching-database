class time_addition:

    def add_time(str_list:list or tuple):
        minutes = sum([int(time[0]) for time in str_list])
        seconds = sum([float(sec[2:]) for sec in str_list])

        minutes += int(seconds // 60)
        remaining_seconds = round(seconds % 60, 2)

        return f"{minutes}:{int(str(remaining_seconds).split('.')[0]):02}.{str(remaining_seconds).split('.')[1]}"
from datetime import datetime

class split_converter:
    def split_to_lap(splits:list):
        ''' Take an input list of all the race splits and return list of laps. Also return extracted total time. '''

        splits, total_time = split_converter.fix_empty_splits(splits)
        conversion = [split_converter.interpret_input(y) - split_converter.interpret_input(x) for x,y in zip(splits,splits[1:])]
        formatted_conversion = [str(x)[3:-4] if len(str(x)) > 7 else str(x)[3:] + '.00' for x in conversion]
        appended_conversion = [str(split_converter.interpret_input(splits[0])).split(' ')[1][1:][3:-4]] + formatted_conversion
        replaced_zeroes = ['' if i == '0:00.00' else i for i in appended_conversion]

        return replaced_zeroes, total_time

    def interpret_input(input:str):
        ''' Convert string to useable datetime value. '''

        time_val = datetime.strptime(input, '%M:%S.%f')
        return time_val
    
    def fix_empty_splits(raw_input:list):
        ''' When not all 8 splits are taken (e.g. for an 800m), replace all the empty strings with useable splits that don't affect the lap calculations. Also extract the total time from the last split. '''

        if all(bool(i) for i in raw_input):
            last_split = [raw_input[-1]]
            return raw_input, last_split
        
        else:
            without_empty_strings = [i for i in raw_input if i != '']
            last_split = [without_empty_strings[-1]] 
            replacements = last_split * (8 - len(without_empty_strings))
            new_list = without_empty_strings + replacements

            return new_list, last_split
        
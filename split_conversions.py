from datetime import datetime

class split_converter:
    def split_to_lap(splits:list):
        ''' Take an input list of all the race splits and return list of laps. Also return extracted total time. '''

        splits, total_time = split_converter.fix_empty_splits(splits)
        conversion = [split_converter.interpret_input(y) - split_converter.interpret_input(x) for x,y in zip(splits,splits[1:])]
        formatted_conversion = [str(x)[3:-4] if len(str(x)) > 7 else str(x)[3:] + '.00' for x in conversion]
        conversion_no_zeroes = ['' if i == '0:00.00' else i for i in formatted_conversion]
        first_split = [splits[0]] 
        final_product = first_split + conversion_no_zeroes

        return final_product, total_time

    def interpret_input(input:str):
        ''' Convert string to useable datetime value. '''

        time_val = datetime.strptime(input, '%M:%S.%f')
        return time_val
    
    def fix_empty_splits(raw_input:list):
        ''' When not all 8 splits are taken (e.g. for an 800m), replace all the empty strings with useable splits that don't affect the lap calculations. Also extract the total time from the last split. '''

        if all(bool(i) for i in raw_input):
            if len(raw_input) == 1:
                last_split = [raw_input]
            else:
                last_split = [raw_input[-1]]

            return raw_input, last_split
        
        else:
            without_empty_strings = [i for i in raw_input if i]
            last_split = [without_empty_strings[-1]] 
            replacements = last_split * (8 - len(without_empty_strings))  # can't be an empty string yet because i haz to do maths
            new_list = without_empty_strings + replacements

            return new_list, last_split
        
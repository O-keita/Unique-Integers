"""
    I will first declare the file path
    which will contain the part to the sample inputs
    for this case we will use sample_01.txt, but
    it can be change to any desirable file as long as
    the file name is spell properly
"""
path_input = 'Sample_Inputs/sample_01.txt'


with open(path_input, 'r') as file:
    """
        removing the white spaces at the beginning
        and end of each line
    """
    for line in file:
            
            """White Spaces at the beginning"""
            while line and (line[0] == ' '
                             or line[0] == '\t' or line[0] == '\n'):
                line = line[1:]
               
                
            """white spaces at the end"""
            while line and (line[-1] == ' '
                             or line[-1] == '\t' or line[-1] == '\n'):
                line = line[:-1]

            "Converting all numbers to integers ready to sort them"
            try:
                 num = int(line)
            except ValueError:
                 continue
            
            
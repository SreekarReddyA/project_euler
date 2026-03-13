def longest_collatz_sequence(n):
    current_number = 2
    longest_sequence = 0
    longest_sequence_number = 2
    length_records = {}
    while current_number < n:
        cn = current_number
        sequence_length = 1
        while cn != 1:
            if cn in length_records.keys():
                sequence_length += length_records[cn]
                break
            if cn % 2 == 0:
                cn = cn /2
            else:
                cn = 3 * cn + 1
            sequence_length += 1
        
        length_records[current_number] = sequence_length
        if sequence_length > longest_sequence:
            longest_sequence = sequence_length
            longest_sequence_number = current_number
        
        current_number += 1
    
    return longest_sequence_number

print(longest_collatz_sequence(1000000))
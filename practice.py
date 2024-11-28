#1. Two Sum

def twoSum(nums, target):
        #make dictionary to store enumerate object references
        number_map = {}
        #for loop that references enumerate object, iterates index of our number value and adds to dict(number_map),
        for i, num in enumerate(nums):
            #calculates difference of current index value and target (target is presumably larger since it is a sum)
            diff = target - num
            #if our difference is written in our number map (last step) then return that difference's index,
            #and the current index we are comparing using
            if diff in number_map:
                return number_map[diff], i
            #then add the current number and its index to the dictionary
            number_map[num] = i
        #if no two add up to the target
        return None

nums=[2,7,11,15]
target=9
print(twoSum(nums,target))

#2. Text-justification

def brute_force_justify(words, maxWidth):
    result = []  # Final justified lines
    line = []  # Current line
    line_length = 0  # Current line's total word length (excluding spaces)

    # Step 1: Generate possible lines
    for word in words:
        if line_length + len(line) + len(word) > maxWidth:  # If adding `word` exceeds width
            result.append(line)  # Save the current line
            line = []  # Reset the line
            line_length = 0
        line.append(word)
        line_length += len(word)
    result.append(line)  # Add the last line

    # Step 2: Justify each line
    justified_result = []
    for i in range(len(result)):
        line = result[i]
        if i == len(result) - 1 or len(line) == 1:  # Last line or single-word line
            justified_result.append(" ".join(line).ljust(maxWidth))
        else:
            spaces = maxWidth - sum(len(word) for word in line)  # Total spaces to distribute
            gaps = len(line) - 1  # Number of gaps between words
            # Distribute spaces evenly
            if gaps > 0:
                space_per_gap = spaces // gaps
                extra_spaces = spaces % gaps
                justified_line = ""
                for j in range(gaps):
                    justified_line += line[j] + " " * (space_per_gap + (1 if j < extra_spaces else 0))
                justified_line += line[-1]  # Add the last word
                justified_result.append(justified_line)
            else:
                # Single word case
                justified_result.append(line[0].ljust(maxWidth))
    return justified_result

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth=16
print("\n".join(brute_force_justify(words,maxWidth)))

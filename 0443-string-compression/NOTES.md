`Old solution`
`It doesn't work very well`
​
count = 1
holder = 0
end = 1
cut = len(chars)
for i in range(len(chars)):
if i+1 <len(chars) and chars[i] == chars[i+1]:
count+=1
else:
chars[holder] = chars[i]
if count > 1:
count_str = list(str(count))
start = holder+1
end = holder+1+ len(count_str)
chars[start:end]= count_str
holder = end
else:
holder = end+1
count = 1
print(chars)
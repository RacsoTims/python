# lst = [n for n in range(50)]

# snip = 0

# for number in lst:
#     if (number + 1) % 10 == 0:
#         lst[snip] = lst[10*snip:number+1]
#         snip += 1
# lst = lst[0:len(lst)//10]
# print(lst)

start = '12'
games = 0

def game(start) -> str:
    
    end = ''
    
    for i in range(len(start)):
        
        counter = 1
        
        if i == 0:
            while start[i+counter] == start[i]:
                counter += 1
            else:
                end += f"{counter}{start[i]}"
        elif i == len(start) - 1:
            if start[i-1] == start[i]:
                continue
            else:
                end += f"{counter}{start[i]}"
        else:
            if start[i-1] == start[i]:
                continue
            else:
                while start[i+counter] == start[i]:
                    if i + counter == len(start) - 1:
                        counter += 1
                        end += f"{counter}{start[i]}"
                        break
                    else:
                        counter += 1
                else:
                    end += f"{counter}{start[i]}"
    return end

while games < 10:
    start = game(start)
    games += 1
    print(len(start), start)

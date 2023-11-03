def count_plyr(plyr_scr, pil_health):
    clear_count = 0
    
    for score in plyr_scr:
        can_break_pil_1 = pil_health[0] % score == 0 
        can_break_pil_2 = pil_health[1] % score == 0
        
        if can_break_pil_1 or can_break_pil_2:
            clear_count += 1
            
    return clear_count
    

num_plyr = int(input())
plyr_scr = list(map(int, input().split()))
pil_health = list(map(int, input().split()))

cleared_plyr = count_plyr(plyr_scr, pil_health)
print(cleared_plyr)
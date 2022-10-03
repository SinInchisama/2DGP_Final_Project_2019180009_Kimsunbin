def move_check(chx,chy,map_array,chdirect):
    if chdirect == 1:
        if (map_array[(chx - 16) // 16][chy // 16] == 1 or map_array[(chx - 16) // 16][chy // 16] == 5):
            # 보드칸 크기가 16 x 16
            chx -= 16
            print(chx, chy)

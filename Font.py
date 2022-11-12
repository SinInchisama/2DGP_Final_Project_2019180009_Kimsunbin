import play_state

def Draw_Num(Num,x,y,sizex,sizey):
    Acount, div = 0, 1
    while Num // div != 0:  # Hp 출력
        result = (Num// div) % 10
        play_state.Font_image.clip_draw(221 + result * 9, 392, 8, 8, x - (Acount * sizex), y, sizex, sizey)
        Acount += 1
        div *= 10

def Draw_Al(Sentence,x,y,sizex,sizey):
    Acount = 0
    for Alpha in Sentence:  # 포켓몬 타입 출력
        if(Alpha == ' '):
            pass
        else:
            play_state.Font_image.clip_draw(167 + ((ord(Alpha) - 97) % 16) * 9, 437 - ((ord(Alpha) - 97) // 16) * 9, 8, 8,x + (Acount * sizex), y, sizex, sizey)
        Acount += 1

def Draw_question(count,x,y,sizex,sizey):
    for i in range(0,count):
        play_state.Font_image.clip_draw(221,402,8,7,x + (i * sizex),y,sizex,sizey)

# Acount = 0
#         for Alpha in Poketmon.Poket_Data[play_state.hero.pList[NowPc].Num].type[i]:  # 포켓몬 타입 출력
#             play_state.Font_image.clip_draw(167 + ((ord(Alpha) - 97) % 16) * 9, 437 - ((ord(Alpha) - 97) // 16) * 9, 8, 8,40 + (Acount * 32), 70 - (32 * i), 32, 32)
#             Acount += 1
#
# j = 0
#     for Alpha in Poketmon.Poket_Data[play_state.hero.pList[NowPc].Num].name:  # 포켓몬 이름 출력
#         play_state.Font_image.clip_draw(167 + ((ord(Alpha) - 97) % 16) * 9, 437 - ((ord(Alpha) - 97) // 16) * 9, 8, 8,264 + (j * 32), 490, 32, 32)
#         play_state.Font_image.clip_draw(167 + ((ord(Alpha) - 97) % 16) * 9, 437 - ((ord(Alpha) - 97) // 16) * 9, 8, 8,335 + (j * 32), 435, 32, 32)
#         j += 1

ABBR_lines = sum(1 for line in open('ABBR-Group.txt'))
HUM_lines = sum(1 for line in open('HUM-Group.txt'))
ENTY_lines = sum(1 for line in open('ENTY-Group.txt'))
LOC_lines = sum(1 for line in open('LOC-Group.txt'))
NUM_lines = sum(1 for line in open('NUM-Group.txt'))
DESC_lines = sum(1 for line in open('DESC-Group.txt'))
TRAIN_lines = sum(1 for line in open('train.txt'))



# print  ("ABBR : "  +  str(ABBR_lines))
# print  ("LOC : "  +  str(LOC_lines))
# print  ("HUM : "  +  str(HUM_lines))
# print  ("ENTY : "  +  str(ENTY_lines))
# print  ("NUM : "  +  str(NUM_lines))
# print  ("DESC : "  +  str(DESC_lines))
# print  ("TRAIN : "  +  str(TRAIN_lines))



prob_ABBR = ABBR_lines/float(TRAIN_lines)
prob_HUM = HUM_lines/float(TRAIN_lines)
prob_ENTY = ENTY_lines/float(TRAIN_lines)
prob_LOC = LOC_lines/float(TRAIN_lines)
prob_NUM = NUM_lines/float(TRAIN_lines)
prob_DESC = DESC_lines/float(TRAIN_lines)






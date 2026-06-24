
def weighted_ensemble_predict(...):

    red_ws = red_row["win_streak"]*0.4 + red_row["knockdown_avg"]*0.30000000000000004 + red_row["submission_avg"]*0.30000000000000004  + red_row["ws"]*0.2 + red_row["reach_in"]*0.1
    blue_ws = blue_row["win_streak"]*0.4 + blue_row["knockdown_avg"]*0.30000000000000004 + blue_row["submission_avg"]*0.30000000000000004   + blue_row["ws"]*0.2 + blue_row["reach_in"]*0.1 

   
    red_all = red_all*(1+red_ws)
    blue_all = blue_all*(1+blue_ws)
    
    blue_oppisite_all = blue_oppisite_all*(1+red_ws)
    red_oppisite_all = red_oppisite_all*(1+blue_ws)
    
    
    red_diff = red_diff*(1+red_ws)
    blue_diff = blue_diff*(1+blue_ws)
    

    blue_oppisite_diff = blue_oppisite_diff*(1+red_ws)
    red_oppisite_diff = red_oppisite_diff*(1+blue_ws)
    

    red_nodiff = red_nodiff*(1+red_ws)
    blue_nodiff = blue_nodiff*(1+blue_ws)
    
    blue_oppisite_nodiff = blue_oppisite_nodiff*(1+red_ws)
    red_oppisite_nodiff = red_oppisite_nodiff*(1+blue_ws)
    

    red_normal = (red_diff+ red_all + red_nodiff)
    red_but_blue_side = (blue_oppisite_diff + blue_oppisite_all + blue_oppisite_nodiff)
    
    red_sum = (red_normal + (red_but_blue_side))

    blue_normal = (blue_diff + blue_all + blue_nodiff)
    blue_but_red_side =(red_oppisite_diff + red_oppisite_all + red_oppisite_nodiff)
    
    blue_sum = (blue_normal + (blue_but_red_side))

    predict_value = f"{r_fighter}" if red_sum > blue_sum else f"{b_fighter}"
    
    red = red_sum/(red_sum+blue_sum)*100
    blue = blue_sum/(red_sum+blue_sum)*100

    return predict_value, red, blue

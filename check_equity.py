'''This script verifies that the equity calculations are working properly on pre-known values'''
import equity
from check_cards import helper_check

# ---- Hands -----
# Hand 1 -- should return 0.145 equity 
flop  = ('Jd','7s','2c')
hero  = ('As','Ks')
range = [('Jh','Jc'), ('Jh','Js'), ('Jc','Js'),
           ('Ah','Jh'), ('Ah','Jc'), ('Ah','Js'),
           ('Ad','Jh'), ('Ad','Jc'), ('Ad','Js'),
           ('Ac','Jh'), ('Ac','Jc'), ('Ac','Js')]

# Chop A -- should turn .5 equity
flop_a  = ('Ad','Kd','Qc')
hero_a  = ('Jh','Th')
range_a = [('Js','Ts')]

# Chop B -- should return .5 equity 
flop_b  = ('Kd','8c','4h')
hero_b  = ('2h','3d')
range_b = [('2s','3c')]


# --- Main Check ----
if __name__ == "__main__":
    
    check_1 = equity.find_equity(flop,hero,range)
    check_2 = equity.find_equity(flop_a,hero_a,range_a)
    check_3 = equity.find_equity(flop_b,hero_b,range_b)

    esti_check1 = equity.estimate_equity(flop,hero,range,100000)

    summary = []

    summary.append(helper_check(.145,check_1,"Exact Equity Check 1"))
    summary.append(helper_check(.5,check_2,"Exact Equity Check 2"))
    summary.append(helper_check(.5,check_3,"Exact Equity Check 3"))
    summary.append(helper_check(.145,esti_check1,"Estimate Equity Check 1"))

    print(f'Equity Test: {sum(summary)} of {len(summary)} passed!')



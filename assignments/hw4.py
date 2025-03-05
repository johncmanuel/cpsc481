def q3(qw,qb,rw,rb,kw,kb,bw,bb,pw,pb):
    return 9*(qw-qb)+5*(rw-rb)+3*(kw-kb)+3*(bw-bb)+1*(pw-pb)

x = q3(0,0,1,2,1,2,2,1,7,6)
print("q3:", x)

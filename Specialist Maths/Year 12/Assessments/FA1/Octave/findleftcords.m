pkg load matgeom
graphics_toolkit gnuplot
cd "/home/noah/Documents/Obsidian/NoahsObsidianSync/NoahsObsidianSync/Specialist Maths/Year 12/Assessments/FA1/Octave/DATA/OLD/"
Eqloader = load("X2.dat")
Eqloader = struct2cell(Eqloader)
Eq = E{1}


XVals = [14, 4, 7, 1, 5, 10, 13, 2, 0]
YVals = [0, -1, -9, -7, -18, -20, -30, -24, -24]


I=4
C=1
Res=1


Z=[10:-1:-10]
if gt(XVals (I+1), XVals(I))
  Start=[XVals(I+1):Res:XVals(I)]
end
if gt(XVals (I), XVals(I+1))
  Start=[XVals(I):Res:XVals(I+1)]
end


hold off
for X=[1:Res:10] Y=[-30:Res:10]
  D=Eq(C,1)*X + Eq(C,2)
  Q=  (Y-Eq(C, 2))  /  Eq(C,1)
  plot(X, D)
  plot(Q, Y)
  hold on
end












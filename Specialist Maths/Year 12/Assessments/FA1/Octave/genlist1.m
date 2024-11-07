pkg load matgeom
graphics_toolkit gnuplot
cd /home/noah/octave
ROW=1
EQNS=zeros(10, 2)

X1 = [14, 4, 7, 1, 5, 10, 13, 2, 0];
Y1 = [0, -1, -9, -7, -18, -20, -30, -24, -24];

X2=[16,14,20,16,20,8,20,14,3,0]
Y2=[0,-4,-8,-10,-13,-16,-22,-32,-26,-26]

hold off
plot(0, 0)

hold on
%finding X1 equations
for J=[0:7]
  K=J+1

  if gt(X1(1+J), X1(2+J))



  h=2
  x=polyfit(X1(J+1:J+2),Y1(J+1:J+2), 1)
  plot(X1(K+1):X1(K) , x(1)*(X1(K+1):X1(K)) + x(2), 'p')
  end


  if gt(X1(2+J), X1(1+J))











  h=1
  x=polyfit(X1(J+1:J+2),Y1(J+1:J+2), 1)
  plot(X1(K):X1(K+1) , x(1)*(X1(K):X1(K+1)) + x(2), 'p')
  end
EQNS(ROW, 1) = x(1)
EQNS(ROW, 2) = x(2)
save X1.dat EQNS
ROW = ROW + 1


  %plotting
%plot(X1(K+1):X1(K) , x(1)*(X1(K+1):X1(K)) + x(2), 'p')
a=(X1(K):X1(K+1))
%plot(X1(K):X1(K+1) , x(1)*(X1(K):X1(K+1)) + x(2), 'p')
line(X1(1:9),Y1(1:9))
line(X2(1:10),Y2(1:10))
axis equal

end


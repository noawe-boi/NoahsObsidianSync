pkg load matgeom
graphics_toolkit gnuplot
close all
rotm = @(a) [cos(a) -sin(a); sin(a) cos(a)];
h = -0.5; # distance from existing polygon
p = [16 14 20 16 20 8 20 14 3 0 0 2 13 10 5 1 7 4 14 16;
     0 -4 -8 -10 -13 -16 -22 -32 -26 -26 -24 -24 -30 -20 -18 -7 -9 -1 0 0];
dp = diff(p, [], 2);
a = atan2 (dp (2, :), dp(1, :));
da = diff (a);
horiz = abs (da) < 16 * eps;
f = 2 * h./sin(da).*sin(da/2);
f(horiz) = h;
f = [h f h];
r = a(1:end-1) + diff(a)/2;
r = pi/2 + [a(1) r a(end)];
p2 = zeros(size(p));

for k=1:columns(p)
  p2(:,k) = p(:,k) + rotm(r(k)) * [f(k); 0];
  line ([p(1, k);p2(1,k)], [p(2, k);p2(2,k)], "color", "magenta");
endfor

line (p(1, :), p(2, :), "color", "green");
line (p2(1, :), p2(2, :), "color", "red");
axis equal
grid on

generated plot

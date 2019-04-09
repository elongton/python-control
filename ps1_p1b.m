m=1; k=1; c=2;
A=[0 1; -k/m -c/m];
Bu=[0; 1/m]; Bw=[0; 1/m];
Cy=[0 1]; Cz=[0 1];
Dyu=0; Dyw=0;
Gyu=ss(A, Bu, Cy, Dyu);
Gyw=ss(A, Bw, Cy, Dyw);
%Part (a) - open loop transfer function
[num_yu, den]=ss2tf(A, Bu, Cy, Dyu);
[num_yw, den]=ss2tf(A, Bw, Cy, Dyw);
[num_yv, den]=ss2tf(A, [0;0], Cy, 1);

Ki=25*0.5; Kp=25;
%convert to state space (not required, but we will use in the next step)
[ac,bc,cc,dc]=tf2ss([Kp Ki], [1 0]);
K=ss(ac,bc,cc,dc);
K
%Find loop TF
Loop=Gyu*K;
%Plot margin with boxes for specs
eT=0.1;wT=1;
eD=0.1;wD=0.1;
eN=0.1;wN=500;
Loopmax=50;
%
[ac,bc,cc,dc]=tf2ss([Kp Ki],[1 0]);
margin(Loop);
h=findall(gcf,'type','axes','visible','on');
subplot(h(1));hold on; axis([0.01 1000 -200 20]); hold off
subplot(h(2));hold on;
    fill([1E-4,1E-4,wT,wT],[0,20*log10(1/eT+1),20*log10(1/eT+1),0],'r');

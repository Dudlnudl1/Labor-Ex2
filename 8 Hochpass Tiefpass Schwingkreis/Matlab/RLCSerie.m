close all
clear all
L=10*10^(-3);
C=100*10^(-9);
f0=1/(2*pi*sqrt(L*C));
R1=22;
%R2=50;

f=linspace(1,10^6,1000);
Xc=1./(2*pi*f*C);
Xl=(2*pi*f*L);
Z1=R1+1./(2*pi*f*C)+2*pi*f*L;
Z01=R1+1./(2*pi*f0*C)+2*pi*f0*L;
%Z2=R2+1./(2*pi*f*C)+2*pi*f*L;
%Z02=R2+1./(2*pi*f0*C)+2*pi*f0*L;
phi=atan((Xc-Xl)/R1)*180/pi;
figure
loglog(f,Z1)
hold on
loglog(f0,Z01,'x')

loglog(f,Xc)
loglog(f,Xl)
hold off
title('RLC Kreis mit R=22 / \Omega ')
grid on
legend('Gesamtimpendanz','Resonanzfrequenz','Impedanz x_c','Impedanz x_L')
ylabel('Impedanz \Omega')
xlabel('f / Hz')

figure
semilogx(f,phi)
grid on
title('Phasenwinkel \phi')


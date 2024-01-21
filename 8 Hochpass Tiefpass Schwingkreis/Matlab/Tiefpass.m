clear all
close all
R=3300;
C=100*10^(-9);
fg=1/(2*pi*R*C);

f=linspace(1,10^5,10000);

Ut=1./(1+2*pi*f*R*C);
Utg=1/(1+2*pi*fg*R*C)
phit=atan(2*pi*f*R*C)*360/(2*pi);
phitg=atan(2*pi*fg*R*C)*360/(2*pi)
figure
loglog(f,20*Ut)
hold on
loglog(fg,20*Utg,'x')
hold off
grid on
xlabel('f /Hz')
ylabel('Amplitudengang / ')
title('Bodeidagramm des Amplitudengangs Tiefpass')
legend('Amplitudengang','Grenzfrequenz')

figure
semilogx(f,phit)
grid on
hold on
semilogx(fg,phitg,'x')
hold off
xlabel('f /Hz')
ylabel('Phasenwinkel \phi')
title('Bodediagramm des Phasenwinkels Tiefpass')
legend('Phasenwinkel','Grenzfrequenz')

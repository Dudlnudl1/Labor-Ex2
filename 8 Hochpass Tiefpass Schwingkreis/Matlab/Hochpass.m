clear all
close all
R=33;
L=10*10^(-3);

fg=R/(2*pi*L);

f=linspace(1,10^5,10000);

Uh=2*pi*f*L./sqrt(R^2+(2*pi*f*L).^2);
Uhg=2*pi*fg*L./sqrt(R^2+(2*pi*fg*L).^2)
phih=-acot(2*pi*f*L/R)*180/(pi);
phihg=acot(2*pi*fg*L/R)*180/(pi)
figure
loglog(f,20*Uh)
hold on
loglog(fg,20*Uhg,'x')
hold off
grid on
xlabel('f /Hz')
ylabel('Amplitudengang /')
title('Bodediagramm des Amplitudengangs Hochpass')
legend('Amplitudengang','Grenzfrequenz')

figure
semilogx(f,phih)
grid on
hold on
semilogx(fg,phihg,'x')
hold off
xlabel('f /Hz')
ylabel('Phasenwinkel \phi')
title('Bodediagramm des Phasenwinkels Hochpass')
legend('Phasenwinkel','Grenzfrequenz')

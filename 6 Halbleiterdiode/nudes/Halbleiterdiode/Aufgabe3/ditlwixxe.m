% Dateipfad zur CSV-Datei mit den Daten
dateiPfad = '.\GonzVülOhm\100uF\1.csv'; % Passe dies entsprechend an

% Daten aus der CSV-Datei laden (angenommen, die Datei hat Header-Zeilen)
daten = csvread(dateiPfad, 3, 0);

% Wert in Spalte 5 (Index 5) extrahieren
wertSpalte5 = daten(:, 5);

% Root Mean Square (RMS) berechnen
rmsWert = rms(wertSpalte5);

%Mittelwert berechnen
meanWert = mean(wertSpalte5);

% Ergebnis ausgeben
fprintf('Der Root Mean Square (RMS) Wert für Spalte 5 beträgt: %.4f\n', rmsWert);
fprintf('Der Mittelwert Wert für Spalte 5 beträgt: %.4f\n', meanWert);



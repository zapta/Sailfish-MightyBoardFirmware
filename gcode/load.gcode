; A script to load a new filamet on ffc. 
; WORK IN PROGRESS, NOT FULLY FUNCTIONAL
;
; See GCODE reference at https://reprap.org/wiki/G-code
; This is for a single extruder machine with 'right' extruder only.

G90 ; Absolute distance mode (for X, Y, Z).
M83 ; Extruder distances are relative.
M135 T0 ; We use offsets of right extruder 
M18 X Y Z ; disable steppers

M73 P0 ; Enable build prorgress indicator
M73 P1 ; set progress to 1%

; Start heating right extruder to 220C.
;M104 S220 T0
M104 S40 T0 ; start heating extruder
M133 T0  ; wait until extruder temprerature reached.

;G92 A0 B0 ; zero extruders (?)

; --- Step1 - Initial load
G4 P500 ; wait for completion
M70 (Unloading...)
G1 E10 F300 ; Push a small amount of fillament to free the extruder.

; --- Step2 - Unload
G4 P500
G1 E-50 F300  ; Pull fillament

; --- Step3 - Wait for loading
; Display message and wait for click
; Using timeout to make sure we don't hold the nozzle hot indefinitly.
; NOTE: M70 delay P is in secs, not millis.
M71 P300 (Press OK to start)


; --- Step3 - Wait for loading
G4 P100
M73 P99 ; Set progress to 99%
; TODO(zapta): remove the delay here and made the message screen existing when printing done.
; NOTE: M70 delay P is in secs, not millis.
M70 P36 (Loading...)

G1 E200  F300  
G4 P500 

M140 S0 T0 ; cool down HBP
M104 S0 T0 ; cool down right extruder
M104 S0 T1 ; cool down left extruder

M18 ; disable all steppers
M72 P1 ; play Ta-Da song
M73 P100  ; progress 100%.
G4 P100 

;M18 ; disable stepper

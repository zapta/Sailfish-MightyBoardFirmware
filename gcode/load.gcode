; A script to load a new filamet on ffc. 
; WORK IN PROGRESS, NOT FULLY FUNCTIONAL

G90
M83

; **** Replicator 1 dual start.gcode ****

M73 P0 ; enable build progress
M73 P1 ; enable build progress

;G162 X Y F3000 ; home XY maximum
;G161 Z F1200 ; home Z minimum
;G92 Z-5 ; set Z to -5
;G1 Z0 ; move Z to 0
;G161 Z F100 ; home Z slowly
;M132 X Y Z A B ; recall home offsets

M135 T0 ; load right extruder offsets

; NOTE(zapta): change X from 150 to 120 to solve X home offset dependency.
;G1 X120 Y-70 Z30 F9000 ; move to wait position right hand side of the table

;G130 X20 Y20 Z20 A20 B20 ; lower stepper Vrefs while heating

; Turn off the material cooling fan(s)?
M127

;M140 S60 T0
;M134 T0 ; stabilize bed temperature

; Start heating right extruder to 190c.
M104 S190 T0
; stabilize right extruder temperature
M133 T0 

;G130 X127 Y127 Z40 A127 B127 ; default stepper Vrefs

; zero extruders
G92 A0 B0 

;;G1 Z0.4 ; position nozzle
; NOTE(zapta): modified to have the swipe entirely within the bed area
;;G1 X110 Y-70 E25 F300 ; purge nozzle
;G1 X120 Y-70 Z0.15 F1200 ; slow wipe
;G1 X110 Y-70 Z0.5 F1200 ; lift

; load
G1 E40 F300 

;G1 X100 Y-70 E25 F300 ; purge nozzle
;G1 X110 Y-70 Z0.15 F1200 ; slow wipe
;G1 X100 Y-70 Z0.5 F1200 ; lift
;----

G92 A0 B0 ; zero extruders
;M73 P1 ;@body (notify GPX body has started)

; unload
G1 E-100 F300  

; Display message and wait for click
M71 (Loading                                              Press OK to load)

; Display message and continue
M70 (111                                                                  )

; zero extruders
G92 A0 B0 
; load
G1 E100  F300  

;G1 Z0.180 F1200
; layer 1, Z = 0.18
;M135 T0
; tool H0.200 W0.400
; skirt
;G4 P6000000  ; wait

M73 P100  ; progress done.

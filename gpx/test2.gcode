; Set all positioning to absolute
G90  
; Set extruder to relative
M83
; **** Replicator 1 dual start.gcode ****
; Set progress to 0%
M73 P0 ; enable build progress
G162 X Y F3000 ; home XY maximum
G161 Z F1200 ; home Z minimum
G92 Z-5 ; set Z to -5
G1 Z0 ; move Z to 0
G161 Z F100 ; home Z slowly
; Active auto leveling?
M132 X Y Z A B ; recall home offsets
; Select extruder T0
M135 T0 ; load right extruder offsets
G1 X150 Y-70 Z30 F9000 ; move to wait position right hand side of the table
G130 X20 Y20 Z20 A20 B20 ; lower stepper Vrefs while heating
; disable cooling fan?
M127
; Set bed tempreature
;;;M140 S60 T0
;;;M134 T0 ; stabilize bed temperature
; Set extruder temperature
;;;M104 S230 T0
;;;M133 T0 ; stabilize right extruder temperature
; Restore actual stepper currents
G130 X127 Y127 Z40 A127 B127 ; default stepper Vrefs
G92 A0 B0 ; zero extruders
G1 Z0.4 ; position nozzle
G1 X110 Y-70 E25 F300 ; purge nozzle
G1 X120 Y-70 Z0.15 F1200 ; slow wipe
G1 X110 Y-70 Z0.5 F1200 ; lift
G92 A0 B0 ; zero extruders
; set progress to 1%
M73 P1 ;@body (notify GPX body has started)
; **** end of start.gcode ****
G1 E-1.0000 F1200
G1 Z0.180 F1200
; layer 1, Z = 0.18
M135 T0
; tool H0.200 W0.400
; skirt
;;;G1 X4.529 Y-9.366 F4200
; move to 0, 0
G1 X0 Y0 Z10 F9000
; wait 1 minute
G4 P60000

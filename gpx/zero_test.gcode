; NOTE(zapta): this gcode is used to test the zero offset
; of the Simplify3D start script. if the X value in the G1
; comand that moves that move the extruder to the front/right
; corner is too high, the printer X zero is skewed to the 
; left.
;
; Working values: 
;
;   Printer Utilities settings:
;     Number of extruders: 1
;     Home Offset X:  119
;     Home Offset Y:  72
;     Home Offset Z:  0 
;
;   Simplify3D startup script
;     G1 X move : 120
;
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
;;;;;G1 X150 Y-70 Z30 F9000 ; move to wait position right hand side of the table
G1 X120 Y-70 Z30 F9000 ; move to wait position right hand side of the table
;----- move to 0,0 and wait
G1 X0 Y0 Z10 F9000
G4 P60000  ; wait 60 sec (does this work?)
;--

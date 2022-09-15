// Connections
//
#define GetButton     ~ PORTB.B5
//
sbit Red            at LATB4_bit;  // logic "1" turns LED off
sbit Green          at LATB3_bit;  // logic "1" turns LED off
sbit OLED_PWD       at LATA4_bit;  // logic "1" powers OLED up
sbit AD8361_PWD     at LATE2_bit;  // logic "1" disables AD8361
sbit C_sw           at LATE0_bit;  // selects either CL or LC circuit
sbit L_010          at LATD7_bit;
sbit L_022          at LATD6_bit;
sbit L_045          at LATD5_bit;
sbit L_100          at LATD4_bit;
sbit L_220          at LATC7_bit;
sbit L_450          at LATC6_bit;
sbit L_1000         at LATC5_bit;
sbit C_22           at LATA5_bit;
sbit C_47           at LATE1_bit;
sbit C_100          at LATA7_bit;
sbit C_220          at LATA6_bit;
sbit C_470          at LATC0_bit;
sbit C_1000         at LATC1_bit;
sbit C_2200         at LATC2_bit;
sbit Rel_to_gnd     at LATD3_bit;
sbit Rel_to_plus_N  at LATC4_bit;

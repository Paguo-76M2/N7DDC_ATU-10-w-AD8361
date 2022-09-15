// pic_init unit for Micro C PRO
// David Fainitski for ATU-10 project
// 2020, 2022

void pic_init (void) {
// ports initialisation
  ANSELA = 0;         // all as digital
  ANSELB = 0;         // all as digital
  ANSB0_bit = 1;      // analog input, V_forward
  ANSB1_bit = 1;      // analog input, V_battery
  ANSB2_bit = 1;      // analog input, V_reflected
  ANSELC = 0;         // all as digital
  ANSELE = 0;         // all as digital
  ANSELD = 0;         // all as digital

  C1ON_bit = 0;      // Disable comparators
  C2ON_bit = 0;

  PORTA = 0;
  PORTB = 0;
  PORTC = 0;
  PORTD = 0;
  PORTE = 0;
  LATA = 0b00000000;
  LATB = 0b00000000;
  LATC = 0b00010000;
  LATD = 0b00000110;
  LATE = 0b00000000;
  TRISA = 0b00000000;
  TRISB = 0b00100111;
  TRISC = 0b00000000;
  TRISD = 0b00000000;
  TRISE = 0b00000000;

  // open drains
  ODCA2_bit = 1;	// i2c SDA
  ODCA3_bit = 1;	// i2c SCL
  ODCD1_bit = 1;	// remote control RING
  ODCD2_bit = 1;	// remote control TIP
  
  // Timer0 settings
  T0CS0_bit = 0; // Fosc/4
  T0CS1_bit = 1;
  T0CS2_bit = 0;
  T016BIT_bit = 1;
  TMR0L = 0xC0;   // 8_000 cycles to OF
  TMR0H = 0xE0;
  TMR0IF_bit = 0;
  T0EN_bit = 1;
  TMR0IE_bit = 1;
  
  // Modules disable
  PMD0 = 0b00011110; // ON: IRQonChange, FixVoltRef, SysClkNet
  PMD1 = 0b11111110; // ON: Timer0; OFF: all other
  PMD2 = 0b01000111; // ON: ADC; OFF: all other
  PMD3 = 0b01111111; // ON: nothing (PWMs)
  PMD4 = 0b01110111; // ON: nothing
  PMD5 = 0b11011111; // ON: nothing
  //interrupt setting
  GIE_bit = 1;
  Delay_ms (100);
  return;
}

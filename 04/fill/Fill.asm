// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.


//START
@SCREEN
D=A
@pixel	//use pixel as a variable that holds the address of the current pixel
M=D  //initialize it to the top left pixel of the screen

@KBD //input
D=M
@WHITE
D;JEQ
@BLACK
0;JMP

//WHITE
@pixel
M=1
@NEXT
0;JMP

//BLACK
@pixel
M=0
@NEXT
0;JMP

@pixel	//set pixel to pixel + 1
D=M+1
M=D
@KBD
D=A-D
@START
D;JEQ
0;JMP
// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

@sum	//Initialize sum to 0
M=0
@R1
D=M
@count  //Initialize count to the value at RAM[1]
M=D

//Loop
@count
D=M
@END	//Check if count is 0, if so go END
D;JEQ
@R0
D=M
@sum	//Add RAM[0] to sum
M=M+D
@count  //Decrement count by 1
M=M-1
@Loop	//loop again
0;JMP

//END
@sum
D=M
@R2	//write sum to RAM[2]
M=D
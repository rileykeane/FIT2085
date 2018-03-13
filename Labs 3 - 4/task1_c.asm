# @author Riley Keane
# @since 12/3/18
# @modified 12/3/18

.data
	prompt:		.asciiz "Enter a year: "
	leap:		.asciiz "Not a leap year"
	notLeap: 	.asciiz "Is a leap year"
	newLine: 	.asciiz "\n"

.text
main:	addi $fp, $sp, 0
	addi $sp, $sp, -4

	addi $v0, $0, 4
	la $a0, prompt
	syscall
	
	addi $v0, $0, 5
	syscall
	sw $v0, -4($fp)
	
	lw $t0, -4($fp)
	addi $t1, $0, 4
	
	# year % 4

	
	
			
